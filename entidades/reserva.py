import random
from iniciacion_listas import datos_globales_reserva,ubicacion, ids_usuario, ids_reserva, datos_globales, shows_con_capacidad,precios_show
from entidades.shows import solo_ids_show

# Función para generar IDs de reserva en forma aleatoria
def id_alt_r():
    n=random.randint(1000,19999)
    while n in ids_reserva:
        n = random.randint(1000, 19999)
    ids_reserva.append(n)
    return n

# revisa los shows para ver la capacidad que tienen y asigna  a los usuarios aleatorios a uno de ellos en caso de que no haya ninguno
# hace un print diciendo que no hay capacidad
def shows_seleccion():
    shows_con_capacidad = []
    for i in datos_globales:
        if i[4] > 0:  
            shows_con_capacidad.append(i[0])
    if not shows_con_capacidad:
        return None
    
    show_elegido = random.choice(shows_con_capacidad)
    
    for i in datos_globales:
        if i[0] == show_elegido:
            i[3] += 1 
            i[4] -= 1  
    
    return show_elegido
#dependiendo de la ubicacion dada marca un precio
def precio_ubi(ubicacion):
    if ubicacion == "platea":
        for i in precios_show:
            if i[0] == show:
                precio = i[1]
                return precio 
            
    elif ubicacion == "campo":
        for i in precios_show:
            if i[0] == show:
                    precio = i[2]
                    return precio 

    elif ubicacion == "vip":
        for i in precios_show:
            if i[0] == show:
                    precio = i[3]
                    return precio 

# Crear reservas aleatorias con el id de la reserva, el del usuario, la ubicacion y el precio de la reserva
while len(datos_globales_reserva) < 4000:
    id_reserva = id_alt_r()
    #id_usuario = random.choice(ids_usuario)
    id_usuario = 1
    ubicacion_u = random.choice(ubicacion)
    show=shows_seleccion()
    if show ==None:
        print("No hay mas shows con capacidad disponibles.")
    precio=precio_ubi(ubicacion_u)

    datos_globales_reserva.append([id_reserva, id_usuario, ubicacion_u, show, precio])

#funcion para buscar reservas mostrando las del usuario que hizo esas reservas
def ver_busqueda_reserva(matriz):

    filas=len(matriz)

    print(f"\033[32m{'-'*73}\033[0m")
    print(f"\033[32m{'IDs':<8}  {'ID Usuario':<13}\033  \033[35m{'Ubicación':>10}  {'ID Show':>12}\033[0m  \033[34m{'Precio':>14}\033[0m")
    print(f"\033[32m{'-'*73}\033[0m")
    for f in range(filas):
        print(f"\033[32m{matriz[f][0]:<8}  {matriz[f][1]:<13}\033[35m  {matriz[f][2]:>10}  {matriz[f][3]:>10}\033[0m  \033[34m{matriz[f][4]:>14}\033[0m")

# Función para mostrar reservas con sistema de filtrado por cantidad
def ver_m2(matriz):

    filas=len(matriz)
    inicio_Cont=int(input(f"\033[35mDesde que reserva deseas empezar: \033[0m"))
    while inicio_Cont < 0 or inicio_Cont >= filas:
        print(f"\033[91mNúmero fuera de rango, solo hay {filas-1} reservas. Seleccione dentro de ese rango\033[0m")
        inicio_Cont=int(input(f"Desde que reserva deseas empezar: "))
    
    vision=int(input("\033[35mCuántos registros desde el inicio desea ver: \033[0m"))
    while vision < 1 or vision > (filas - inicio_Cont):
        print(f"\033[91m Debe ser entre 1 y {filas - inicio_Cont}\033[0m")
        vision = int(input("\033[35mCuántos registros desde el inicio deseas ver: \033[0m"))

    fin= inicio_Cont+vision

    print(f"\033[32m{'-'*73}\033[0m")
    print(f"\033[32m{'IDs':<8}  {'ID Usuario':<13}\033  \033[35m{'Ubicación':>10}  {'ID Show':>12}\033[0m  \033[34m{'Precio':>14}\033[0m")
    print(f"\033[32m{'-'*73}\033[0m")

    for f in range(inicio_Cont, fin):
        print(f"\033[32m{matriz[f][0]:<8}  {matriz[f][1]:<13}\033[35m  {matriz[f][2]:>10}  {matriz[f][3]:>10}\033[0m  \033[34m{matriz[f][4]:>14}\033[0m")