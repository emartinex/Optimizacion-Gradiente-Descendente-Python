# Guía de uso de los notebooks

## 1. Objetivo

Resolver problemas básicos de optimización diferenciable mediante solución analítica y método numérico de gradiente descendente, e interpretar el historial de convergencia.

## 2. Orden recomendado

1. Lee las secciones 1 a 3 sobre optimización, derivadas y tamaño de paso.
2. Ejecuta las celdas de importación y definición de funciones (secciones 4 a 8).
3. Reproduce el ejercicio $f(x)=(x-3)^2$ en la sección 9.
4. Observa la oscilación del ejemplo con $\alpha=1$ en la sección 10.
5. **Sección 11:** ejecuta el asistente de captura; o **sección 12:** edita `configuracion` para evitar preguntas.
6. Interpreta los puntos críticos, la tabla de iteraciones y las gráficas.

## 3. Captura de datos

| Campo | Ejemplo | Descripción |
| --- | --- | --- |
| Función | `(x-3)^2` | Función objetivo a minimizar |
| Variables | `x` o `x,y` | Variables separadas por comas |
| Punto inicial | `0` o `4,3` | Coordenada inicial de cada variable, en orden |
| Tasa `alpha` | `0.25` | Tamaño de paso positivo |
| Iteraciones | `500` | Número máximo de actualizaciones |
| Tolerancia | `1e-8` | Umbral de la norma del gradiente |
| Retroceso Armijo | `s` o `n` | Ajuste adaptativo del tamaño de paso |

Si ejecutas el notebook completo y no deseas detenerte en las preguntas, cambia `MODO_INTERACTIVO = True` por `False` en la sección 11. Después usa la configuración manual de la sección 12.

## 4. Ejemplos de expresiones

```python
"(x-3)^2"                           # Parabólica, 1 variable
"(x-1)^2 + 3*(y+2)^2"             # Cuadrática, 2 variables
"x^2 + y^2 + z^2"                 # 3 variables
"100*(y-x^2)^2 + (1-x)^2"         # Rosenbrock, no convexa
"sin(x) + x^2/10"                 # Función trigonométrica
"exp(x) + (x-1)^2"                # Función exponencial
"log(x) + x^2"                    # Dominio: x > 0
```

**Sintaxis:** escribe `2*x`, no `2x`. Se admiten las potencias `x^2` y `x**2`. El separador decimal es punto (`0.25`). Para `log(x)`, `sqrt(x)` y otras expresiones con dominio restringido, elige un punto inicial válido; los pasos podrían salir del dominio.

## 5. Fórmulas principales

Para una variable:

$$x_{k+1}=x_k-\alpha f'(x_k)$$

Para varias variables:

$$\mathbf{x}_{k+1}=\mathbf{x}_k-\alpha\nabla f(\mathbf{x}_k)$$

Una medida frecuente de paro es $\|\nabla f(\mathbf{x}_k)\|\leq\varepsilon$.

Para buscar puntos estacionarios de manera analítica:

$$\nabla f(\mathbf{x})=\mathbf{0}$$

Si la Hessiana es definida positiva en un punto crítico, es un mínimo local estricto; si es definida negativa, es un máximo local estricto; si es indefinida, es un punto de silla. En otros casos, la prueba puede ser inconclusa.

## 6. Interpretación de la salida

- **Solución analítica:** candidatos encontrados por SymPy y clasificación cuando es posible; pueden omitirse soluciones paramétricas o casos sin forma cerrada.
- **Estado:** convergencia por tolerancia, máximo de iteraciones, oscilación, estancamiento, divergencia o problema de dominio.
- **Tabla de historial:** coordenadas, derivadas, costo, norma del gradiente y tamaño de paso realmente aplicado.
- **Gráficas:** evolución del costo y del gradiente; ruta de la optimización en una o dos variables.

Una norma del gradiente pequeña **no demuestra por sí sola** que el punto sea un mínimo global.

## 7. Exportación a CSV

Después de ejecutar la sección 12:

```python
resultado_manual["historial"].to_csv("iteraciones_ejercicio.csv", index=False)
```

El archivo se guarda en el directorio de ejecución del notebook y puede descargarse desde el entorno. Los archivos `iteraciones_*.csv` se ignoran en Git para evitar subir resultados temporales por accidente.
