from entidades.reserva import *
from entidades.usuarios import *
from funciones.funciones_globales import *

colordorado = "\033[38;2;207;181;59m"

def vista_reserva(admin):
    vista = []
    if admin:
        try:
            mostrar_archivo_texto('datos/datos_reservas.txt')
        except OSError:
            print("\033[91mNo se pudo acceder al archivo de reservas.\033[0m")
        return
    elif admin == False:
        usuario_Act = obt_id_Actual()
        vista = busqueda_en_txt('datos/datos_reservas.txt', usuario_Act, 1)
        if len(vista) > 0:
            mostrar_tabla(vista, 1)
        else:
            print("\033[91mNo hay ninguna reserva registrada.\033[0m")

def alta_reserva(nueva_reserva):
    try:
        with open('datos/datos_reservas.txt', 'a', encoding='utf-8') as archivo:
            linea = f"{nueva_reserva[0]},{nueva_reserva[1]},{nueva_reserva[2]},{nueva_reserva[3]},{nueva_reserva[4]},{nueva_reserva[5]}\n"
            archivo.write(linea)
    except OSError as e:
        print(f"\033[91mError al guardar la reserva: {e}\033[0m")

def agregar_reservas(admin):
    try:
        datos_shows = cargar_datos_json('datos/datos_shows.json')
    except OSError:
        print("\033[91mNo se pudo cargar el archivo de shows.\033[0m")
        return

    id_reserva = id_alt_r()
    id_usuario = obt_id_Actual()
    mostrar_tabla(datos_shows, 2)
    busqueda = True
    while busqueda:
        while True:
            try:
                num_reserva = int(input("\033[36m¿Cuántas reservas desea hacer?\033[0m "))
                if num_reserva <= 0:
                    print("\033[91mEl número ingresado no es válido.\033[0m")
                    continue
                show = int(input("\033[36mIngrese el ID del show al que desea asistir:\033[0m "))
                show_encontrado = False
                tiene_capacidad = False
                for i in datos_shows:
                    if i["id-show"] == show:
                        show_encontrado = True
                        if i["espacios-disponibles"] > 0 and i["espacios-disponibles"] >= num_reserva:
                            tiene_capacidad = True
                if not show_encontrado:
                    print("\033[91mEl ID ingresado no existe.\033[0m")
                    continue
                elif not tiene_capacidad:
                    print("\033[91mEste show no tiene capacidad disponible.\033[0m")
                    continue
                else:
                    busqueda = False
                    break
            except ValueError:
                print("\033[91mEntrada inválida.\033[0m")
            except (KeyboardInterrupt, EOFError):
                return
    for i in datos_shows:
        if i["id-show"] == show:
            i["espacios-disponibles"] -= num_reserva
            i["espectadores"] += num_reserva
    for i in datos_shows:
        if i["id-show"] == show:
            precio_platea = i["precio"] * num_reserva
            precio_campo = precio_platea * 2
            precio_vip = precio_platea * 3
    while True:
        try:
            ubicacion_u = int(input(
                "\n\033[92m=============  MENÚ DE UBICACIONES  =============\033[0m\n"
                f"\033[36m  → [1] El costo de platea es de {precio_platea}\033[0m\n"
                f"\033[36m  → [2] El costo de campo es de {precio_campo}\033[0m\n"
                f"{colordorado}  → [3] El costo de VIP es de {precio_vip}\033[0m\n"
                "\033[92m================================================\033[0m\n"
                "\033[36mSeleccione tipo de ubicación:\033[0m "
            ))
            if ubicacion_u not in (1, 2, 3):
                print("\033[91mDebe elegir una opción válida (1, 2 o 3).\033[0m")
                continue
            else:
                break
        except ValueError:
            print("\033[91mEntrada inválida.\033[0m")
        except (KeyboardInterrupt, EOFError):
            return
    if ubicacion_u == 1:
        precio_act = precio_platea
        sector = "platea"
    elif ubicacion_u == 2:
        precio_act = precio_campo
        sector = "campo"
    elif ubicacion_u == 3:
        precio_act = precio_vip
        sector = "vip"
    print(f"\033[34mReserva generada con éxito. Precio total: ${precio_act}\033[0m")

    nueva_reserva = [id_reserva, id_usuario, sector, show, precio_act, num_reserva]
    alta_reserva(nueva_reserva)
    inicializar_datos_json('datos/datos_shows.json', datos_shows)

