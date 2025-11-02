from iniciacion_listas import *
from entidades.usuarios import id_user
from funciones.funciones_globales import cargar_datos_json
import re

#busqueda por dni y contraseña para revisar que esten en los datos globales de contraseña
def busqueda(dni, contraseña):
    datos_usuarios = "datos/datos_usuarios.json"
    datos_usuarios=cargar_datos_json(datos_usuarios)
    for i in range(len(datos_usuarios)):
        if datos_usuarios[i]["dni"] == dni and datos_usuarios[i]["contraseña"] == contraseña:
            return True
    return False

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
        except(ValueError,KeyboardInterrupt):
            print("\033[91mporfavor ingrese caracteres numericos validos\033[0m")
#parte de ingreso con contraseña y dni

def login():
    #carga de datos de usuarios
    datos_usuarios = "datos/datos_usuarios.json"
    datos_usuarios=cargar_datos_json(datos_usuarios)
    #ingreso de dni
    while True:
        try:
            dni_ingres=int(input("\033[36m Escriba su dni para verificacion: \033[0m"))
            break
        except (ValueError,KeyboardInterrupt):
            print("\033[91mporfavor caracteres numericos validos\033[0m")
            continue
    #revision del ingreso
    datos_usuarios_dni = []
    for usuario in datos_usuarios:
        datos_usuarios_dni.append(usuario["dni"])
    while dni_ingres not in datos_usuarios_dni and dni_ingres not in dni_admins:
        print("\033[91m Id no encontrado revise que este bien su dni.\033[0m")
        try:
            dni_ingres=int(input("\033[36m Escriba su dni para verificacion: \033[0m"))
        except (ValueError,KeyboardInterrupt):
            print("\033[91mporfavor caracteres numericos validos\033[0m")
            continue
    print()
    #ingreso de contraseña
    while True:
        try:
            contraseña=input("\033[36m Escriba su contraseña de usuario: \033[0m")
            break
        except(ValueError, KeyboardInterrupt):
            print("\033[91mingrese caracteres que sean validos\033[0m")
            continue
    datos_usuarios_password = []
    for usuario in datos_usuarios:
        datos_usuarios_password.append(usuario["contraseña"])
    while contraseña not in datos_usuarios_password and contraseña not in contraseñas_admin:
        print("\033[91m contraseña no encontrado revise que este bien su contraseña.\033[0m")
        try:
            contraseña=input("\033[36m Escriba su contraseña de usuario: \033[0m")
            if contraseña in datos_usuarios_password or contraseña in contraseñas_admin:
                break
        except(ValueError, KeyboardInterrupt):
            print("\033[91mingrese caracteres que sean validos\033[0m")
            continue
    print()

    #revision de ambos al mismo tiempo
    while not (
        (dni_ingres in datos_usuarios_dni and contraseña in datos_usuarios_password) or
        (dni_ingres in dni_admins and contraseña in contraseñas_admin)
    ):
        #menu de reintento en caso de que no sean correctos alguno de ellos o no coincidan
        print("\033[91m DNI o contraseña incorrectos \033[0m")
        while True:
            try:
                vuelta = int(input(
                    "\n\033[92m=== MENÚ DE REINTENTO ===\033[0m\n"
                    f"\033[35m  → [0] Volver al menú de ingreso\033[0m\n"
                    "\033[35m  → [1] Reingresar el Dni\033[0m\n"
                    "\033[35m  → [2] Reingresar la Contraseña\033[0m\n"
                    "\033[1;35m Seleccione una opción: \033[0m"
                ))
                if vuelta in (0,1,2):
                    break
                else:
                    print("\033[91msolo se premiten numeros del 0 al 2\033[0m")
            except (ValueError, KeyboardInterrupt):
                print("\033[91malgo a salido mal\033[0m")
                continue
        #sale de la funcion y te manda de nuevo al menu de ingreso
        if vuelta==0:
            return 
        
        #modifica el dni al que escriba el usuario
        elif vuelta==1:
            while True:
                try:
                    dni_ingres = int(input("\033[36mEscriba su DNI para verificación: \033[0m"))
                    break
                except (ValueError,KeyboardInterrupt):
                    print("\033[91mDebe ingresar solo números.\033[0m")

        #modificia la contraseña a la que escriba el usuario
        elif vuelta==2:
            while True:
                try:
                    contraseña=(input("\033[36m Escriba su contraseña para verificacion: \033[0m"))
                    break
                except KeyboardInterrupt:
                    print("\033[91mpor favor ingrese su contraseña\033[0m")
    

    
    #busca que las contraseñas de admin y el dni del admin esten en sus listas respectivas
    if contraseña in contraseñas_admin and dni_ingres in dni_admins:
        print("\033[92m Ingreso conseguido como ADMIN.\033[0m")
        return "ADMIN"
    #busca que coincidan el dni con la contraseña
    else :
        usuario_encontrado = busqueda(dni_ingres, contraseña)
        dni_en_uso.clear()
        #agarra el dni que escribio el usuario al iniciar sesion
        dni_en_uso.append(dni_ingres)
        print(dni_en_uso)
        print("\033[32m Ingreso conseguido como USUARIO.\033[0m")
        return "Usuario"

