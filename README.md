# Optimización matemática con gradiente descendente en Python

**Proyecto didáctico con notebooks de Jupyter y Google Colab** para aprender, implementar y visualizar el método de gradiente descendente, desde la derivación matemática hasta la comparación de resultados analíticos y numéricos.

## Descripción

En optimización buscamos minimizar una **función objetivo** o **función de costo**. El método de gradiente descendente actualiza iterativamente una variable o un vector de variables en dirección opuesta a la derivada o al gradiente:

$$
\mathbf{x}_{k+1}=\mathbf{x}_{k}-\alpha\,\nabla f(\mathbf{x}_{k})
$$

Donde:

- $\mathbf{x}_{k}$: punto o parámetros en la iteración $k$.
- $\alpha > 0$: tasa de aprendizaje o tamaño de paso.
- $\nabla f(\mathbf{x}_{k})$: gradiente de la función de costo.
- $\mathbf{x}_{k+1}$: nuevo punto calculado.

El propósito del proyecto es **explicar el procedimiento matemático**, facilitar la experimentación y mostrar por qué la elección del tamaño de paso determina la convergencia, la oscilación o la divergencia.

## Características

- Fundamentos de optimización, minimización, función objetivo, gradiente y Hessiana.
- Cálculo simbólico de derivadas parciales mediante **SymPy**.
- Búsqueda de **puntos estacionarios** y clasificación local mediante la Hessiana cuando es posible.
- Solución iterativa con **gradiente descendente** usando NumPy.
- Tamaño de paso fijo y opción de **búsqueda por retroceso de Armijo**.
- Captura interactiva de la función, variables, valores iniciales y parámetros.
- Opción de configuración manual para repetir prácticas sin responder preguntas.
- Explicación de las primeras iteraciones, tablas con Pandas y comparación con resultados analíticos disponibles.
- Gráficas de evolución del costo y de la norma del gradiente; trayectoria en 1D o contornos en 2D.
- Ejemplos de convergencia y oscilación por elección inadecuada de la tasa de aprendizaje.

> **Alcance matemático:** el proyecto maneja muchas funciones diferenciables, pero no garantiza resolver analíticamente cualquier expresión ni hallar un mínimo global en funciones no convexas. Está orientado a optimización **sin restricciones**; la visualización de trayectorias está disponible en una y dos dimensiones.

## Estructura del repositorio

```text
gradiente-descendente-github/
├── README.md
├── requirements.txt
├── .gitignore
├── notebooks/
│   ├── Optimizacion_Gradiente_Descendente_Interactivo.ipynb
│   └── Optimizacion_Gradiente_Descendente_Ejemplos_Resueltos.ipynb
├── docs/
│   ├── GUIA_DE_USO.md
│   ├── EJERCICIOS.md
│   └── PUBLICAR_EN_GITHUB.md
└── tests/
    └── test_gradiente.py
```

## Inicio rápido con Google Colab

