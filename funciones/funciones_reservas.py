from entidades.reserva import *
from entidades.usuarios import *
from funciones.funciones_globales import *

colordorado = "\033[38;2;207;181;59m"

def vista_reserva(admin):
    vista = []
    datos = cargar_datos_txt('datos/datos_reservas.txt')
    
    if not datos:
        print("\033[91mNo hay ninguna reserva registrada.\033[0m")
        return
    if admin:
        mostrar_tabla(datos, 1)
    elif admin == False:
        usuario_Act = obt_id_Actual()
        for i in datos:
            try:
                if int(i[1]) == usuario_Act:
                    vista.append(i)
            except ValueError:
                continue
        if len(vista) > 0:
            mostrar_tabla(vista, 1)
        else:
            print("\033[91mNo hay ninguna reserva registrada.\033[0m")

def agregar_reservas(admin):
    datos_shows = cargar_datos_json('datos/datos_shows.json')
    if not datos_shows:
        print("\033[91mNo hay shows disponibles para reservar.\033[0m")
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

                show_seleccionado = None
                for s in datos_shows:
                    if s["id-show"] == show:
                        show_seleccionado = s
                        break
                
                if not show_seleccionado:
                    print("\033[91mEl ID ingresado no existe.\033[0m")
                    continue

                if show_seleccionado["espacios-disponibles"] < num_reserva:
                    print(f"\033[91mNo hay suficiente capacidad. Disponibles: {show_seleccionado['espacios-disponibles']}\033[0m")
                    continue
                busqueda = False
                break
                
            except ValueError:
                print("\033[91mError: Ingrese solo números enteros.\033[0m")
                continue
            except (KeyboardInterrupt, EOFError):
                print("\n\033[93mReserva cancelada por el usuario.\033[0m")
                return
            
    show_seleccionado["espacios-disponibles"] -= num_reserva
    show_seleccionado["espectadores"] += num_reserva

    # Calculamos precios base
    precio_platea = show_seleccionado["precio"] * num_reserva
    precio_campo = precio_platea * 2
    precio_vip = precio_platea * 3

    while True:
        try:
            print("\n\033[92m=============  MENÚ DE UBICACIONES  =============\033[0m")
            print(f"\033[36m  → [1] Platea (Total: ${precio_platea})\033[0m")
            print(f"\033[36m  → [2] Campo  (Total: ${precio_campo})\033[0m")
            print(f"{colordorado}  → [3] VIP    (Total: ${precio_vip})\033[0m")
            print("\033[92m================================================\033[0m")
            
            ubicacion_u = int(input("\033[36mSeleccione tipo de ubicación: \033[0m"))

            if ubicacion_u == 1:
                precio_act = precio_platea
                sector = "platea"
                break
            elif ubicacion_u == 2:
                precio_act = precio_campo
                sector = "campo"
                break
            elif ubicacion_u == 3:
                precio_act = precio_vip
                sector = "vip"
                break
            else:
                print("\033[91mOpción inválida (1-3).\033[0m")
                continue

        except ValueError:
            print("\033[91mError de tipeo.\033[0m")
        except (KeyboardInterrupt, EOFError):
            print("\n\033[93mOperación cancelada.\033[0m")
            return
        
    print(f"\033[34mReserva generada con éxito. Precio total: ${precio_act}\033[0m")

    datos_reservas = cargar_datos_txt('datos/datos_reservas.txt')
    nueva_reserva = [id_reserva, id_usuario, sector, show_seleccionado["id-show"], precio_act, num_reserva]
    datos_reservas.append(nueva_reserva)

    inicializar_datos_txt('datos/datos_reservas.txt', datos_reservas)
    inicializar_datos_json('datos/datos_shows.json', datos_shows)

