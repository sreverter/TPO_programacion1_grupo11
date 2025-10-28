import random
from iniciacion_listas import *
from datetime import datetime, timedelta

# Función para generar IDs de shows aleatoriamente
def id_alt():
    n=random.randint(1000, 9999)
    while n in ids_shows:
        n=random.randint(1000, 9999)
    ids_shows.append(n)
    return n

# Función para generar fechas aleatorias de shows con restricciones desde el 1 del 1 de 2025 hasta el 31 del 12 del 2025 (1 año)
def fecha_alt():
    fecha_inicio = datetime(2025, 1, 1)
    fecha_fin = datetime(2025, 12, 31)
    rango_dias = (fecha_fin - fecha_inicio).days
    dias_random = random.randint(0, rango_dias)
    fecha_aleatoria = fecha_inicio + timedelta(days=dias_random)
    return fecha_aleatoria.date()

# Crear 10 shows aleatorios con (id, tipo, duracion, espectadores, espacios disponibles y fecha del evento)
while len(datos_globales) != 10:
    id_show = id_alt()
    tipo_Evento = random.choice(tipos_show)
    duracion = random.choice([60,120,180])
    espectadores=0
    espacios_disponibles = 999
    fecha = fecha_alt()
    datos_globales.append([id_show, tipo_Evento, duracion, espectadores, espacios_disponibles, fecha])


#creacion de precios 
for i in datos_globales:
        id_show = i[0]

        precio_b = random.randint(7200,12000)
        precio_b2 = precio_b * 2
        precio_b3 = precio_b * 3

        precios_show.append([id_show,precio_b,precio_b2,precio_b3])

# Guardar solo los IDs de los shows
for i in datos_globales:
    solo_ids_show.append(i[0])

# Función para mostrar matriz de shows con colores, espacios y encabezados
def ver_m(matriz):
    filas = len(matriz)
    columnas_t = ["ID's", "Tipo de evento", "Duración", "Cant. Espectadores", "Esp. Disponibles", "Fecha"]

    print("\033[32m" + "-" * 95 + "\033[0m")
    print(f"\033[36m{'IDs':<8}\033[0m  \033[35m{'Tipo de evento':<18}\033[0m  \033[32m{'Duración':>10}\033[0m  \033[34m{'Cant. Espect.':>16}\033[0m  \033[33m{'Esp. Disp.':>14}\033[0m  \033[35m{'Fecha':>12}\033[0m")
    print("\033[32m" + "-" * 95 + "\033[0m")

    for f in range(filas):
        print(f"\033[36m{matriz[f][0]:<8}\033[0m  \033[35m{matriz[f][1]:<18}\033[0m  \033[32m{matriz[f][2]:>10}\033[0m  \033[34m{matriz[f][3]:>16}\033[0m  \033[33m{matriz[f][4]:>14}\033[0m  \033[35m{str(matriz[f][5]):>12}\033[0m")