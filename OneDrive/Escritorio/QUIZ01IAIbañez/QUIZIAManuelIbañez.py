import random
import math
import matplotlib.pyplot as plt

# Definición de ciudades
ciudades = {
    'A': (0, 0),
    'B': (1, 5),
    'C': (2, 3),
    'D': (5, 2),
    'E': (6, 6),
    'F': (7, 1),
    'G': (8, 4),
    'H': (9, 9)
}

# ------------------------------
# Calcular distancia de una ruta
# ------------------------------
def distancia_ruta(ruta):
    distancia = 0
    for i in range(len(ruta)):
        ciudad_actual = ciudades[ruta[i]]
        ciudad_siguiente = ciudades[ruta[(i + 1) % len(ruta)]]
        distancia += math.dist(ciudad_actual, ciudad_siguiente)
    return distancia

# ------------------------------
# Crear población inicial (aleatoria)
# ------------------------------
def crear_poblacion_inicial(tam_poblacion):
    poblacion = []
    ciudades_lista = list(ciudades.keys())
    for _ in range(tam_poblacion):
        ruta = ciudades_lista[:]
        random.shuffle(ruta)  # aleatoria cada vez
        poblacion.append(ruta)
    return poblacion

# ------------------------------
# Selección por ruleta
# ------------------------------
def seleccion(poblacion, distancias):
    fitness = [1 / d for d in distancias]
    total_fitness = sum(fitness)
    probabilidades = [f / total_fitness for f in fitness]
    return poblacion[random.choices(range(len(poblacion)), probabilidades)[0]]

# ------------------------------
# Cruce OX
# ------------------------------
def cruce(padre1, padre2):
    size = len(padre1)
    inicio, fin = sorted(random.sample(range(size), 2))
    
    hijo = [None] * size
    hijo[inicio:fin] = padre1[inicio:fin]
    
    pos = fin
    for ciudad in padre2:
        if ciudad not in hijo:
            if pos >= size:
                pos = 0
            hijo[pos] = ciudad
            pos += 1
    return hijo

# ------------------------------
# Mutación por intercambio
# ------------------------------
def mutacion(ruta, tasa_mutacion):
    for i in range(len(ruta)):
        if random.random() < tasa_mutacion:
            j = random.randint(0, len(ruta) - 1)
            ruta[i], ruta[j] = ruta[j], ruta[i]
    return ruta

# ------------------------------
# Algoritmo genético principal
# ------------------------------
def algoritmo_genetico(tam_poblacion=50, generaciones=200, tasa_mutacion=0.05):
    poblacion = crear_poblacion_inicial(tam_poblacion)

    mejor_ruta = None
    mejor_distancia = float('inf')
    historial = []

    for _ in range(generaciones):
        distancias = [distancia_ruta(ruta) for ruta in poblacion]

        for i in range(len(poblacion)):
            if distancias[i] < mejor_distancia:
                mejor_ruta = poblacion[i]
                mejor_distancia = distancias[i]

        historial.append(mejor_distancia)

        nueva_poblacion = []
        for _ in range(tam_poblacion // 2):
            padre1 = seleccion(poblacion, distancias)
            padre2 = seleccion(poblacion, distancias)
            hijo1 = cruce(padre1, padre2)
            hijo2 = cruce(padre2, padre1)
            nueva_poblacion.append(mutacion(hijo1, tasa_mutacion))
            nueva_poblacion.append(mutacion(hijo2, tasa_mutacion))

        poblacion = nueva_poblacion

    return mejor_ruta, mejor_distancia, historial

# ------------------------------
# Graficar mejor ruta
# ------------------------------
def graficar_ruta(ruta, titulo="Mejor Ruta"):
    x = [ciudades[ciudad][0] for ciudad in ruta] + [ciudades[ruta[0]][0]]
    y = [ciudades[ciudad][1] for ciudad in ruta] + [ciudades[ruta[0]][1]]

    plt.figure(figsize=(6,6))
    plt.plot(x, y, marker='o', linestyle='-', color="b")
    for ciudad in ruta:
        plt.text(ciudades[ciudad][0], ciudades[ciudad][1], ciudad, fontsize=12, color="red")
    plt.title(titulo)

# ------------------------------
# Ejecutar
# ------------------------------
mejor_ruta, mejor_distancia, historial = algoritmo_genetico()

print("Mejor ruta encontrada:", mejor_ruta)
print("Distancia total:", mejor_distancia)

# Mostrar ambas gráficas
graficar_ruta(mejor_ruta, "Ruta óptima encontrada")
plt.figure()
plt.plot(historial, color="green")
plt.title("Evolución de la distancia mínima")
plt.xlabel("Generaciones")
plt.ylabel("Distancia")

plt.show()