def busqueda_Reserva():
    datos = cargar_datos_txt('datos/datos_reservas.txt')
    if not datos:
        print("\033[91mNo hay reservas para buscar.\033[0m")
        return

    while True:
        try:
            eleccion = int(input("\033[36m→ [1] Buscar por ID de reserva\n→ [2] Buscar por ID de usuario:\nOpción: \033[0m"))
            if eleccion in (1, 2):
                break
            print("\033[91mDebe elegir entre 1 o 2.\033[0m")
        except ValueError:
            print("\033[91mError de tipeo.\033[0m")
        except (KeyboardInterrupt, EOFError):
            return
    reserva_enct=[]
    encontrado = False 
    if eleccion == 1:
        while True:
            try:
                eleccion = int(input("\033[36mIngrese ID de reserva:\033[0m "))
                break
            except ValueError:
                print("\033[91mID inválido.\033[0m")
            except (KeyboardInterrupt, EOFError):
                return
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
            except ValueError:
                print("\033[91mEntrada inválida.\033[0m")
            except (KeyboardInterrupt, EOFError):
                return
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
    if not datos_reservas:
        print("No hay reservas para borrar.")
        return

    #reaparti por bloques porque ya me estaba mareando
    # === BLOQUE USUARIO NORMAL ===
    if not admin:           
        reservas_usuario = []
        id_usuario = obt_id_Actual()

        for i in datos_reservas:
            if i[1] == id_usuario:
                reservas_usuario.append(i)

        if not reservas_usuario:
            print("\033[91mNo hay reservas registradas a su nombre.\033[0m")
            return

        mostrar_tabla(reservas_usuario, 1)
        opcion = borrado_reserva_menu()
        if opcion is None: 
            return
        id_show = []

        if opcion == 1:
            try:
                id_borrar = int(input("\033[36mIngrese el ID de la reserva que desea eliminar:\033[0m "))
                reserva_a_borrar=None
                for i in reservas_usuario:
                    if i[0] == id_borrar:
                        reserva_a_borrar=i
                        break
                
                if reserva_a_borrar:
                    id_show.append([reserva_a_borrar[3], reserva_a_borrar[5]])
                    datos_reservas.remove(reserva_a_borrar)
                    print(f"\033[31mReserva {id_borrar} eliminada.\033[0m")
                else:
                    print("\033[91mNo se encontró la reserva con ese ID.\033[0m")
            except ValueError:
                print("\033[91mID inválido.\033[0m")
            except (KeyboardInterrupt, EOFError):
                return
        
        # === BORRAR TODAS LAS RESERVAS ===
        elif opcion == 2:
            datos_reservas_borrar = []
            for i in datos_reservas:
                if i[1] == id_usuario:
                    id_show.append([i[3], i[5]])
                else:
                    datos_reservas_borrar.append(i)

            datos_reservas=datos_reservas_borrar 

            print("\033[31mTodas sus reservas han sido eliminadas.\033[0m")

        actualizar_datos_borrado(id_show, datos_reservas, datos_shows)

    # === BLOQUE ADMIN ===
    if admin == True: 
        opcion = borrado_reserva_menu()
        if opcion is None: 
            return
        id_show=[]


        if opcion == 1:
            while True:
                try:
                    eleccion = int(input("\033[36mSeleccione ID de reserva a eliminar:\033[0m "))
                    reserva_encontrada=None 
                    for i in datos_reservas:
                        if i[0] == eleccion:
                            reserva_encontrada = i 
                            break
                    if reserva_encontrada:
                        id_show.append([reserva_encontrada[3], reserva_encontrada[5]])
                        datos_reservas.remove(reserva_encontrada)
                        print("\033[31mLa reserva ha sido eliminada.\033[0m")
                        break
                    else:
                        print("\033[91mReserva no encontrada.\033[0m")
                        
                except ValueError:
                    print("Error de tipeo")
                except (KeyboardInterrupt, EOFError):
                    return

            actualizar_datos_borrado(id_show, datos_reservas, datos_shows)

        elif opcion == 2:
            while True:
                try:
                    eleccion = int(input("\033[36mSeleccione ID de usuario para eliminar sus reservas:\033[0m "))
                    
                    tiene_reservas = False
                    for i in datos_reservas:
                        if i[1] == eleccion:
                            tiene_reservas = True
                            break
                    
                    if not tiene_reservas:
                        print("\033[91mEse usuario no tiene reservas.\033[0m")
                        continue
                    else:
                        print("\033[96mID de usuario confirmado.\033[0m")
                        reservas_usuario_temp = []
                        for i in datos_reservas:
                            if i[1] == eleccion:
                                reservas_usuario_temp.append(i)
                        
                        print(f"\n\033[34mSe eliminarán {len(reservas_usuario_temp)} reservas.\033[0m")
                        mostrar_tabla(reservas_usuario_temp, 1)
                        
                        confirmacion=str(input("¿esta seguro? (s/n)")).lower()
                        if confirmacion=="n":
                            return
                        else:
                            break
                except ValueError:
                    print("Error de tipeo")
                except (KeyboardInterrupt, EOFError):
                    return
            
            reservas_del_id = []
            datos_finales=[]
            for i in datos_reservas:
                if i[1] == eleccion:
                    id_show.append([i[3], i[5]])
                    reservas_del_id.append(i)
                else:
                    datos_finales.append (i)

            datos_reservas=datos_finales
            print("\033[31mReservas eliminadas.\033[0m")
            
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
    if not datos_reservas:
        print("No hay reservas para editar.")
        return

    mostrar_tabla(datos_reservas, 1)
    reserva_encontrada = None
    while True:
        try:
            id_a_editar = int(input("\033[36mSeleccione el ID de reserva a editar:\033[0m "))
            for r in datos_reservas:
                if r[0] == id_a_editar:
                    reserva_encontrada = r
                    break
            if reserva_encontrada:
                break
            else:    
                print("\033[91mNo se encontró la reserva con ese ID.\033[0m")
                continue
        except ValueError:
            print("\033[91mError de tipeo.\033[0m")
        except (KeyboardInterrupt, EOFError):
            return

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
        except ValueError:
            print("Error de tipeo")
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
                print("Error de tipeo")
            except (KeyboardInterrupt, EOFError):
                return

        if ubicacion == 1:
            nueva_ubicacion = "platea"
        elif ubicacion == 2:
            nueva_ubicacion = "campo"
        elif ubicacion == 3:
            nueva_ubicacion = "vip"

        id_show = int(reserva_encontrada[3])
        show_actual = buscar_show(id_show)
        if show_actual:
            nuevo_precio = calcular_precio(show_actual, nueva_ubicacion, cantidad)
            reserva_encontrada[2] = nueva_ubicacion
            reserva_encontrada[4] = nuevo_precio
            print("\033[34mUbicación y precio actualizados correctamente.\033[0m")
        else:
            print("\033[91mEl show original parece que ya no existe.\033[0m")

    elif eleccion == 2:
        mostrar_tabla(datos_shows, 2)
        show_nuevo=None
        while True:
            try:
                nuevo_show_id = int(input("\033[36mIngrese el ID del nuevo show:\033[0m "))
                show_nuevo = buscar_show(nuevo_show_id)
                if not show_nuevo:
                    print("\033[91mEl ID ingresado no existe.\033[0m")
                    continue

                if show_nuevo == 0:
                    print("\033[91mEl ID ingresado no existe.\033[0m")
                    continue
                if show_nuevo['espacios-disponibles'] < cantidad:
                    print("\033[91mNo hay suficiente capacidad en ese show para mover la reserva.\033[0m")
                    continue
                break
            except ValueError:
                print("Error de tipeo")
            except (KeyboardInterrupt, EOFError):
                return

        for show in datos_shows:
            if show["id-show"] == int(reserva_encontrada[3]):
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