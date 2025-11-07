from funciones.funciones_globales import *
import re


# Función para generar IDs de usuarios aleatoriamente 
def id_user():

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

def cambio_nombre_usuario():
    while True:
        try:
            nombre_nuevo=str(input("ingrese el nombre que desea de usuario"))
            return nombre_nuevo
        except (ValueError,KeyboardInterrupt):
            print("no se acepta el caracter que intento colocar")
            continue

def cambio_dni_usuario():
    datos_usuarios = cargar_datos_json('datos/datos_usuarios.json')
    while True:
        try:
            dni_nuevo = int(input("\033[36m Escriba el dni por el que desea cambiar: \033[0m"))
            existe_dni = checkear_dato_repetido(datos_usuarios, dni_nuevo, "dni")
            if dni_nuevo <= 0:
                print("no se permiten dnis menores o iguales a 0")
                continue
            if existe_dni:
                print("\033[91m Este DNI ya está registrado. Intente con otro.\033[0m")
                continue
            return dni_nuevo
        except ValueError:
            print("no se admite otra cosa que no sean numeros enteros")

def cambio_telefono_usuario():
    while True:
        try:
            telefono_nuevo = int(input("\033[36mIngrese el numero de telefono por el que desea cambiar: \033[0m"))
            if telefono_nuevo > 1100000000 and telefono_nuevo < 1199999999:
                return telefono_nuevo
            else:
                print("\033[91mEl número debe estar entre 1100000000 y 1199999999.\033[0m")
        except (ValueError,KeyboardInterrupt):
            print("\033[91mError: solo se admiten números.\033[0m")

def cambio_email_usuario():
    while True:
        try:
            #el usuario escribe su email 
            email = input("\033[36m Escriba su nuevo email: \033[0m")
            
            #validaciones basicas de email
            arroba = re.findall('@', email)
            punto  = re.findall(r'\.', email)   

            if len(arroba) !=0 and len(punto) != 0:
                return email
                
            else: 
                print("\033[91m Email inválido, debe contener '@' y '.' \033[0m")
        except(KeyboardInterrupt, ValueError):
            print("ponga caracteres validos")
            continue
