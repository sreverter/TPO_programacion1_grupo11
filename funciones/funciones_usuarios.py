from ingreso import dni_en_uso
from funciones.funciones_reservas import obt_id_Actual
from funciones.funciones_globales import *
from entidades.usuarios import *
datos_usuarios_js="datos/datos_usuarios.json"
datos_reserva_txt="datos/datos_reservas.txt"

def vista_Usuarios(admin):
        datos_usuarios=cargar_datos_json(datos_usuarios_js)
        if not datos_usuarios:
            print("No hay usuarios cargados.")
            return

        if admin: 
            while True:
                try:
                    eleccion = int(input("\033[36m1-VER TODOS LOS USUARIOS\n2-BUSCAR USUARIO POR ID:\033[0m"))
                    if eleccion in (1,2):
                        break
                    else:
                        print("\033[91mel número no está dentro de los parámetros dados\033[0m")
                except ValueError:
                    print("Entrada inválida.")
                except KeyboardInterrupt:
                    print("Operación cancelada.")
                    return

            if eleccion == 1:
                while True:
                    try:
                        filtro_usuarios= int(input("\033[36mIngrese el estado de los usuarios a mostrar (1)Activo - 2)Inactivo - 3)Todos):\033[0m "))
                        if filtro_usuarios in (1,2,3):
                            break
                        print("Opción inválida.")
                    except ValueError:
                        print("Entrada inválida.")
                    except KeyboardInterrupt:
                        print("Operación cancelada.")
                        return
                if filtro_usuarios == 1:
                    usuarios_filtrados = list(filter(lambda x: x["estado"] is True, datos_usuarios))
                    print("\n\033[92m=== USUARIOS ACTIVOS ===\033[0m")
                elif filtro_usuarios == 2:
                    usuarios_filtrados = list(filter(lambda x: x["estado"] is False, datos_usuarios))
                    print("\n\033[91m=== USUARIOS INACTIVOS ===\033[0m")
                elif filtro_usuarios == 3:
                    usuarios_filtrados = datos_usuarios
                    print("\n\033[94m=== TODOS LOS USUARIOS ===\033[0m")
                if usuarios_filtrados:
                    mostrar_tabla(usuarios_filtrados, 2)  
                else:
                    print("\033[91mNo hay usuarios con ese estado.\033[0m")
            elif eleccion == 2:
                while True:
                    try:
                        eleccion = int(input("\033[36mIngrese ID a buscar:\033[0m "))
                        break
                    except ValueError:
                        print("Entrada inválida.")
                    except KeyboardInterrupt:
                        print("Operación cancelada.")
                        return
                encontrado=False
                for user in datos_usuarios:
                    if user["id"]==eleccion:
                        encontrado=True
                        mostrar_tabla([user], 2)
                if not encontrado:
                    print("\033[91mNo se ha encontrado el ID del usuario\033[0m")
        elif admin == False:
            id = obt_id_Actual()
            for user in datos_usuarios:
                if user['id']==id:
                    mostrar_tabla([user], 2)

def edicion_usuario(admin):
    usuarios=cargar_datos_json(datos_usuarios_js)
    if not usuarios:
        print("No se pudieron cargar los usuarios.")
        return

    if admin:

        while True:
            try:
                eleccion = int(input("\033[36mSeleccione el ID de usuario a editar:\033[0m "))
                break
            except (ValueError, KeyboardInterrupt):
                print("\033[91mIngrese caracteres válidos\033[0m")
                continue
        usuario_encontrado = None

        for user in usuarios:
            if user["id"] == eleccion:
                usuario_encontrado = user
                break

        if usuario_encontrado is None:
            print("Usuario no encontrado.")
            return

        while True:
            try:
                opcion = int(input(
                "\n\033[36m=== MENÚ DE EDICIÓN ===\033[0m\n"
                "\033[35m  → [0] Editar nombre\033[0m\n"
                "\033[35m  → [1] Editar DNI\033[0m\n"
                "\033[35m  → [2] Editar teléfono\033[0m\n"
                "\033[35m  → [3] Editar correo\033[0m\n"
                "\033[35m  → [4] Editar estado a Inactivo\033[0m\n"
                "\033[35m  → [5] Editar estado a Activo\033[0m\n"
                "\033[36mSeleccione una opción:\033[0m "
                ))
                if opcion in (0,1,2,3,4,5):
                    break
                else:
                    print("\033[91mel número ingresado no es válido\033[0m")
                    continue
            except(KeyboardInterrupt,ValueError):
                print("\033[91mIngrese caracteres válidos\033[0m")
                continue

        usuarios_actualizados = []
        for user in usuarios:
            if user["id"] == eleccion:
                if opcion==0:
                    user['nombre'] = cambio_nombre_usuario()
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
        print("\033[92mEl usuario ha sido editado con éxito\033[0m")

    elif admin==False:
        for i in usuarios:
            if i["dni"] == dni_en_uso[0]:
                print("\033[96mSe ha accedido a su perfil\033[0m")
                while True:
                    try:
                        opcion = int(input(
                            "\n\033[36m=== MENÚ DE EDICIÓN ===\033[0m\n"
                            "\033[35m  → [0] Editar nombre\033[0m\n"
                            "\033[35m  → [1] Editar teléfono\033[0m\n"
                            "\033[35m  → [2] Editar correo\033[0m\n"
                            "\033[36mSeleccione una opción:\033[0m "
                        ))
                        if opcion in (0,1,2):
                            break
                    except ValueError:
                        print("opcion inválida.")
                        return
                    except KeyboardInterrupt:
                        print("Edición cancelada.")
                        return
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
        print("\033[92mEl usuario ha sido actualizado con éxito\033[0m")

def borrado_usuarios():
        while True:
            try:
                id_eliminar = int(input("\033[36mSeleccione ID a eliminar:\033[0m "))
                break
            except ValueError:
                print("ID inválido.")
                return
            except KeyboardInterrupt:
                print("Edición cancelada.")
                return
        usuarios=cargar_datos_json(datos_usuarios_js)
        if not usuarios:
            print("No hay usuarios cargados.")
            return

        id_usuarios = []
        for u in usuarios:
            id_usuarios.append(u["id"])
        if id_eliminar not in id_usuarios:
            print("\033[91mEl usuario que intenta eliminar no está en la base de datos\033[0m")
            return
            
        print("\033[91mRecuerde que esta acción es irrevertible\033[0m")
        print("\033[91mPor favor vuelva a dar confirmación\033[0m")
        
        while True:
            try:
                opcion = int(input("[1] Eliminar / [2] Cancelar: "))
                break
            except ValueError:
                print("Opción inválida.")
                return
            except KeyboardInterrupt:
                return

        if opcion == 1:
            for user in usuarios:
                if user["id"]==id_eliminar:
                    user["estado"]=False
            inicializar_datos_json(datos_usuarios_js, usuarios)
            
            arch_reservas=cargar_datos_txt(datos_reserva_txt)#-----------------------------------
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
                print("\033[91mNo se eliminaron reservas asociadas\033[0m")
            else:
                inicializar_datos_txt(datos_reserva_txt, reservas_correctas)

        elif opcion == 2:
                print("\033[94mVolviendo al menú\033[0m")
                return
