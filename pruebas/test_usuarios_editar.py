from iniciacion_listas import datos_globales_usuarios, dni_en_uso, datos_globales_reserva,id_usuarios,datos_de_ingreso_dni
from entidades.usuarios import ver_m3,id_usuarios,ver_busqueda_usuarios
from funciones.funciones_reservas import obt_id_Actual
from funciones.funciones_globales import mostrar_tabla
import re
import json

def edicion_usuario(admin):
    if admin:

        while True:
            try:
                eleccion = int(input("Seleccione el id de usuario a editar: "))
            except (ValueError, KeyboardInterrupt):
                print("ponga caracteres válidos")
                continue

            if eleccion not in id_usuarios:
                print("ID no encontrado.")
                continue  # vuelve a pedir un ID válido

            # Si llega acá, el ID es válido
            usuario_encontrado = None
            for i in datos_globales_usuarios:
                if i[0] == eleccion:
                    usuario_encontrado = i
                    break

            if not usuario_encontrado:
                print("ID no encontrado en los datos globales.")
                continue


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
            
            if opcion == 0:
                i[1] = input("\033[36m Ingrese nombre a cambiar: \033[0m")
            elif opcion == 1:
                while True:
                    try:
                        dni = int(input("\033[36m Escriba el dni por el que desea cambiar: \033[0m"))
                        if dni not in datos_de_ingreso_dni:
                            i[2]=dni
                            break
                        else:
                            print("\033[91m El DNI por el cual pide cambiar esta siendo usado, intente de nuevo.\033[0m")
                    except ValueError:
                        print("no se admite otra cosa que no sean numeros enteros")
                
            elif opcion == 2:
                while True:
                    try:
                        telefono = int(input("\033[36mIngrese el numero de telefono por el que desea cambiar: \033[0m"))
                        if telefono > 1100000000 and telefono < 1199999999:
                            i[3]=telefono
                            break
                        else:
                            print("\033[91mEl número debe estar entre 1100000000 y 1199999999.\033[0m")
                    except ValueError:
                        print("\033[91mError: solo se admiten números.\033[0m")
            elif opcion == 3:
                while True:
                    try:
                        #el usuario escribe su email 
                        email = input("\033[36m Escriba su nuevo email: \033[0m")
                        
                        #validaciones basicas de email
                        arroba = re.findall('@', email)
                        punto  = re.findall(r'\.', email)   

                        if len(arroba) !=0 or len(punto) != 0:
                            i[4]=email
                            break
                        else: 
                            print("\033[91m Email inválido, debe contener '@' y '.' \033[0m")
                    except(KeyboardInterrupt, ValueError):
                        print("ponga caracteres validos")
                        continue

            elif opcion == 4:
                i[5]= False
            elif opcion == 5:
                i[5] = True
            
            print("el usuario a sido editado con exito")
            break
    

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
                if opcion == 0:
                    i[1] = input("\033[36mIngrese nombre: \033[0m")

                elif opcion == 1:
                    while True:
                        try:
                            telefono = int(input("\033[36mIngrese el numero de telefono por el que desea cambiar: \033[0m"))
                            if telefono > 1100000000 and telefono < 1199999999:
                                i[3]=telefono
                                break
                            else:
                                print("\033[91mEl número debe estar entre 1100000000 y 1199999999.\033[0m")
                        except ValueError:
                            print("\033[91mError solo se admiten números.\033[0m")

                elif opcion == 2:
                    #el usuario escribe su email 
                    email = input("\033[36m Escriba su nuevo email: \033[0m")
                    
                    #validaciones basicas de email
                    arroba = re.findall('@', email)
                    punto  = re.findall(r'\.', email)   

                    if len(arroba) ==0 or len(punto) == 0:
                        print("\033[91m Email inválido, debe contener '@' y '.' \033[0m")
                        email = input("\033[36m Escriba su email: \033[0m")
                    else:
                        i[4]=email
    
                print("\033[92mSe ha editado el usuario exitosamente.\033[0m")