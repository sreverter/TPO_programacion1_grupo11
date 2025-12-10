from ingreso import dni_en_uso
from funciones.funciones_reservas import obt_id_Actual
from funciones.funciones_globales import *
from entidades.usuarios import *
datos_usuarios_js="datos/datos_usuarios.json"
datos_reserva_txt="datos/datos_reservas.txt"
datos_shows_js = "datos/datos_shows.json"


def vista_Usuarios(admin):
        datos_usuarios=cargar_datos_json(datos_usuarios_js)
        if not datos_usuarios:
            print("\033[91mNo hay usuarios registrados.\033[0m")
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
                    print("\033[91mError de tipeo.\033[0m")
                except (KeyboardInterrupt, EOFError):
                    return
            if eleccion == 1:
                while True:
                    try:
                        filtro_usuarios = int(input("\033[36mEstado: (1)Activo - (2)Inactivo - (3)Todos: \033[0m"))
                        if filtro_usuarios in (1, 2, 3):
                            break
                        print("\033[91mOpción inválida.\033[0m")
                    except ValueError:
                        print("Error de tipeo")
                    except (KeyboardInterrupt, EOFError):
                        return
                if filtro_usuarios == 1:
                    usuarios_filtrados = list(filter(lambda x: x["estado"] is True, datos_usuarios))
                    print("\n\033[92m=== USUARIOS ACTIVOS ===\033[0m")
                elif filtro_usuarios == 2:
                    usuarios_filtrados = list(filter(lambda x: x["estado"] is False, datos_usuarios))
                    print("\n\033[91m=== USUARIOS INACTIVOS ===\033[0m")
                else:
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
                        print("\033[91mError de tipeo.\033[0m")
                    except (KeyboardInterrupt, EOFError):
                        return
                encontrado=False
                for user in datos_usuarios:
                    if user["id"]==eleccion:
                        encontrado=True
                        mostrar_tabla([user], 2)
                        break
                if not encontrado:
                    print("\033[91mNo se ha encontrado el ID del usuario\033[0m")
        else:
            id = obt_id_Actual()
            if id is None:
                print("\033[91mError al identificar usuario.\033[0m")
                return
            for user in datos_usuarios:
                if user['id']==id:
                    mostrar_tabla([user], 2)
                    return

def edicion_usuario(admin):
    usuarios = cargar_datos_json(datos_usuarios_js)
    if not usuarios:
        print("No hay usuarios.")
        return

    # 1. Selección del Usuario (Solo Admin busca por ID, Usuario edita su propio perfil)
    usuario_a_editar = None
    
    if admin:
        while True:
            try:
                eleccion = int(input("\033[36mSeleccione el ID de usuario a editar:\033[0m "))
                for user in usuarios:
                    if user['id'] == eleccion:
                        usuario_a_editar = user
                        break
                
                if usuario_a_editar:
                    break
                else:
                    print("\033[91mUsuario no encontrado.\033[0m")
            except ValueError:
                print("\033[91mError de tipeo.\033[0m")
            except (KeyboardInterrupt, EOFError):
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
            except ValueError:
                print("\033[91mError de tipeo.\033[0m")
            except (KeyboardInterrupt, EOFError):
                return

    else:
        # Modo Usuario Normal: Se edita a sí mismo
        if not dni_en_uso:
            return
        dni_actual = dni_en_uso[0]
        for user in usuarios:
            if user['dni'] == dni_actual:
                usuario_a_editar = user
                print("\033[96mSe ha accedido a su perfil\033[0m")
                break
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
                print("\033[91mError de tipeo.\033[0m")
            except (KeyboardInterrupt, EOFError):
                return
    if not usuario_a_editar:
        print("Error al cargar perfil.")
        return

    # 3. Ejecución de Cambios (Validando NONE)
    cambio_realizado = False

    if opcion == 0:
        nuevo_nombre = cambio_nombre_usuario()
        if nuevo_nombre is not None:
            usuario_a_editar['nombre'] = nuevo_nombre
            cambio_realizado = True

    elif opcion == 1 and admin:
        nuevo_dni = cambio_dni_usuario()
        if nuevo_dni is not None:
            usuario_a_editar['dni'] = nuevo_dni
            cambio_realizado = True

    elif opcion == 2:
        nuevo_tel = cambio_telefono_usuario()
        if nuevo_tel is not None:
            usuario_a_editar['telefono'] = nuevo_tel
            cambio_realizado = True

    elif opcion == 3:
        nuevo_email = cambio_email_usuario()
        if nuevo_email is not None:
            usuario_a_editar['correo'] = nuevo_email
            cambio_realizado = True
    elif opcion==4:
        usuario_a_editar['estado']=False
        cambio_realizado=True

    elif opcion==5:
        usuario_a_editar['estado']=True
        cambio_realizado=True
        
    if cambio_realizado:
        inicializar_datos_json(datos_usuarios_js, usuarios)
        print("\033[92mDatos actualizados con éxito.\033[0m")
    else:
        print("\033[93mNo se realizaron cambios (Cancelado).\033[0m")

def borrado_usuarios():
    usuarios = cargar_datos_json(datos_usuarios_js)
    if not usuarios:
        print("No hay usuarios.")
        return
    while True:
        try:
            id_eliminar = int(input("\033[36mSeleccione ID a eliminar:\033[0m "))
            usuario_encontrado = None
            for u in usuarios:
                if u["id"] == id_eliminar:
                    usuario_encontrado = u
                    break
            

            if not usuario_encontrado:
                print("\033[91mUsuario no encontrado.\033[0m")
                return
            break

        except ValueError:
            print("Error de tipeo")
        except (KeyboardInterrupt, EOFError):
            return
        print("\033[91mRecuerde que esta acción es irrevertible\033[0m")
        print("\033[91mPor favor vuelva a dar confirmación\033[0m")

        
    while True:

        try:
            opcion = int(input("\033[36m[1] Confirmar\n[2] Cancelar\nOpción: \033[0m"))
            if opcion == 2:
                return
            if opcion == 1:
                break
        except ValueError:
            print("Error de tipeo")
        except (KeyboardInterrupt, EOFError):
            return
        
    usuario_encontrado["estado"] = False
    inicializar_datos_json(datos_usuarios_js, usuarios)
    print("\033[93mUsuario desactivado.\033[0m")
    datos_reservas = cargar_datos_txt(datos_reserva_txt)
    datos_shows = cargar_datos_json(datos_shows_js)
    
    reservas_a_conservar = []
    id_shows_afectados = []
    count_borrados = 0
    for reserva in datos_reservas:
        try:
            
            reserva_id = int(reserva[1])
            
            if reserva_id == id_eliminar:
                reserva_id_show = int(reserva[3])
                reserva_cantidad = int(reserva[5])
                id_shows_afectados.append((reserva_id_show, reserva_cantidad))
                count_borrados += 1
            else:
                reservas_a_conservar.append(reserva)
        except (ValueError, IndexError):
            continue

    if count_borrados > 0:
        inicializar_datos_txt(datos_reserva_txt, reservas_a_conservar)

        for show_id, cantidad in id_shows_afectados:
            for show in datos_shows:
                if show["id-show"] == show_id:
                    show["espacios-disponibles"] += cantidad
                    show["espectadores"] -= cantidad
                    break
        
        # C. Guardamos el JSON de shows actualizado
        inicializar_datos_json(datos_shows_js, datos_shows)
        print(f"\033[92mSe eliminaron {count_borrados} reservas y se liberó el espacio correspondiente.\033[0m")
    else:
        print("\033[94mEl usuario no tenía reservas asociadas.\033[0m")