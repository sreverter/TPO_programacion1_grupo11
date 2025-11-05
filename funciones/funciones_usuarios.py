from datos import datos_usuarios
from iniciacion_listas import dni_en_uso,datos_de_ingreso_dni
from funciones.funciones_reservas import obt_id_Actual
from funciones.funciones_globales import *
import re
datos_usuarios_js="datos/datos_usuarios.json"
datos_reserva_txt="datos/datos_reservas.txt"

def cambio_nombre_usuario():
    while True:
        try:
            nombre_nuevo=str(input("ingrese el nombre que desea de usuario"))
            return nombre_nuevo
        except (ValueError,KeyboardInterrupt):
            print("no se acepta el caracter que intento colocar")
            continue

def cambio_dni_usuario():
    while True:
        try:
            dni_nuevo = int(input("\033[36m Escriba el dni por el que desea cambiar: \033[0m"))
            if dni_nuevo <= 0:
                print("no se permiten dnis menores o iguales a 0")
                continue
            if dni_nuevo not in datos_de_ingreso_dni:
                return dni_nuevo
            else:
                print("\033[91m El DNI por el cual pide cambiar esta siendo usado, intente de nuevo.\033[0m")
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

def vista_Usuarios(admin):
        datos_usuarios=cargar_datos_json(datos_usuarios_js)
        if admin: 
            while True:
                try:
                    eleccion = int(input("\033[96m1-VER TODOS LOS USUARIOS\n2-BUSCAR USUARIO POR ID:\033[0m"))
                    if eleccion in (1,2):
                        break
                    else:
                        print("el numero no esta dentro de los parametros dados")
                except(ValueError,KeyboardInterrupt):
                    print("el caracter usado no es uno valido para esta region")
                    continue
            if eleccion == 1:
                filtro_usuarios= int(input("Ingrese el estado de los usuarios a mostrar (1- Activo, 2- Inactivo, 3- Todos): "))
                # Usamos filter() según la elección
                if filtro_usuarios == 1:
                    usuarios_filtrados = list(filter(lambda x: x["estado"] is True, datos_usuarios))
                    print("\n\033[92m=== USUARIOS ACTIVOS ===\033[0m")
                elif filtro_usuarios == 2:
                    usuarios_filtrados = list(filter(lambda x: x["estado"] is False, datos_usuarios))
                    print("\n\033[91m=== USUARIOS INACTIVOS ===\033[0m")
                elif filtro_usuarios == 3:
                    usuarios_filtrados = datos_usuarios
                    print("\n\033[94m=== TODOS LOS USUARIOS ===\033[0m")

                # Si hay resultados, mostramos la tabla o lista
                if usuarios_filtrados:
                    mostrar_tabla(usuarios_filtrados, 2)  
                else:
                    print("No hay usuarios con ese estado.")
        elif admin == False:
            id = obt_id_Actual()
            for user in datos_usuarios:
                if user['id']==id:
                    print(user['id'],user['nombre'],user['dni'],user['telefono'],user['correo'],user['estado'])



"""def vista_Usuarios(admin):
        datos_usuarios=cargar_datos_json(datos_usuarios_js)
        if admin: 
            while True:
                try:
                    eleccion = int(input("\033[96m1-VER TODOS LOS USUARIOS\n2-BUSCAR USUARIO POR ID:\033[0m"))
                    if eleccion in (1,2):
                        break
                    else:
                        print("el numero no esta dentro de los parametros dados")
                except(ValueError,KeyboardInterrupt):
                    print("el caracter usado no es uno valido para esta region")
                    continue

            if eleccion == 1:
                mostrar_tabla(datos_usuarios,2)
                #imprime raro falta un imprmir lindo 
            elif eleccion == 2:
                while True:
                    try:
                        eleccion = int(input("Ingrese ID a buscar: "))
                        break
                    except(ValueError,KeyboardInterrupt):
                        print("el caracter usado no es uno valido para esta region")
                        continue
                encontrado=False
                for user in datos_usuarios:
                    if user["id"]==eleccion:
                        encontrado=True
                        print(user['id'],user['nombre'],user['dni'],user['telefono'],user['correo'],user['estado'])
                        #imprime raro falta un imprmir lindo
                if not encontrado:
                    print("no se a entcontrado el id del usuario")"""

        