def busqueda_Reserva():
    reserva_enct = []
    encontrado = False
    while True:
        try:
            eleccion = int(input("\033[36m→ [1] Buscar por ID de reserva\n→ [2] Buscar por ID de usuario:\033[0m "))
            if eleccion in (1, 2):
                break
            else:
                print("\033[91mDebe elegir entre 1 o 2.\033[0m")
        except ValueError:
            print("\033[91mEntrada inválida.\033[0m")
            continue
        except (KeyboardInterrupt, EOFError):
            continue
    if eleccion == 1:
        while True:
            try:
                eleccion = int(input("\033[36mIngrese ID de reserva:\033[0m "))
                break
            except ValueError:
                print("\033[91mEntrada inválida.\033[0m")
                continue
            except (KeyboardInterrupt, EOFError):
                continue
        busqueda = busqueda_en_txt('datos/datos_reservas.txt', eleccion, 2)
        if busqueda:
            encontrado = True
            reserva_enct = busqueda
        if not encontrado:
            print("\033[91mID de reserva no encontrado.\033[0m")
        else:
            mostrar_tabla(reserva_enct, 1)
    elif eleccion == 2:
        while True:
            try:
                eleccion = int(input("\033[36mIngrese ID de usuario:\033[0m "))
                break
            except ValueError:
                print("\033[91mEntrada inválida.\033[0m")
                continue
            except (KeyboardInterrupt, EOFError):
                continue
        busqueda = busqueda_en_txt('datos/datos_reservas.txt', eleccion, 1)
        if busqueda:
            encontrado = True
            reserva_enct = busqueda
        if not encontrado:
            print("\033[91mID de usuario no encontrado.\033[0m")
        else:
            mostrar_tabla(reserva_enct, 1)


def borrado_reserva(admin): 
    try:
        datos_shows = cargar_datos_json('datos/datos_shows.json')
    except OSError:
        print("\033[91mNo se pudo acceder al archivo de shows.\033[0m")
        return

    
    id_usuario_actual = obt_id_Actual()
    reservas_a_borrar = []

    # ==== BLOQUE USUARIO ====
    if not admin: 
        mis_reservas = busqueda_en_txt('datos/datos_reservas.txt', id_usuario_actual, 1)

        if not mis_reservas:
            print("\033[91mNo hay reservas registradas a su nombre.\033[0m")
            return

        mostrar_tabla(mis_reservas, 1)
        opcion = borrado_reserva_menu()

        if opcion == 1:
            try:
                id_reserva = int(input("\033[36mIngrese el ID de la reserva que desea eliminar:\033[0m "))

                reserva_encontrada = None
                for res in mis_reservas:
                    if int(res[0]) == id_reserva:
                        reserva_encontrada = res
                        break
                
                if reserva_encontrada:
                    reservas_a_borrar.append(reserva_encontrada)
                    borrado_en_txt('datos/datos_reservas.txt', id_reserva, 1) 
                    print(f"\033[31mReserva {id_reserva} eliminada correctamente.\033[0m")
                else:
                    print("\033[91mEl ID ingresado no corresponde a una de sus reservas.\033[0m")
                    return

            except ValueError:
                print("\033[91mEntrada inválida.\033[0m")
            except (KeyboardInterrupt, EOFError):
                return
        
        elif opcion == 2:
            reservas_a_borrar = mis_reservas 
            borrado_en_txt('datos/datos_reservas.txt', id_usuario_actual, 2)
            print("\033[31mTodas sus reservas han sido eliminadas.\033[0m")

    # ==== BLOQUE ADMIN ====
    elif admin:
        opcion = borrado_reserva_menu()

        if opcion == 1:
            try:
                id_reserva = int(input("\033[36mSeleccione ID de reserva a eliminar:\033[0m "))

                busqueda = busqueda_en_txt('datos/datos_reservas.txt', id_reserva, 2) 
                
                if busqueda:
                    reservas_a_borrar = busqueda
                    borrado_en_txt('datos/datos_reservas.txt', id_reserva, 1)
                    print(f"\033[31mLa reserva {id_reserva} ha sido eliminada.\033[0m")
                else:
                    print("\033[91mNo se encontró ninguna reserva con ese ID.\033[0m")
                    return
            except ValueError:
                print("\033[91mEntrada inválida.\033[0m")
            except (KeyboardInterrupt, EOFError):
                return


        elif opcion == 2:
            try:
                id_usuario_target = int(input("\033[36mSeleccione ID de usuario para eliminar sus reservas:\033[0m "))
                
                busqueda = busqueda_en_txt('datos/datos_reservas.txt', id_usuario_target, 1)
                
                if busqueda:
                    print("\n\033[34mReservas encontradas del usuario:\033[0m")
                    mostrar_tabla(busqueda, 1)
                    
                    reservas_a_borrar = busqueda
                    borrado_en_txt('datos/datos_reservas.txt', id_usuario_target, 2)
                    print("\033[31mTodas las reservas del usuario han sido eliminadas.\033[0m")
                else:
                    print("\033[91mEse usuario no tiene reservas registradas.\033[0m")
                    return

            except ValueError:
                print("\033[91mEntrada inválida.\033[0m")
            except (KeyboardInterrupt, EOFError):
                return

    if reservas_a_borrar:
        cambios_realizados = False
        
        shows_y_cantidades = list(map(lambda r: (int(r[3]), int(r[5])), reservas_a_borrar))

        cambios_realizados = False

        for id_show_reserva, cantidad_entradas in shows_y_cantidades:
            for show in datos_shows:
                if show["id-show"] == id_show_reserva:
                    show["espacios-disponibles"] += cantidad_entradas
                    show["espectadores"] -= cantidad_entradas
                    cambios_realizados = True
                    break

        if cambios_realizados:
            inicializar_datos_json('datos/datos_shows.json', datos_shows) 
            print("\033[34mDisponibilidad de asientos actualizada en el sistema.\033[0m")

