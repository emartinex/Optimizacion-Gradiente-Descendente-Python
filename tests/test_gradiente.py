"""Pruebas de estructura y comportamiento del notebook educativo.

Ejecución desde la raíz:
    python -m unittest discover -s tests -v
"""
from __future__ import annotations

import contextlib
import io
import json
import unittest
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
INTERACTIVO = ROOT / "notebooks" / "Optimizacion_Gradiente_Descendente_Interactivo.ipynb"
RESUELTOS = ROOT / "notebooks" / "Optimizacion_Gradiente_Descendente_Ejemplos_Resueltos.ipynb"


def cargar():
    with INTERACTIVO.open(encoding="utf-8") as archivo:
        nb = json.load(archivo)
    espacio = {"__name__": "__test_notebook__"}
    # Ejecutar sólo las definiciones; no se capturan datos ni se trazan gráficos.
    with contextlib.redirect_stdout(io.StringIO()):
        for indice in (5, 7, 9, 11):
            codigo = "".join(nb["cells"][indice]["source"])
            exec(compile(codigo, f"celda_{indice}.py", "exec"), espacio)
    return espacio


class PruebasNotebook(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.e = cargar()

    def test_archivos_json_validos(self):
        for ruta in (INTERACTIVO, RESUELTOS):
            with self.subTest(archivo=ruta.name):
                with ruta.open(encoding="utf-8") as archivo:
                    nb = json.load(archivo)
                self.assertEqual(nb["nbformat"], 4)
                self.assertGreaterEqual(len(nb["cells"]), 20)
                self.assertIn("kernelspec", nb["metadata"])

    def test_derivada_y_solucion_analitica(self):
        p = self.e["ProblemaOptimizacion"]("(x-3)^2", "x")
        self.assertEqual(str(p.gradiente_simbolico[0]), "2*x - 6")
        self.assertAlmostEqual(p.valor([3.0]), 0.0)
        self.assertTrue(np.allclose(p.gradiente([0]), [-6]))
        tabla = self.e["solucion_analitica"](p)
        self.assertAlmostEqual(float(tabla.iloc[0]["x*"]), 3.0)
        self.assertEqual(tabla.iloc[0]["Clasificación Hessiana"], "Mínimo local estricto")

    def test_primeras_iteraciones(self):
        p = self.e["ProblemaOptimizacion"]("(x-3)^2", "x")
        r = self.e["gradiente_descendente"](p, [0], alpha=0.25, max_iter=4)
        self.assertTrue(np.allclose(r["trayectoria"][:, 0], [0, 1.5, 2.25, 2.625, 2.8125]))
        self.assertAlmostEqual(float(r["historial"].iloc[2]["f(x)"]), 0.5625)

    def test_convergencia_una_variable(self):
        p = self.e["ProblemaOptimizacion"]("(x-3)^2", "x")
        r = self.e["gradiente_descendente"](p, [0], alpha=0.25, max_iter=200)
        self.assertIn("Convergió", r["estado"])
        self.assertAlmostEqual(r["punto_final"][0], 3.0, places=6)
        self.assertLess(r["valor_final"], 1e-10)

    def test_oscilacion_paso_uno(self):
        p = self.e["ProblemaOptimizacion"]("(x-3)^2", "x")
        r = self.e["gradiente_descendente"](p, [0], alpha=1.0, max_iter=12)
        self.assertIn("Oscilación", r["estado"])
        self.assertTrue(np.allclose(r["trayectoria"][:3, 0], [0, 6, 0]))

    def test_dos_variables(self):
        p = self.e["ProblemaOptimizacion"]("(x-1)^2 + 3*(y+2)^2", "x,y")
        r = self.e["gradiente_descendente"](p, [4, 3], alpha=0.1, max_iter=500)
        self.assertTrue(np.allclose(r["punto_final"], [1, -2], atol=1e-5))
        self.assertLess(r["valor_final"], 1e-10)

    def test_bloqueo_de_expresiones_no_admitidas(self):
        with self.assertRaises(ValueError):
            self.e["ProblemaOptimizacion"]("__import__('os').system('echo hola')", "x")


if __name__ == "__main__":
    unittest.main()