def edicion_usuario(admin):
    usuarios=cargar_datos_json(datos_usuarios_js)
    if admin:
        encontrado=False
        while True:
            try:
                eleccion = int(input("Seleccione el id de usuario a editar: "))
            except (ValueError, KeyboardInterrupt):
                print("ponga caracteres válidos")
                continue
            try:
                
                for user in usuarios:
                    if user['id'] == eleccion:
                        encontrado=True
                if encontrado:
                    break
                elif encontrado==False:
                    print("no se encontro el usuario que esta buscando")
                    continue
                        
            except (OSError,FileNotFoundError):
                print("no se pudo abrir o no se encontro el archivo")

        while True:
            try:
                opcion = int(input(
                "\n\033[92m=== MENU DE EDICIÓN ===\033[0m\n"
                "\033[35m  → [0] Editar nombre\033[0m\n"
                "\033[35m  → [1] Editar DNI \033[0m\n"
                "\033[35m  → [2] Editar telefono\033[0m\n"
                "\033[35m  → [3] Editar correo\033[0m\n"
                "\033[35m  → [4] Editar estado a Inactivo\033[0m\n"
                "\033[35m  → [5] Editar estado a activo\033[0m\n"
                "\033[1;35m Seleccione una opción: \033[0m"
                ))
                if opcion in (0,1,2,3,4,5):
                    break
                else:
                    print("el numero que ha puesto no es ninguno de los mencionados")
                    continue
            except(KeyboardInterrupt,ValueError):
                print("ponga caracteres validos")
                continue

        usuarios_actualizados = []
        for user in usuarios:
            if user["id"] == eleccion:
                if opcion==0:
                    user['nombre']=cambio_nombre_usuario() 
                elif opcion==1:
                    user['dni']=cambio_dni_usuario()
                elif opcion==2:
                    user['telefono']=cambio_telefono_usuario()                            
                elif opcion==3:
                    user['correo']=cambio_email_usuario()
                elif opcion==4:
                    user['estado']=False
                elif opcion==5:
                    user['estado']=True
                
            usuarios_actualizados.append(user)

        inicializar_datos_json(datos_usuarios_js,usuarios_actualizados)

        print("el usuario a sido editado con exito")

    elif admin==False:  # EDITAR USUARIO SIENDO USUARIO
        for i in usuarios:
            if i["dni"] == dni_en_uso[0]:
                print("\033[96mSe ha accedido a su perfil\033[0m")
                while True:
                    try:
                        opcion = int(input(
                            "\n\033[92m=== MENÚ DE EDICIÓN ===\033[0m\n"
                            "\033[35m  → [0] Editar nombre\033[0m\n"
                            "\033[35m  → [1] Editar teléfono\033[0m\n"
                            "\033[35m  → [2] Editar correo\033[0m\n"
                            "\033[1;35mSeleccione una opción: \033[0m"
                        ))

                        if opcion in (0,1,2):
                            break
                    except(ValueError,KeyboardInterrupt):
                            print("ponga caracteres validos")
                            continue
            # elif i["dni"]!=dni_en_uso[0]:
            #     print("parece que ha habido un error en la base de datos y no hemos encontrado su perfil")

        usuarios_actualizados = []
        for user in usuarios:
            if user["dni"] == dni_en_uso[0]:
                if opcion==0:
                    user['nombre']=cambio_nombre_usuario() 
                elif opcion==1:
                    user['telefono']=cambio_telefono_usuario() 
                elif opcion==2:
                    user['correo']=cambio_email_usuario()
            usuarios_actualizados.append(user)

        inicializar_datos_json(datos_usuarios_js,usuarios_actualizados)
        print("el usuario a sido actualizado con exito")

def borrado_usuarios():
        while True:
            try:
                id_eliminar = int(input("Seleccione id a eliminar: "))
                break
            except(ValueError,KeyboardInterrupt):
                print("porfavor ponga caracteres valido")
                continue

        usuarios=cargar_datos_json(datos_usuarios_js)
        id_usuarios = []
        for u in usuarios:
            id_usuarios.append(u["id"])
        if id_eliminar not in id_usuarios:
            print("el usuario que esta intentando eliminar no esta en la base de datos")
            return
            
        print("\033[1;91m Recuerde que esta acción es irrevertible \033[0m")
        print()
        print("\033[1;91m Por favor vuelva a dar confirmación \033[0m")
        
        while True:
            try:
                opcion = int(input(
                    "\033[35m  → [1] Eliminar cuenta\033[0m\n"
                    "\033[35m  → [2] Volver al menú\033[0m\n"
                ))
                if opcion in (1,2):
                    break
                else:
                    print("solo 1 y 2 son numeros validos")
            except(KeyboardInterrupt,ValueError):
                print("porfavor ponga caracteres valido")
                continue

        if opcion == 1:
            for user in usuarios:
                if user["id"]==id_eliminar:
                    user["estado"]=False
            inicializar_datos_json(datos_usuarios_js, usuarios)
            
            
            arch_reservas=cargar_datos_txt(datos_reserva_txt)
            reservas=[]
            for linea in arch_reservas:
                partes=linea
                reservas.append(partes)
            
            reservas_correctas=[]
            for i in reservas:
                id_usuario=int(i[1])
                if id_usuario != id_eliminar:
                    reservas_correctas.append(i)

            if len(reservas_correctas) == len(reservas):
                print("No se eliminaron reservas asociadas.")
            else:
                inicializar_datos_txt(datos_reserva_txt, reservas_correctas)

        elif opcion == 2:
                print("volviendo al menu")
                return