def edicion_reserva():
    datos_shows = cargar_datos_json("datos/datos_shows.json")
    try:
        mostrar_archivo_texto('datos/datos_reservas.txt')
    except OSError:
        print("\033[91mNo se pudo acceder al archivo de reservas.\033[0m")
        return

    show_encontrado = False
    while not show_encontrado:
        try:
            id_a_editar = int(input("\033[36mSeleccione el ID de reserva a editar:\033[0m "))
            reserva_encontrada = busqueda_en_txt('datos/datos_reservas.txt', id_a_editar, 2)
            if reserva_encontrada:
                show_encontrado = True
            if not show_encontrado:
                print("\033[91mNo se encontró la reserva con ese ID.\033[0m")
                continue
        except ValueError:
            print("\033[91mEntrada inválida.\033[0m")
        except (KeyboardInterrupt, EOFError):
            return

    try:
        cantidad = int(reserva_encontrada[0][5])
    except (IndexError, ValueError):
        print("\033[91mDatos de reserva corruptos.\033[0m")
        return

    print(f"\033[34mEditando reserva ID: {reserva_encontrada[0][0]}\033[0m")

    while True:
        try:
            eleccion = int(input(
                "\n\033[92m=== MENÚ DE EDICIÓN DE RESERVA ===\033[0m\n"
                "\033[36m  → [1] Editar ubicación\033[0m\n"
                "\033[36m  → [2] Editar show\033[0m\n"
                "\033[36mSeleccione una opción:\033[0m "
            ))
            if eleccion in (1, 2):
                break
            print("\033[91mOpción inválida.\033[0m")
        except ValueError:
            print("\033[91mEntrada inválida.\033[0m")
        except (KeyboardInterrupt, EOFError):
            return

    if eleccion == 1:
        while True:
            try:
                ubicacion = int(input(
                    "\n\033[92m=== SELECCIONE NUEVA UBICACIÓN ===\033[0m\n"
                    "\033[36m  → [1] Platea\033[0m\n"
                    "\033[36m  → [2] Campo\033[0m\n"
                    "\033[36m  → [3] VIP\033[0m\n"
                    "\033[36mSeleccione opción:\033[0m "
                ))
                if ubicacion in (1, 2, 3):
                    break
                print("\033[91mDebe ingresar un número entre 1 y 3.\033[0m")
            except ValueError:
                print("\033[91mEntrada inválida.\033[0m")
            except (KeyboardInterrupt, EOFError):
                return

        if ubicacion == 1:
            nueva_ubicacion = "platea"
        elif ubicacion == 2:
            nueva_ubicacion = "campo"
        elif ubicacion == 3:
            nueva_ubicacion = "vip"

        id_show = int(reserva_encontrada[0][3])
        show_actual = buscar_show(id_show)
        if not show_actual:
            print("\033[91mEl show asociado ya no existe.\033[0m")
            return

        nuevo_precio = calcular_precio(show_actual, nueva_ubicacion, cantidad)
        modificacion_en_txt('datos/datos_reservas.txt', id_a_editar, nuevo_show_id=None, nuevo_sector=nueva_ubicacion, nuevo_precio=nuevo_precio)
        print("\033[34mUbicación y precio actualizados correctamente.\033[0m")

    elif eleccion == 2:
        mostrar_tabla(datos_shows, 2)
        while True:
            try:
                nuevo_show_id = int(input("\033[36mIngrese el ID del nuevo show:\033[0m "))
                show_nuevo = buscar_show(nuevo_show_id)
                if show_nuevo == 0:
                    print("\033[91mEl ID ingresado no existe.\033[0m")
                    continue
                if show_nuevo['espacios-disponibles'] <= 0:
                    print("\033[91mNo hay capacidad disponible en ese show.\033[0m")
                    continue
                break
            except ValueError:
                print("\033[91mEntrada inválida.\033[0m")
            except (KeyboardInterrupt, EOFError):
                return

        for show in datos_shows:
            if show["id-show"] == reserva_encontrada[0][3]:
                show["espacios-disponibles"] += cantidad
                show["espectadores"] -= cantidad
                break

        for show in datos_shows:
            if show["id-show"] == nuevo_show_id:
                show["espacios-disponibles"] -= cantidad
                show["espectadores"] += cantidad
                break

        nueva_ubic = reserva_encontrada[0][2]
        nuevo_precio = calcular_precio(show_nuevo, nueva_ubic, cantidad)
        reserva_encontrada[0][3] = nuevo_show_id
        reserva_encontrada[0][4] = nuevo_precio
        modificacion_en_txt('datos/datos_reservas.txt', id_a_editar, nuevo_show_id, nuevo_sector=None, nuevo_precio=nuevo_precio)
        print("\033[34mShow actualizado correctamente.\033[0m")

    inicializar_datos_json('datos/datos_shows.json', datos_shows)
    print("\033[96mCambios guardados exitosamente.\033[0m")
