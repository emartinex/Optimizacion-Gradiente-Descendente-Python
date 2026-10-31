# Publicar este proyecto en GitHub

## Información lista para copiar

**Nombre sugerido del repositorio:** `gradiente-descendente-optimizacion-python`

**Descripción corta (About):**

> Notebooks educativos de Jupyter y Google Colab para aprender optimización con gradiente descendente, solución analítica, derivadas simbólicas, iteraciones y visualización en Python.

**Temas (topics) sugeridos:**

`python`, `jupyter-notebook`, `google-colab`, `gradient-descent`, `optimization`, `sympy`, `numpy`, `matplotlib`, `machine-learning`, `educacion`

**Mensaje sugerido del primer commit:**

`docs: publicar notebooks didácticos de gradiente descendente`

## Opción A. Publicación desde el navegador

1. Entra a [GitHub](https://github.com/) e inicia sesión.
2. Selecciona **New repository** (Nuevo repositorio).
3. Escribe el nombre y la descripción sugeridos.
4. Elige **Public** o **Private** según tu preferencia.
5. Como esta carpeta ya contiene `README.md`, no necesitas crear otro README desde GitHub.
6. Crea el repositorio.
7. En el repositorio vacío, selecciona **uploading an existing file** o **Add file → Upload files**, según la interfaz.
8. **Descomprime el ZIP y sube el contenido de la carpeta, no el ZIP como único archivo.** Conserva la estructura `notebooks/`, `docs/` y `tests/`.
9. Confirma los cambios y comprueba que `README.md` se visualiza en la portada.

**Importante:** algunos navegadores o interfaces de carga pueden omitir archivos ocultos como `.gitignore`. Para conservar todos los archivos es más confiable la opción B con Git.

## Opción B. Publicación desde la terminal con Git

Crea primero un repositorio **vacío** en GitHub (sin README, licencia ni `.gitignore` automáticos). Luego ejecuta desde la carpeta descomprimida:

```bash
git init
git branch -M main
git add .
git commit -m "docs: publicar notebooks didacticos de gradiente descendente"
git remote add origin https://github.com/TU_USUARIO/gradiente-descendente-optimizacion-python.git
git push -u origin main
```

Sustituye `TU_USUARIO` por tu cuenta o nombre de organización. La primera vez que utilices Git quizá necesites configurar tu identidad local (`git config --global user.name` y `git config --global user.email`) e iniciar sesión mediante el método de autenticación que GitHub indique. No incluyas tokens o contraseñas en archivos del proyecto.

## Comprobación después de subir

- Verifica que aparece el `README.md` en la página principal.
- Abre cada notebook en `notebooks/` para comprobar que GitHub lo renderiza.
- Abre `docs/GUIA_DE_USO.md` y `docs/EJERCICIOS.md`.
- Ejecuta `python -m unittest discover -s tests -v` en un entorno con dependencias instaladas.
- Abre el notebook interactivo desde Google Colab y ejecuta las primeras secciones.

## Licencia, autoría y mantenimiento

**Antes de publicarlo**, decide si quieres añadir un archivo `LICENSE` (por ejemplo, MIT o Apache-2.0) y si deseas identificar explícitamente la autoría. El proyecto no incluye una licencia por defecto: esto evita asignar permisos de reutilización sin una decisión expresa.

No publiques datos privados de estudiantes ni capturas con información personal en un repositorio público. Los notebooks contienen ejemplos matemáticos, no tus fotografías o apuntes originales.
