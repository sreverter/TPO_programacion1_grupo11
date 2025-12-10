from entidades.reserva import *
from entidades.usuarios import *
from funciones.funciones_globales import *

colordorado = "\033[38;2;207;181;59m"

def vista_reserva(admin):
    vista = []
    # datos = cargar_datos_txt('datos/datos_reservas.txt')
    if admin:
        mostrar_archivo_texto('datos/datos_reservas.txt')
    elif admin == False:
        usuario_Act = obt_id_Actual()
        vista = devolver_usuario_txt('datos/datos_reservas.txt', usuario_Act)
        if len(vista) > 0:
            mostrar_tabla(vista, 1)
        else:
            print("\033[91mNo hay ninguna reserva registrada.\033[0m")

def alta_reserva(nueva_reserva):
    try:
        with open('datos/datos_reservas.txt', 'a', encoding='utf-8') as archivo:
            linea = f"{nueva_reserva[0]},{nueva_reserva[1]},{nueva_reserva[2]},{nueva_reserva[3]},{nueva_reserva[4]},{nueva_reserva[5]}\n"
            archivo.write(linea)
            print("\033[34mReserva guardada con éxito.\033[0m")
    except OSError as e:
        print(f"Error al guardar la reserva: {e}")

def agregar_reservas(admin):
    datos_shows = cargar_datos_json('datos/datos_shows.json')
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
            except (ValueError, KeyboardInterrupt):
                print("\033[91mEl ID que ingresó contiene caracteres inválidos.\033[0m")
                continue
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
        except (ValueError, KeyboardInterrupt):
            print("\033[91mOpción inválida, intente nuevamente.\033[0m")
            continue
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
    datos = cargar_datos_txt('datos/datos_reservas.txt')
    reserva_enct = []
    encontrado = False
    while True:
        try:
            eleccion = int(input("\033[36m→ [1] Buscar por ID de reserva\n→ [2] Buscar por ID de usuario:\033[0m "))
            if eleccion in (1, 2):
                break
            else:
                print("\033[91mDebe elegir entre 1 o 2.\033[0m")
        except (ValueError, KeyboardInterrupt):
            print("\033[91mEntrada inválida.\033[0m")
            continue
    if eleccion == 1:
        while True:
            try:
                eleccion = int(input("\033[36mIngrese ID de reserva:\033[0m "))
                break
            except (ValueError, KeyboardInterrupt):
                print("\033[91mID inválido.\033[0m")
                continue
        for i in datos:
            if i[0] == eleccion:
                encontrado = True
                reserva_enct.append(i)
        if not encontrado:
            print("\033[91mID de reserva no encontrado.\033[0m")
        else:
            mostrar_tabla(reserva_enct, 1)
    elif eleccion == 2:
        while True:
            try:
                eleccion = int(input("\033[36mIngrese ID de usuario:\033[0m "))
                break
            except (ValueError, KeyboardInterrupt):
                print("\033[91mEntrada inválida.\033[0m")
                continue
        for i in datos:
            if i[1] == eleccion:
                encontrado = True
                reserva_enct.append(i)
        if not encontrado:
            print("\033[91mID de usuario no encontrado.\033[0m")
        else:
            mostrar_tabla(reserva_enct, 1)
