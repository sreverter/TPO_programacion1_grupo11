from funciones.funciones_globales import *
from ingreso import dni_en_uso
from functools import reduce

ruta_archivo = "datos/datos_reservas.txt"

def id_alt_r():
    ids = set()

    try:
        with open("datos/datos_reservas.txt", "rt", encoding="utf-8") as archivo:
            # for linea in archivo:
            linea = archivo.readline()
            while linea:
                datos = linea.strip().split(",")

                if not datos or not datos[0].isdigit():
                    continue
                ids.add(int(datos[0]))
                linea = archivo.readline()
                
    except FileNotFoundError:
        return 1

    if not ids:
        return 1

    # buscar el primer número faltante
    i = 1
    while i in ids:
        i += 1

    return i

def obt_id_Actual():
    dni_act = (dni_en_uso[0])
    user_act = []
    datos_usuario = cargar_datos_json('datos/datos_usuarios.json')
    for i in datos_usuario:
        if i["dni"] == dni_act:
            user_act.append(i["id"])
    return user_act[0]

def buscar_show(id_show):
    datos_shows = cargar_datos_json("datos/datos_shows.json")
    for s in datos_shows:
        if int(s['id-show']) == int(id_show):
            return s
    return 0

def calcular_precio(show, ubicacion, cantidad):
    base = int(show['precio'])
    multiplicador = {
        'platea': 1,
        'campo': 2,
        'vip': 3
    }.get(ubicacion, 1)
    entradas = [base * multiplicador] * cantidad
    total = reduce(lambda acc, x: acc + x, entradas, 0)
    return total

def actualizar_datos_borrado(id_show_list, datos_shows):
    for show_id, cantidad in id_show_list:
        for show in datos_shows:
            if show["id-show"] == show_id:
                show["espacios-disponibles"] += cantidad
                show["espectadores"] -= cantidad
    print("\033[34mLos datos de capacidad fueron actualizados\033[0m")
    inicializar_datos_json('datos/datos_shows.json', datos_shows)

def borrado_reserva_menu():
    while True:
        try:
            opcion = int(input("\n\033[36m¿Qué desea hacer?\033[0m\n"
                                "\033[36m1 - Borrar una sola reserva\033[0m\n"
                                "\033[36m2 - Borrar todas las reservas\033[0m\n"
                                "\033[36mSeleccione una opción:\033[0m "))
            if opcion in (1, 2):
                return opcion
            else:
                print("\033[91mDebe ser un número entre 1 y 2\033[0m")
        except ValueError:
            print("error de tipeo.")
            return
        except KeyboardInterrupt:
            print("Edición cancelada.")
            return