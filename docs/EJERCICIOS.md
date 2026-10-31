# Ejercicios propuestos de gradiente descendente

Estos ejercicios permiten comparar método analítico y método numérico. Trabaja con distintas tasas de aprendizaje y puntos iniciales, y registra el comportamiento observado.

## Ejercicio 1. Mínimo de una parábola

- $f(x)=(x-3)^2$
- $x_0=0$, $\alpha=0.25$
- Calcula a mano las primeras cinco iteraciones.
- **Referencia analítica:** $x^*=3$, $f(x^*)=0$.

## Ejercicio 2. Función cuadrática desplazada

- $f(x)=(x-5)^2+2$
- $x_0=-1$, $\alpha=0.2$
- Identifica el punto donde la derivada es cero.
- **Referencia analítica:** $x^*=5$, $f(x^*)=2$.

## Ejercicio 3. Dos variables

- $f(x,y)=(x-1)^2+3(y+2)^2$
- $(x_0,y_0)=(4,3)$, $\alpha=0.1$
- Calcula el gradiente, la Hessiana y el punto crítico.
- **Referencia analítica:** $(x^*,y^*)=(1,-2)$, $f(x^*,y^*)=0$.

## Ejercicio 4. Influencia de la tasa de aprendizaje

- Usa $f(x)=(x-3)^2$, $x_0=0$.
- Prueba $\alpha=0.1$, $0.25$, $0.75$ y $1$.
- Compara la cantidad de iteraciones y el comportamiento gráfico.
- **Pista:** con $\alpha=1$ el método alterna entre $0$ y $6$ y no converge.

## Ejercicio 5. Función no convexa

- $f(x,y)=100(y-x^2)^2+(1-x)^2$ (función de Rosenbrock).
- Prueba $(x_0,y_0)=(-1.2,1)$ con $\alpha=0.001$ y luego con retroceso de Armijo.
- Compara las rutas y observa cómo una tasa grande puede generar problemas numéricos.
- **Referencia:** el punto $(1,1)$ es un mínimo global y $f(1,1)=0$; hallar ese punto numéricamente puede requerir muchas iteraciones.

## Ejercicio 6. Tres variables

- $f(x,y,z)=(x-2)^2+2(y+1)^2+4(z-3)^2$.
- $(x_0,y_0,z_0)=(0,0,0)$, $\alpha=0.1$.
- Verifica las derivadas parciales y compara con el resultado numérico.
- **Referencia analítica:** $(2,-1,3)$, con costo mínimo $0$.
- La gráfica de trayectoria no se dibuja en tres variables; sí están disponibles las gráficas de costo y norma del gradiente.

## Guía breve para entregar la actividad

En cada ejercicio documenta: función objetivo, derivadas, punto crítico y su clasificación (si existe), parámetros iniciales, primeras cinco iteraciones, tabla, gráficas, estado de finalización e interpretación del comportamiento numérico.