def borrado_reserva(admin):
    datos_reservas = cargar_datos_txt('datos/datos_reservas.txt')
    datos_shows = cargar_datos_json('datos/datos_shows.json')
    #reaparti por bloques porque ya me estaba mareando
    # === BLOQUE USUARIO NORMAL ===
    if admin == False: 
        reservas_d_usuario = False            
        reservas_usuario = []
        id_usuario = obt_id_Actual()

        for i in datos_reservas:
            if i[1] == id_usuario:
                reservas_d_usuario = True
                reservas_usuario.append(i)

        if not reservas_d_usuario:
            print("\033[91mNo hay reservas registradas a su nombre.\033[0m")
            return

        mostrar_tabla(reservas_usuario, 1)
        opcion = borrado_reserva_menu()
        id_show = []

        if opcion == 1:
            try:
                id_borrar = int(input("\033[36mIngrese el ID de la reserva que desea eliminar:\033[0m "))
                encontrada = False
                for i in datos_reservas:
                    if i[1] == id_usuario and i[0] == id_borrar:
                        id_show.append([i[3], i[5]])
                        datos_reservas.remove(i)
                        encontrada = True
                        print(f"\033[31mReserva {id_borrar} eliminada correctamente.\033[0m")
                        break
                if not encontrada:
                    print("\033[91mNo se encontró la reserva con ese ID.\033[0m")
            except (ValueError, KeyboardInterrupt):
                print("\033[31mID inválido\033[0m")
        
        # === BORRAR TODAS LAS RESERVAS ===
        elif opcion == 2:
            datos_reservas_borrar = []
            for i in datos_reservas:
                if i[1] == id_usuario:
                    id_show.append([i[3], i[5]])
                    datos_reservas_borrar.append(i)

            for i in datos_reservas_borrar:
                datos_reservas.remove(i)

            print("\033[31mTodas sus reservas han sido eliminadas.\033[0m")

        actualizar_datos_borrado(id_show, datos_reservas, datos_shows)

    # === BLOQUE ADMIN ===
    if admin == True: 
        reservas_usuario = []
        reservas_d_usuario = False
        reservas_del_id = []
        show_encontrado = False
        opcion = borrado_reserva_menu()

        if opcion == 1:
            while True:
                try:
                    eleccion = int(input("\033[36mSeleccione ID de reserva a eliminar:\033[0m "))
                    show_encontrado = False
                    for i in datos_reservas:
                        if i[0] == eleccion:
                            show_encontrado = True
                            print("\033[96mID de reserva confirmado.\033[0m")
                            break
                    if not show_encontrado:
                        print("\033[91mEsa reserva no es válida.\033[0m")
                        continue
                    else:
                        break
                except (KeyboardInterrupt, ValueError):
                    print("\033[91mCarácter inválido.\033[0m")
                    continue

            id_show = []
            datos_reservas_borrar = []
            for i in datos_reservas:
                if i[0] == eleccion:
                    datos_reservas_borrar.append(i)
                    id_show.append((i[3], i[5]))
                    break
            for i in datos_reservas_borrar:
                datos_reservas.remove(i)
            print("\033[31mLa reserva ha sido eliminada.\033[0m")
            actualizar_datos_borrado(id_show, datos_reservas, datos_shows)

        elif opcion == 2:
            while True:
                try:
                    eleccion = int(input("\033[36mSeleccione ID de usuario para eliminar sus reservas:\033[0m "))
                    for i in datos_reservas:
                        if i[1] == eleccion:
                            show_encontrado = True
                    print("\033[96mID de usuario confirmado.\033[0m")
                    if not show_encontrado:
                        print("\033[91mEse usuario no tiene reservas.\033[0m")
                        continue
                    else:
                        break
                except (KeyboardInterrupt, ValueError):
                    print("\033[91mCarácter inválido.\033[0m")
                    continue

            reservas_del_id = []
            for i in datos_reservas:
                if i[1] == eleccion:
                    reservas_usuario.append(i)
                    reservas_del_id.append(i)

            print("\n\033[34mReservas del usuario:\033[0m")
            mostrar_tabla(reservas_del_id, 1)

            datos_reservas_borrar = []
            id_show = []
            for i in datos_reservas:
                if i[1] == eleccion:
                    datos_reservas_borrar.append(i)
                    id_show.append([i[3], i[5]])

            for i in datos_reservas_borrar:
                datos_reservas.remove(i)

            print("\033[31mTodas sus reservas han sido eliminadas.\033[0m")

            for show_id, cantidad in id_show:
                for show in datos_shows:
                    if show["id-show"] == show_id:
                        show["espacios-disponibles"] += cantidad
                        show["espectadores"] -= cantidad

            print("\033[34mLos datos de capacidad fueron actualizados.\033[0m")
            inicializar_datos_txt('datos/datos_reservas.txt', datos_reservas)
            inicializar_datos_json('datos/datos_shows.json', datos_shows)

def edicion_reserva():
    datos_reservas = cargar_datos_txt('datos/datos_reservas.txt')
    datos_shows = cargar_datos_json("datos/datos_shows.json")
    mostrar_tabla(datos_reservas, 1)
    show_encontrado = False
    while not show_encontrado:
        try:
            id_a_editar = int(input("\033[36mSeleccione el ID de reserva a editar:\033[0m "))
            for r in datos_reservas:
                if r[0] == id_a_editar:
                    reserva_encontrada = r
                    show_encontrado = True
                    break
            if not show_encontrado:
                print("\033[91mNo se encontró la reserva con ese ID.\033[0m")
                continue
        except (ValueError, KeyboardInterrupt):
            print("\033[91mEntrada inválida.\033[0m")
            continue

    cantidad = int(reserva_encontrada[5])
    print(f"\033[34mEditando reserva ID: {reserva_encontrada[0]}\033[0m")

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
        except (ValueError, KeyboardInterrupt):
            print("\033[91mCarácter no válido.\033[0m")

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
            except (ValueError, KeyboardInterrupt):
                print("\033[91mNúmero inválido.\033[0m")

        if ubicacion == 1:
            nueva_ubicacion = "platea"
        elif ubicacion == 2:
            nueva_ubicacion = "campo"
        elif ubicacion == 3:
            nueva_ubicacion = "vip"

        id_show = int(reserva_encontrada[3])
        show_actual = buscar_show(id_show)
        nuevo_precio = calcular_precio(show_actual, nueva_ubicacion, cantidad)
        reserva_encontrada[2] = nueva_ubicacion
        reserva_encontrada[4] = nuevo_precio
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
            except (ValueError, KeyboardInterrupt):
                print("\033[91mEntrada inválida.\033[0m")

        for show in datos_shows:
            if show["id-show"] == reserva_encontrada[3]:
                show["espacios-disponibles"] += cantidad
                show["espectadores"] -= cantidad
                break

        for show in datos_shows:
            if show["id-show"] == nuevo_show_id:
                show["espacios-disponibles"] -= cantidad
                show["espectadores"] += cantidad
                break

        nueva_ubic = reserva_encontrada[2]
        nuevo_precio = calcular_precio(show_nuevo, nueva_ubic, cantidad)
        reserva_encontrada[3] = nuevo_show_id
        reserva_encontrada[4] = nuevo_precio
        print("\033[34mShow actualizado correctamente.\033[0m")

    inicializar_datos_txt('datos/datos_reservas.txt', datos_reservas)
    inicializar_datos_json('datos/datos_shows.json', datos_shows)
    print("\033[96mCambios guardados exitosamente.\033[0m")
