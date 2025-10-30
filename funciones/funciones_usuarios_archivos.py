from iniciacion_listas import datos_globales_usuarios, dni_en_uso,datos_de_ingreso_dni
from funciones.funciones_reservas import obt_id_Actual
from funciones.funciones_globales import mostrar_tabla
import re
import json

def vista_Usuarios(admin):
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
                with open("datos/datos_usuarios.json", "r",encoding="utf-8") as archivo:
                    datos_usuarios=json.load(archivo)
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
                with open("datos/datos_usuarios.json", "r", encoding="utf-8")as archivo:
                    datos_usuarios=json.load(archivo)
                    for user in datos_usuarios:
                        if user["id"]==eleccion:
                            encontrado=True
                            print(user['id'],user['nombre'],user['dni'],user['telefono'],user['correo'],user['estado'])
                            #imprime raro falta un imprmir lindo
                    if not encontrado:
                        print("no se a entcontrado el id del usuario")

        elif admin == False:
            id = obt_id_Actual()
            with open("datos/datos_usuarios.json", "r", encoding="utf-8")as archivo:
                datos_usuarios=json.load(archivo)
                for user in datos_usuarios:
                    if user['id']==id:
                        print(user['id'],user['nombre'],user['dni'],user['telefono'],user['correo'],user['estado'])


def edicion_usuario(admin):
    if admin:
        encontrado=False
        while True:
            try:
                eleccion = int(input("Seleccione el id de usuario a editar: "))
            except (ValueError, KeyboardInterrupt):
                print("ponga caracteres válidos")
                continue
            try:
                with open("datos/datos_usuarios.json", "r",encoding="utf-8")as archivo:
                    usuarios=json.load(archivo)
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
        with open("datos/datos_usuarios.json", "r", encoding="utf-8") as archivo:
            usuarios = json.load(archivo)

            usuarios_actualizados = []
            for user in usuarios:
                if user["id"] == eleccion:
                    if opcion==0:
                        while True:
                            try:
                                nombre_nuevo=str(input("ingrese el nombre que desea de usuario"))
                                user['nombre']=nombre_nuevo
                                break
                            except (ValueError,KeyboardInterrupt):
                                print("no se acepta el caracter que intento colocar")
                                continue
                    elif opcion==1:
                        while True:
                            try:
                                dni_nuevo = int(input("\033[36m Escriba el dni por el que desea cambiar: \033[0m"))
                                if dni_nuevo <= 0:
                                    print("no se permiten dnis menores o iguales a 0")
                                    continue
                                if dni_nuevo not in datos_de_ingreso_dni:
                                    user['dni']=dni_nuevo
                                    break
                                else:
                                    print("\033[91m El DNI por el cual pide cambiar esta siendo usado, intente de nuevo.\033[0m")
                            except ValueError:
                                print("no se admite otra cosa que no sean numeros enteros")
                    elif opcion==2:
                        while True:
                            try:
                                telefono_nuevo = int(input("\033[36mIngrese el numero de telefono por el que desea cambiar: \033[0m"))
                                if telefono_nuevo > 1100000000 and telefono_nuevo < 1199999999:
                                    user['telefono']=telefono_nuevo
                                    break
                                else:
                                    print("\033[91mEl número debe estar entre 1100000000 y 1199999999.\033[0m")
                            except (ValueError,KeyboardInterrupt):
                                print("\033[91mError: solo se admiten números.\033[0m")
                                
                            
                    elif opcion==3:
                        while True:
                            try:
                                #el usuario escribe su email 
                                email = input("\033[36m Escriba su nuevo email: \033[0m")
                                
                                #validaciones basicas de email
                                arroba = re.findall('@', email)
                                punto  = re.findall(r'\.', email)   

                                if len(arroba) !=0 and len(punto) != 0:
                                    user['correo']=email
                                    break
                                else: 
                                    print("\033[91m Email inválido, debe contener '@' y '.' \033[0m")
                            except(KeyboardInterrupt, ValueError):
                                print("ponga caracteres validos")
                                continue

                    elif opcion==4:
                        user['estado']=False
                    elif opcion==5:
                        user['estado']=True
                    
                usuarios_actualizados.append(user)

            with open("datos/datos_usuarios.json", "w", encoding="utf-8") as archivo:
                json.dump(usuarios_actualizados, archivo, indent=4, ensure_ascii=False)

            print("el usuario a sido editado con exito")
            
    

    elif admin==False:  # EDITAR USUARIO
        for i in datos_globales_usuarios:
            if i[2] == dni_en_uso[0]:
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
            with open("datos/datos_usuarios.json", "r", encoding="utf-8") as archivo:
                usuarios = json.load(archivo)

            usuarios_actualizados = []
            for user in usuarios:
                if user["dni"] == dni_en_uso[0]:
                    if opcion==0:
                        while True:
                            try:
                                nombre_nuevo=input("ingrese el nombre que desea de usuario")
                            except (ValueError,KeyboardInterrupt):
                                print("no se acepta el caracter que intento colocar")
                                continue
                            user['nombre']=nombre_nuevo

                    elif opcion==1:
                        while True:
                            try:
                                telefono_nuevo = int(input("\033[36mIngrese el numero de telefono por el que desea cambiar: \033[0m"))
                                if telefono_nuevo > 1100000000 and telefono_nuevo < 1199999999:
                                    user['telefono']=telefono_nuevo
                                    break
                                else:
                                    print("\033[91mEl número debe estar entre 1100000000 y 1199999999.\033[0m")
                            except (ValueError,KeyboardInterrupt):
                                print("\033[91mError: solo se admiten números.\033[0m")
                            
                    elif opcion==2:
                        while True:
                            try:
                                #el usuario escribe su email 
                                email = input("\033[36m Escriba su nuevo email: \033[0m")
                                
                                #validaciones basicas de email
                                arroba = re.findall('@', email)
                                punto  = re.findall(r'\.', email)   

                                if len(arroba) !=0 and len(punto) != 0:
                                    user['correo']=email
                                    break
                                else: 
                                    print("\033[91m Email inválido, debe contener '@' y '.' \033[0m")
                            except(KeyboardInterrupt, ValueError):
                                print("ponga caracteres validos")
                                continue
                    
                usuarios_actualizados.append(user)

            with open("datos/datos_usuarios.json", "w", encoding="utf-8") as archivo:
                json.dump(usuarios_actualizados, archivo, indent=4, ensure_ascii=False)


def borrado_usuarios():
        while True:
            try:
                id_eliminar = int(input("Seleccione id a eliminar: "))
                break
            except(ValueError,KeyboardInterrupt):
                print("porfavor ponga caracteres valido")
                continue
        with open("datos/datos_usuarios.json", "r",encoding="utf-8") as usuarios_revision:
            usuarios=json.load(usuarios_revision)
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
            with open("datos/datos_usuarios.json", "w", encoding="utf-8") as archivo:
                json.dump(usuarios, archivo, indent=4, ensure_ascii=False)
            
            
            with open("datos/datos_reservas.txt","r", encoding="utf-8") as arch_reservas:
                reservas=[]
                for linea in arch_reservas:
                    partes=linea.strip().split(",")
                    reservas.append(partes)

                reservas_correctas=[]
                for i in reservas:
                    id_usuario=int(i[1])
                    if id_usuario != id_eliminar:
                        reservas_correctas.append(i)

            with open("datos/datos_reservas.txt", "w", encoding="utf-8") as arch_reservas:
                for r in reservas_correctas:
                    linea = ";".join(r)
                    arch_reservas.write(linea + "\n")

        elif opcion == 2:
                print("volviendo al menu")
                return