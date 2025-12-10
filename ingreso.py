from entidades.usuarios import id_user
from funciones.funciones_globales import *
import re

dni_en_uso = []
#menu para el ingreso de forma coloreada
def menu_login():
# Marco verde brillante
    print("\033[92m╔════════════════════════════╗\033[0m")
    print("\033[92m║\033[0m       \033[93mMENÚ DE INGRESO\033[0m      \033[92m║\033[0m")
    print("\033[92m╠════════════════════════════╣\033[0m")

    # Opciones cyan
    print("\033[92m║\033[0m  \033[96m 0 → Iniciar Sesión\033[0m       \033[92m║\033[0m")
    print("\033[92m║\033[0m  \033[96m 1 → Registrarse\033[0m          \033[92m║\033[0m")

    # Cierre verde
    print("\033[92m╚════════════════════════════╝\033[0m")

    while True:
        try:
            ingreso = int(input(f"\033[1;35m Seleccione una opción: \033[0m"))
            #validacion de opciones
            if ingreso in (0, 1):
                return ingreso
            else:
                print(f"\033[91m Opción inválida, intente de nuevo.\033[0m")
        except ValueError:
            print("Error de tipeo")
            continue
        except (KeyboardInterrupt, EOFError):
            print("Operación cancelada.")
            return

#parte de ingreso con contraseña y dni
def login():
    #carga de datos de usuarios
    # datos_usuarios = "datos/datos_usuarios.json"
    datos_usuarios = cargar_datos_json("datos/datos_usuarios.json")
    #variables de uso interno
    info_usuario = []
    dni_encontrado=False
    contraseña_encontrada=False
    #ingreso de dni
    while True:
        try:
            dni_ingres=int(input("\033[36m Escriba su dni para verificacion: \033[0m"))
            break
        except ValueError:
            print("Error de tipeo")
            continue
        except (KeyboardInterrupt, EOFError):
            print("Operación cancelada.")
            return
    while True:
        for i in datos_usuarios:
            if i["dni"]==dni_ingres:
                info_usuario.append(i)
                dni_encontrado=True
        if dni_encontrado:
            break
        else:
            print("\033[91m DNI no encontrado revise que este bien su escrito.\033[0m")
            try:
                dni_ingres=int(input("\033[36m Escriba su dni para verificacion: si desea volver al menu de ingreso ingrese -1: \033[0m"))
                if dni_ingres==-1:
                    return
            except ValueError:
                print("Error de tipeo")
                continue
            except (KeyboardInterrupt, EOFError):
                print("Operación cancelada.")
                return
    print()
    #ingreso de contraseña
    while True:
        try:
            contraseña=input("\033[36m Escriba su contraseña de usuario: \033[0m")
            break
        except ValueError:
            print("Error de tipeo")
            continue
        except (KeyboardInterrupt, EOFError):
            print("Operación cancelada.")
            return

    while True:
        for i in info_usuario:
            if i["contraseña"]==contraseña:
                contraseña_encontrada=True
        if contraseña_encontrada:
            break
        else:
            print("\033[91m Contraseña incorrecta, intente de nuevo.\033[0m")
            try:
                contraseña=input("\033[36m Escriba su contraseña de usuario: si desea volver al menu de ingreso presione -1: \033[0m")
                if contraseña=="-1":
                    return
            except ValueError:
                print("Error de tipeo")
                continue
            except (KeyboardInterrupt, EOFError):
                print("Operación cancelada.")
                return
    
    for i in info_usuario:
        if i["roles"]=="admin":
            #lista con el dni que esta usando la persona actualmente en el programa
            dni_en_uso.clear()
            #agarra el dni que escribio el usuario al iniciar sesion
            dni_en_uso.append(dni_ingres)
            print("\033[92m Ingreso conseguido como ADMIN.\033[0m")
            return "ADMIN"
        else:
            #lista con el dni que esta usando la persona actualmente en el programa
            dni_en_uso.clear()
            #agarra el dni que escribio el usuario al iniciar sesion
            dni_en_uso.append(dni_ingres)
            print("\033[32m Ingreso conseguido como USUARIO.\033[0m")
            return "Usuario"


