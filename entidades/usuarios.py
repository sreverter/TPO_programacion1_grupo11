from funciones.funciones_globales import *
import re

def id_user():
    datos_usuarios = cargar_datos_json('datos/datos_usuarios.json')
    if not datos_usuarios:
        return 1
    mayor_id = 0
    for usuario in datos_usuarios:
        if usuario["id"] > mayor_id:
            mayor_id = usuario["id"]
    mayor_id += 1
    return mayor_id

def cambio_nombre_usuario():
    while True:
        try:
            nombre_nuevo = str(input("\033[36mIngrese el nombre que desea de usuario:\033[0m "))
            return nombre_nuevo
        except ValueError:
            print("Nombre inválido.")
            return
        except KeyboardInterrupt:
            print("Edición cancelada.")
            return
def cambio_dni_usuario():
    datos_usuarios = cargar_datos_json('datos/datos_usuarios.json')
    while True:
        try:
            dni_nuevo = int(input("\033[36mEscriba el DNI por el que desea cambiar:\033[0m "))
            existe_dni = checkear_dato_repetido(datos_usuarios, dni_nuevo, "dni")
            if dni_nuevo <= 0:
                print("\033[91mNo se permiten DNIs menores o iguales a 0\033[0m")
                continue
            if existe_dni:
                print("\033[91mEste DNI ya está registrado. Intente con otro.\033[0m")
                continue
            return dni_nuevo
        except ValueError:
            print("dni inválido.")
            continue
        except KeyboardInterrupt:
            print("Edición cancelada.")
            continue
def cambio_telefono_usuario():
    while True:
        try:
            telefono_nuevo = int(input("\033[36mIngrese el numero de telefono por el que desea cambiar: \033[0m"))
            if telefono_nuevo > 1100000000 and telefono_nuevo < 1199999999:
                return telefono_nuevo
            else:
                print("\033[91mEl número debe estar entre 1100000000 y 1199999999\033[0m")
        except ValueError:
            print("telefono inválido.")
            continue
        except KeyboardInterrupt:
            print("Edición cancelada.")
            continue

def cambio_email_usuario():
    while True:
        try:
            email = input("\033[36mEscriba su nuevo email:\033[0m ")
            arroba = re.findall('@', email)
            punto = re.findall(r'\.', email)
            if len(arroba) != 0 and len(punto) != 0:
                return email
            else:
                print("\033[91mEmail inválido, debe contener '@' y '.'\033[0m")
        except ValueError:
            print("email inválido.")
            continue
        except KeyboardInterrupt:
            print("Edición cancelada.")
            continue