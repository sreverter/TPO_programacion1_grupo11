import random
from iniciacion_listas import *
from funciones.funciones_globales import *


# Función para generar IDs de usuarios aleatoriamente 
def id_user():
    # n=random.randint(1000,9999)
    # while n in id_usuarios:
    #     n=random.randint(1000,9999)       
    # id_usuarios.append(n)
    # return n
    datos_usuarios = cargar_datos_json('datos/datos_usuarios.json')
    
    # Si el archivo está vacío, empezamos desde 1
    if not datos_usuarios:
        return 1
    
    # Buscar el valor más alto en la primera columna (ID)
    mayor_id = 0
    for usuario in datos_usuarios:
        if usuario["id"] > mayor_id:
            mayor_id = usuario["id"]
    mayor_id += 1
    return mayor_id

# creacion de dnis aleatoriamente
def dni_user():
    dni = random.randint(16000000, 90000000)
    while dni in dni_usuarios:
        dni = random.randint(16000000, 90000000)
    dni_usuarios.append(dni)
    return dni

# Crear una lista la cual incluye informacion como el id del usuario nombre dni telefono correo y estado(activo o inactivo)
while len(datos_globales_usuarios) != 400:
    id_usuario = id_user()
    nombre = random.choice(nombres).ljust(10, " ")
    dni=dni_user()
    telefono = random.randint(1100000000, 1199999999)
    correo = (nombre + random.choice(["@gmail.com","@hotmail.com","@yahoo.com"])).replace(" ", "")
    while len(correo) < 25:
        correo += " "
    estado = random.choice([True, False])

    datos_globales_usuarios.append([id_usuario, nombre, dni, telefono, correo, estado])

# Guardar solo IDs y DNIs de usuarios activos
for i in datos_globales_usuarios:
    if i[5] == True:
        ids_usuario.append(i[0])

for i in datos_globales_usuarios:
    dni_usuarios.append(i[2])

# Función para mostrar matriz de usuarios
def ver_busqueda_usuarios(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    
    print("\033[32m" + "-"*91 + "\033[0m")
    print(f"\033[36m{'ID':<8}\033[0m  \033[35m{'Nombre':<13}\033[0m  \033[32m{'DNI':>10}  {'Telefono':>14}\033[0m  \033[34m{'Mail':>14}\033[0m  \033[32m{'Estado':>22}\033[0m")
    print("\033[32m" + "-"*91 + "\033[0m")
    
    for f in range(filas):
        if matriz[f][5] == True:
            estado = "ACTIVO"
            color_estado = "\033[32m"   
        else:
            estado = "INACTIVO"
            color_estado = "\033[91m" 

        print(f"\033[36m{matriz[f][0]:<8}\033[0m  \033[35m{matriz[f][1]:<13}\033[0m  \033[32m{matriz[f][2]:>10}  {matriz[f][3]:>14}\033[0m  \033[34m{matriz[f][4]:>14}\033[0m  {color_estado}{estado:>12}\033[0m")

def ver_m3(matriz):

    filas = len(matriz)
    columnas = len(matriz[0])

    inicio_Cont=int(input(f"\033[35mDesde que reserva deseas empezar: \033[0m"))
    while inicio_Cont < 0 or inicio_Cont >= filas:
        print(f"\033[91mNúmero fuera de rango, solo hay {filas-1} reservas. Seleccione dentro de ese rango\033[0m")
        inicio_Cont=int(input(f"\033[35mDesde que reserva deseas empezar: \033[0m"))
    
    vision=int(input("\033[96mCuántos registros desde el inicio desea ver: \033[0m"))
    while vision < 1 or vision > (filas - inicio_Cont):
        print(f"Debe ser entre 1 y {filas - inicio_Cont}")
        vision = int(input("\033[96mCuántos registros desde el inicio deseas ver: \033[0m"))

    columnas_t = ["ID","Nombre     ","DNI    ","        Telefono","Mail","                                Estado"]

    fin=inicio_Cont+vision
    print("\033[32m" + "-"*91 + "\033[0m")
    print(f"\033[36m{'ID':<8}\033[0m  \033[35m{'Nombre':<13}\033[0m  \033[32m{'DNI':>10}  {'Telefono':>14}\033[0m  \033[34m{'Mail':>14}\033[0m  \033[32m{'Estado':>22}\033[0m")
    print("\033[32m" + "-"*91 + "\033[0m")
    for f in range(inicio_Cont, fin):
        if matriz[f][5] == True:
            estado = "ACTIVO"
            color_estado = "\033[32m"   
        else:
            estado = "INACTIVO"
            color_estado = "\033[91m" 

        print(f"\033[36m{matriz[f][0]:<8}\033[0m  \033[35m{matriz[f][1]:<13}\033[0m  \033[32m{matriz[f][2]:>10}  {matriz[f][3]:>14}\033[0m  \033[34m{matriz[f][4]:>14}\033[0m  {color_estado}{estado:>12}\033[0m")