#registro
def registrar():
    #se asigna un id al usuario que se este registrando
    num_usuario = id_user()
    datos_usuarios = cargar_datos_json('datos/datos_usuarios.json')

    #el usuario escribe el nombre
    while True:   
        try:
            nombre = str(input("\033[36m Escriba el nombre que desee usar: \033[0m"))
            break
        except ValueError:
            print("Error de tipeo")
            continue
        except (KeyboardInterrupt, EOFError):
            print("Operación cancelada.")
            return
    #validaciones basicas de dni debido a no poder acceder a una fuente confiable de dnis para comparar 
    while True:
        try:
            dni_cread = int(input("\033[36m Escriba el número de su DNI: \033[0m"))
            existe_dni = checkear_dato_repetido(datos_usuarios, dni_cread, "dni")
            if dni_cread <= 0:
                print("no se permiten dnis menores o iguales a 0")
                continue
            if existe_dni:
                print("\033[91m Este DNI ya está registrado. Intente con otro.\033[0m")
                continue
            break
        except ValueError:
            print("Error de tipeo")
            continue
        except (KeyboardInterrupt, EOFError):
            print("Operación cancelada.")
            return


    
    #revision de que sea dentro de los parametros asignados con el numero de area
    while True:
        try:
            telefono_cread = int(input("\033[36mIngrese su número de teléfono sin código de área: \033[0m"))
            if telefono_cread > 1100000000 and telefono_cread < 1199999999:
                break
            else:
                print("\033[91mEl número debe estar entre 1100000000 y 1199999999.\033[0m")
        except ValueError:
            print("Error de tipeo")
            continue
        except (KeyboardInterrupt, EOFError):
            print("Operación cancelada.")
            return

    #convierte el telefono en un string
    telefono_cread=str(telefono_cread)
    
    #se define un patron
    patron= r"(11)(\d{6})(\d{2})"
    
    #se asigna una forma de como queremos mostrarlo
    numero_oculto=r"\1-XXXX-XX\3"
    
    #se substituye por los parametros asignados
    telefono_organizado=re.sub(patron,numero_oculto,telefono_cread)
    
    while True:
        try:
            email = input("\033[36m Escriba su email: \033[0m")
            
            # 1. Validar si existe
            existe_email = checkear_dato_repetido(datos_usuarios, email, "correo")
            if existe_email:
                print("\033[91m Este correo ya está registrado. Intente con otro.\033[0m")
                continue # Vuelve a pedir el input

            # 2. Validar formato
            arroba = re.findall('@', email)
            punto  = re.findall(r'\.', email)

            if len(arroba) == 0 or len(punto) == 0:
                print("\033[91m Email inválido, debe contener '@' y '.' \033[0m")
                continue # Vuelve a pedir el input
            
            # Si pasa todo, salimos
            break

        # Excepciones del input
        except ValueError:
            print("Error de tipeo")
            continue
        except (KeyboardInterrupt, EOFError):
            print("\nOperación cancelada.")
            return
        
    #el usuario define su contraseña    
    while True:   
        try:
            contraseña = input("\033[36m Escriba la contraseña que desea: \033[0m")
            break
        except ValueError:  
            print("Error de tipeo")
            continue
        except (KeyboardInterrupt, EOFError):
            print("Operación cancelada.")
            return


    
    while True:
            try:
                roles = int(input("\033[36m Ingrese 1 si desea ser admin o 2 si desea ser usuario: \033[0m"))
                if roles in (1, 2):
                    break
                else:
                    print("\033[91m Por favor ingrese 1 o 2.\033[0m")
            except ValueError:
                print("\033[91m Debe ingresar un número (1 o 2).\033[0m")
            except (KeyboardInterrupt, EOFError):
                print("\n\033[93m\nEjecución interrumpida por el usuario. Saliendo...\033[0m")
                return
    if roles==1:
        rol_asignado="admin"
    else:
        rol_asignado="usuario"
    

    #se muestra la informacion de una forma mas legible para la lectura del usuario
    print("\033[1;92m Usuario creado con éxito con la siguiente información:\033[0m")
    print(f"\033[92m \n",( "═" * 50),"\033[0m")
    print(f"\033[35m  - ID usuario : {num_usuario}\033[0m")
    print(f"\033[35m  - Nombre     : {nombre}\033[0m")
    print(f"\033[35m  - DNI        : {dni_cread}\033[0m")
    print(f"\033[35m  - Teléfono   : {telefono_organizado}\033[0m")
    print(f"\033[35m  - Email      : {email}\033[0m")
    print("\033[92m",( "═" * 50),"\033[0m")

    #se añaden los datos puestos por el usuario en sus respectivos lugares
    nuevo_usuario = {
        "id": num_usuario,
        "nombre": nombre,
        "dni": dni_cread,
        "telefono": telefono_cread,
        "correo": email,
        "estado": True,
        "contraseña": contraseña,
        "roles": rol_asignado
    }   
    datos_usuarios.append(nuevo_usuario)
    inicializar_datos_json('datos/datos_usuarios.json', datos_usuarios)
    
    #se le dice al usuario que se a registrado con exito
    print("\033[1;36m Usuario registrado con éxito. \033[0m")
    print("")