#registro
def registrar():
    #se asigna un id al usuario que se este registrando
    num_usuario = id_user()

    #el usuario escribe el nombre
    nombre = str(input("\033[36m Escriba el nombre que desee usar: \033[0m"))

    #validaciones basicas de dni debido a no poder acceder a una fuente confiable de dnis para comparar 
    while True:
        try:
            dni_cread = int(input("\033[36m Escriba el número de su DNI: \033[0m"))
            if dni_cread <= 0:
                print("no se permiten dnis menores o iguales a 0")
                continue
            elif dni_cread in datos_de_ingreso_dni or dni_cread in dni_admins:
                print("\033[91m Este DNI ya está registrado. Intente con otro.\033[0m")
                continue
            break
        except ValueError:
            print("no se admite otra cosa que no sean enteros")
            continue

    
    #revision de que sea dentro de los parametros asignados con el numero de area
    while True:
        try:
            telefono_cread = int(input("\033[36mIngrese su número de teléfono sin código de área: \033[0m"))
            if telefono_cread > 1100000000 and telefono_cread < 1199999999:
                print("\033[92mNúmero válido.\033[0m")
                break
            else:
                print("\033[91mEl número debe estar entre 1100000000 y 1199999999.\033[0m")
        except ValueError:
            print("\033[91mError: solo se admiten números.\033[0m")

    #convierte el telefono en un string
    telefono_cread=str(telefono_cread)
    
    #se define un patron
    patron= r"(11)(\d{6})(\d{2})"
    
    #se asigna una forma de como queremos mostrarlo
    numero_oculto=r"\1-XXXX-XX\3"
    
    #se substituye por los parametros asignados
    telefono_organizado=re.sub(patron,numero_oculto,telefono_cread)
    
    #el usuario escribe su email 
    email = input("\033[36m Escriba su email: \033[0m")
    
    #validaciones basicas de email
    arroba = re.findall('@', email)
    punto  = re.findall(r'\.', email)   

    if len(arroba) ==0 or len(punto) == 0:
        print("\033[91m Email inválido, debe contener '@' y '.' \033[0m")
        email = input("\033[36m Escriba su email: \033[0m")
    
    #el usuario define su contraseña    
    contraseña = input("\033[36m Escriba la contraseña que desea: \033[0m")

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
    datos_de_ingreso_dni.append(dni_cread)
    datos_globales_contraseñas.append(contraseña)
    datos_globales_usuarios.append([num_usuario, nombre,dni_cread, telefono_cread, email, True])
    
    #se le dice al usuario que se a registrado con exito
    print("\033[1;36m Usuario registrado con éxito. \033[0m")
    print("")


"""
                        with open("datos_usuarios.json","r", encoding="utf-8") as archivo:
                            usuarios = json.load(archivo)
                            for user in usuarios:
                                if user["id"]==id_eliminar:
                                    user["estado"]=False
                            usuarios_eliminar.append(user)
                        with open("datos/datos_usuarios.json", "w", encoding="utf-8") as archivo:
                            json.dump(usuarios_eliminar, archivo, indent=4, ensure_ascii=False)                     

"""


#hacer que cuando te registres aparezca appendeado al archivo json de usuario toda la info de forma ordenada
#esto va a ayudar a resolver parte cambia la w por una a y saca las comparaciones aunque la laectura requiere que el   