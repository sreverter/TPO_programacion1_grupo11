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
            if not nombre_nuevo:
                print("\033[91mEl nombre no puede estar vacío.\033[0m")
                continue
            return nombre_nuevo
        except (ValueError):
            print("\033[91mNo se acepta el carácter que intentó colocar\033[0m")
            continue
        except (KeyboardInterrupt, EOFError):
            print("\n\033[93mCambio de nombre cancelado.\033[0m")
            return None 

def cambio_dni_usuario():
    datos_usuarios = cargar_datos_json('datos/datos_usuarios.json')
    while True:
        try:
            dni_nuevo = int(input("\033[36mEscriba el DNI por el que desea cambiar:\033[0m "))
            if dni_nuevo <= 0:
                print("\033[91mNo se permiten DNIs menores o iguales a 0\033[0m")
                continue
            existe_dni = checkear_dato_repetido(datos_usuarios, dni_nuevo, "dni")
            if existe_dni:
                print("\033[91mEste DNI ya está registrado. Intente con otro.\033[0m")
                continue
            return dni_nuevo
        except ValueError:
            print("\033[91mNo se admite otra cosa que no sean números enteros\033[0m")
        except (KeyboardInterrupt, EOFError):
            print("\n\033[93mCambio de DNI cancelado.\033[0m")
            return None 
        
def cambio_telefono_usuario():
    while True:
        try:
            telefono_nuevo = int(input("\033[36mIngrese el numero de telefono por el que desea cambiar: \033[0m"))
            if telefono_nuevo > 1100000000 and telefono_nuevo < 1199999999:
                return telefono_nuevo
            else:
                print("\033[91mEl número debe estar entre 1100000000 y 1199999999\033[0m")
        except ValueError:
            print("\033[91mError: solo se admiten números\033[0m")
        except (KeyboardInterrupt, EOFError):
            print("\n\033[93mCambio de teléfono cancelado.\033[0m")
            return None 

def cambio_email_usuario():
    datos_usuarios = cargar_datos_json('datos/datos_usuarios.json')
    while True:
        try:
            email = input("\033[36mEscriba su nuevo email:\033[0m ")

            if checkear_dato_repetido(datos_usuarios, email, "correo"):
                print("\033[91mEste correo ya está en uso por otro usuario.\033[0m")
                continue

            arroba = re.findall('@', email)
            punto = re.findall(r'\.', email)
            if len(arroba) != 0 and len(punto) != 0:
                return email
            else:
                print("\033[91mEmail inválido, debe contener '@' y '.'\033[0m")
        
        except ValueError:
             print("\033[91mCarácter inválido.\033[0m")
        except (KeyboardInterrupt, EOFError):
            print("\n\033[93mCambio de email cancelado.\033[0m")
            return None 
