from funciones.funciones_globales import *
from iniciacion_listas import dni_en_uso
from functools import reduce

# Función para generar IDs de reserva en forma aleatoria
def id_alt_r():
    datos_reservas = cargar_datos_txt('datos/datos_reservas.txt')
    
    # Si el archivo está vacío, empezamos desde 1
    if not datos_reservas:
        return 1
    
    # Buscar el valor más alto en la primera columna (ID)
    mayor_id = 0
    for reserva in datos_reservas:
        if reserva[0] > mayor_id:
            mayor_id = reserva[0]
    mayor_id+=1
    return mayor_id

#se agarra el id del usuario comparandolo con el dni que esta en uso
def obt_id_Actual():
    #se agarra el dni en uso y se pone en otra variable
    dni_act = (dni_en_uso[0])
    #se crea una lista que es donde va a ir el usuario de ese dni
    user_act = []
    #se añade el id de ese usuario
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

    # Determinar el multiplicador según la ubicación
    multiplicador = {
        'platea': 1,
        'campo': 2,
        'vip': 3
    }.get(ubicacion, 1)

    # Creamos una lista con el precio de cada entrada
    entradas = [base * multiplicador] * cantidad

    # Usamos reduce para sumar todos los precios
    total = reduce(lambda acc, x: acc + x, entradas, 0)

    return total

def actualizar_datos_borrado(id_show_list, datos_reservas, datos_shows):

    # Actualizar la capacidad en los shows
    for show_id, cantidad in id_show_list:
        for show in datos_shows:
            if show["id-show"] == show_id:
                show["espacios-disponibles"] += cantidad
                show["espectadores"] -= cantidad

    # Mensaje informativo
    print("\033[34mLos datos de capacidad fueron actualizados\033[0m")

    # Guardar cambios
    inicializar_datos_txt('datos/datos_reservas.txt', datos_reservas)
    inicializar_datos_json('datos/datos_shows.json', datos_shows)

def borrado_reserva_menu():
    while True:
        try:
            opcion = int(input("\n\033[35m¿Qué desea hacer?\033[0m\n"
                                "1 - Borrar una sola reserva\n"
                                "2 - Borrar todas las reservas\n"
                                "\033[36mSeleccione una opción: \033[0m"))
            if opcion in (1, 2):
                return opcion
            else:
                print("Debe ser un número entre 1 y 2.")
        except (ValueError, KeyboardInterrupt):
            print("Ingrese un valor válido.")
