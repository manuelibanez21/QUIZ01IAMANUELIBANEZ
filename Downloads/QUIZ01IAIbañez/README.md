\# QUIZIAManuelibañez



Este proyecto implementa un \*\*Algoritmo Genético (GA)\*\* en Python, enfocado en la solución de un problema de optimización de rutas.

El código incluye los pasos fundamentales de un GA: creación de población inicial, selección, cruce, mutación y visualización de resultados.



---



\## 📌 Contenido del repositorio



\* `QUIZIAManuelibañez.py` → Script principal que contiene toda la implementación del algoritmo genético.

\* `README.md` → Documento explicativo del funcionamiento del código y cómo ejecutarlo.



---



\## ⚙️ Funcionamiento del código



\### 1. \*\*Población inicial\*\*



\* Se generan varias soluciones candidatas (\*\*rutas\*\*) de manera \*\*aleatoria\*\*.

\* Cada ruta es una permutación de los puntos definidos en el espacio.



\### 2. \*\*Evaluación de aptitud (Fitness)\*\*



\* Se calcula la distancia total de cada ruta.

\* Cuanto menor sea la distancia, \*\*mejor es la solución\*\*.



\### 3. \*\*Selección\*\*



\* Se eligen las mejores rutas de acuerdo a su aptitud.

\* El método utilizado puede ser por ranking o probabilidad proporcional a la calidad.



\### 4. \*\*Cruce (Crossover)\*\*



\* Se combinan dos rutas para generar nuevas soluciones.

\* La idea es heredar características de los padres y producir rutas más cortas.



\### 5. \*\*Mutación\*\*



\* Con una probabilidad baja, se alteran algunos elementos de la ruta.

\* Esto introduce diversidad en la población y evita la convergencia prematura.



\### 6. \*\*Visualización de rutas\*\*



\* Se muestran \*\*dos gráficos\*\*:



&nbsp; 1. Una ruta inicial (aleatoria).

&nbsp; 2. La mejor ruta encontrada después de las generaciones.



---



\## 🚀 Ejecución



\### Requisitos:



\* Python 3.x

\* Librerías necesarias:



&nbsp; ```bash

&nbsp; pip install matplotlib numpy

&nbsp; ```



\### Para ejecutar:



```bash

python QUIZIAManuelibañez.py

```



Esto mostrará en pantalla dos figuras con las rutas generadas y optimizadas.



---



\## 📊 Resultados esperados



\* Una primera figura con una ruta aleatoria (población inicial).

\* Una segunda figura con la mejor ruta optimizada mediante el algoritmo genético.



---



\## 👤 Autor



\*\*Manuel Ibáñez\*\*

Proyecto de Inteligencia Artificial — Quiz 01