1. Abre [Google Colab](https://colab.research.google.com/).
2. Selecciona **Archivo → Subir notebook** (la ubicación del menú puede variar).
3. Sube `notebooks/Optimizacion_Gradiente_Descendente_Interactivo.ipynb`.
4. Ejecuta las celdas en orden. La primera celda de código instala dependencias faltantes.
5. En la sección **11** introduce los datos del problema o edita la configuración de la sección **12**.

También puedes abrir el notebook directamente desde GitHub utilizando **Archivo → Abrir notebook → GitHub** en Colab una vez publicado el repositorio.

## Ejecución local (Jupyter Notebook)

Requisito recomendado: **Python 3.10 o posterior**.

```bash
# 1. Clonar una vez que el repositorio exista
git clone https://github.com/TU_USUARIO/TU_REPOSITORIO.git
cd TU_REPOSITORIO

# 2. Crear y activar un entorno virtual (Linux/macOS)
python -m venv .venv
source .venv/bin/activate

# En Windows PowerShell, en lugar del comando anterior:
# .venv\Scripts\Activate.ps1

# 3. Instalar las bibliotecas
python -m pip install -r requirements.txt

# 4. Iniciar Jupyter
jupyter notebook
```


## Ejemplo de referencia

Minimizar:

$$f(x)=(x-3)^2$$

**Solución analítica:**

$$f'(x)=2(x-3)=0\quad\Longrightarrow\quad x^*=3,\qquad f(3)=0.$$

**Gradiente descendente:** con $x_0=0$ y $\alpha=0.25$,

$$x_{k+1}=x_k-0.25\,[2(x_k-3)].$$

| Iteración $k$ | $x_k$ | $f'(x_k)$ | $f(x_k)$ |
| ---: | ---: | ---: | ---: |
| 0 | 0 | -6 | 9 |
| 1 | 1.5 | -3 | 2.25 |
| 2 | 2.25 | -1.5 | 0.5625 |
| 3 | 2.625 | -0.75 | 0.140625 |
| 4 | 2.8125 | -0.375 | 0.03515625 |

Al continuar, $x_k$ se acerca a $3$ y el costo tiende a $0$.

Con $\alpha=1$ para este mismo ejemplo, la secuencia oscila entre $x=0$ y $x=6$, por lo que **no converge**.

## Formular un ejercicio propio

Ejemplo de dos variables:

```python
configuracion = {
    "funcion": "(x-1)^2 + 3*(y+2)^2",
    "variables": "x,y",
    "punto_inicial": [4.0, 3.0],
    "alpha": 0.10,
    "max_iter": 500,
    "tolerancia": 1e-8,
    "retroceso": False,
}
```

En la sección 12 del notebook puedes cambiar esta configuración; el algoritmo calcula derivadas, intenta clasificar los puntos críticos y genera el historial numérico.

La sintaxis de las funciones emplea `*` para multiplicar, `^` o `**` para potencias y nombres de funciones como `sin`, `cos`, `exp`, `log` y `sqrt`. Consulta [la guía de uso](docs/GUIA_DE_USO.md) para más ejemplos.

## Notebooks incluidos

| Archivo | Uso |
| --- | --- |
| [Notebook interactivo](notebooks/Optimizacion_Gradiente_Descendente_Interactivo.ipynb) | Para ejecutar actividades, capturar datos y probar nuevas funciones. |
| [Notebook con ejemplos resueltos](notebooks/Optimizacion_Gradiente_Descendente_Ejemplos_Resueltos.ipynb) | Para consultar celdas ejecutadas, tablas y gráficas de referencia. |

La versión con resultados sirve como evidencia didáctica; para experimentar libremente es preferible utilizar el notebook interactivo.

## Validación

Las pruebas automatizadas comprueban la estructura de los notebooks y casos básicos de convergencia y oscilación:

```bash
python -m unittest discover -s tests -v
```

Consulta también los [ejercicios propuestos](docs/EJERCICIOS.md) y las [instrucciones para publicar en GitHub](docs/PUBLICAR_EN_GITHUB.md).

## Aplicación en inteligencia artificial

Gradiente descendente es un algoritmo fundamental de optimización empleado para ajustar parámetros en numerosos modelos de aprendizaje automático. En redes neuronales se utiliza, junto con otras técnicas como retropropagación y optimizadores derivados, para reducir una función de pérdida durante el entrenamiento.

## Limitaciones y consideraciones

- **Puntos estacionarios no equivalen siempre a mínimos**: pueden ser máximos, puntos de silla o casos inconclusos.
- **La solución analítica puede no existir en forma cerrada** o no ser obtenida por SymPy.
- **Una tasa de aprendizaje incorrecta puede causar oscilación, divergencia o estancamiento.**
- **Las funciones no convexas pueden presentar mínimos locales.** El resultado depende del punto inicial.
- **No se admiten restricciones** de igualdad/desigualdad ni derivadas no definidas en el punto de evaluación como un caso general.
- El intérprete de expresiones permite únicamente un subconjunto de operaciones matemáticas; no está diseñado como servicio público para expresiones arbitrarias de terceros.
