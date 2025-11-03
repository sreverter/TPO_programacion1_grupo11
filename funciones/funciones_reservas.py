from iniciacion_listas import dni_en_uso
from entidades.reserva import id_alt_r 
from entidades.usuarios import *
from funciones.funciones_globales import *

#region por hacer
#hacer un modulo de colores o un diccionario con ellos
#ver la funcion de borrado y si queremos que se eliminen todas las reservas o solo las que decida ese usuario borrar
#en el caso de la segunda hace falrta validaciones sobre si la reserva es de el y asi
colordorado="\033[38;2;207;181;59m"


#se agarra el id del usuario comparandolo con el dni que esta en uso
def obt_id_Actual():
    #se agarra el dni en uso y se pone en otra variable
    dni_act = (dni_en_uso[0])
    #se crea una lista que es donde va a ir el usuario de ese dni
    user_act = []
    #se añade el id de ese usuario
    datos_usuario = cargar_datos_json('datos/datos_usuarios.json')
    for i in datos_usuario:
        if i["dni"] == dni_act:
            user_act.append(i["id"])
    return user_act[0]

def vista_reserva(admin):
    #se separa la vista de el admin y el no admin para diferenciar que es lo que pueden o no ver  
    vista=[]
    datos = cargar_datos_txt('datos/datos_reservas.txt')
    if admin:
        #se muestra la matriz de las resrvas que hay
        mostrar_tabla(datos, 1)
        
    #muestra las reservas que hizo ese usuario exclusivamente 
    elif admin == False:
        #se obtiene el id de usuario
        usuario_Act = obt_id_Actual()
        #se revisa que exista ese usuario en los datos de reservas y se añade a la lista
        for i in datos:
            if int(i[1]) == usuario_Act:  
                vista.append(i)
        #si hay mas de una reserva te muestra la cantidad de reservas que hizo el usuario
        if len(vista) > 0:
            mostrar_tabla(vista, 1)
        #si no hay reservas te printea no hay reservas 
        else:
            print("no hay ninguna reserva")

def agregar_reservas(admin):
        datos_shows = cargar_datos_json('datos/datos_shows.json')
        #se genera un id aleatorio
        id_reserva = id_alt_r() 
        #si no es un admin se busca el id del usuario
        if admin == False:
            id_usuario = obt_id_Actual()
        #si es admin se genera un id aleatorio
        else:
            id_usuario = id_user()
        #se muestran todos los shows
        mostrar_tabla(datos_shows, 2) 
        
        busqueda = True
        while busqueda:
            while True:
                try:
                    #se pide un id para ver si puede o no entrar en ese show
                    num_reserva = int(input("\033[35m¿Cuántas reservas desea hacer? \033[0m"))
                    if num_reserva <= 0:
                        print("el numero que ingreso no es valido")
                        continue
                    show = int(input("\033[35mIngrese el numero de id del show que desea asistir: \033[0m"))
                    show_encontrado = False
                    tiene_capacidad = False
                    
                    #se revisa que tenga capacidad ademas de buscar si esta en la base de shows
                    for i in datos_shows:
                        if i["id-show"] == show:
                            show_encontrado = True
                            if i["espacios-disponibles"] > 0 and i["espacios-disponibles"] >= num_reserva:
                                tiene_capacidad = True
                    
                    #se printea una cosa o la otra dependiendo de si no lo encuentra o no tiene capacidad
                    if not show_encontrado:
                        print("\033[31mEl id ingresado no existe, por favor ingrese un id valido.\033[0m")
                        continue
                    elif not tiene_capacidad:
                        print("\033[31mEste show no tiene capacidad disponible.\033[0m")
                        continue
                    else:
                        #se para la busqueda
                        busqueda = False
                        break
                except (ValueError, KeyboardInterrupt):
                    print("el id que selecciono parece tener errores de caracteres")
                    continue

        #se suma y resta los espectadores y los espacios disponibles 
        for i in datos_shows:
            if i["id-show"] == show:
                i["espacios-disponibles"] -= num_reserva
                i["espectadores"] += num_reserva

        for i in datos_shows:
            if i["id-show"] == show:
                lol = i["precio"]*num_reserva
                precio_platea = lol
                precio_campo = lol*2
                precio_vip = lol*3

        while True:
            try:
                ubicacion_u = int(input(
                "\n\033[92m=============  MENU DE UBICACIONES  =============\033[0m\n"
                f"\n\033[35m  → [1] El costo de platea es de {precio_platea}\033[0m\n"
                f"\n\033[35m  → [2] El costo de campo es de {precio_campo}\033[0m\n"
                f"\n\033[35m{colordorado}  → [3] El costo de VIP es de {precio_vip}\033[0m\n"
                "\n\033[92m================================================\033[0m\n"   
                "\n\033[35mElegi tipo de ubicación: \033[0m"))
                #validacion de is puso o no un numero correcto
                if ubicacion_u not in(1,2,3):
                    print("su numero no fue ninguno dado asegurese de que sea mayor a 0 y menor a 3")
                    continue
                else:
                    break
            except (ValueError,KeyboardInterrupt):
                print("lo que puso no esta dentro de los parametros esperados porfavor vuelva a intentarlo")
                continue


        #determina el precio basado en el show y el precio de dicho show
        if ubicacion_u == 1:
            precio_act = precio_platea
            sector = "platea"

        elif ubicacion_u == 2:
            precio_act = precio_campo
            sector = "campo"
        
        elif ubicacion_u == 3:
            precio_act = precio_vip
            sector = "vip"

        print(f"\033[1;34mReserva generada con exito. El precio de su entrada termino en ${precio_act}\033[0m")
        
        datos_reservas = cargar_datos_txt('datos/datos_reservas.txt')
        nueva_reserva = [id_reserva, id_usuario, sector, show, precio_act, num_reserva]
        datos_reservas.append(nueva_reserva)
        print(datos_reservas)
        inicializar_datos_txt('datos/datos_reservas.txt', datos_reservas)


def busqueda_Reserva():
    datos=cargar_datos_txt('datos/datos_reservas.txt')
    #crea una lista 
    reserva_enct = []
    
    #se crea un booleano para definir cuando se encuentra
    encontrado = False

    #se le dice que es lo que puede hacer
    while True:
        try:
            eleccion = int(input("\033[35m → [1] BUSCAR RESERVA POR ID DE RESERVA\n → [2] BUSCAR RESERVA POR ID USUARIO:\033[0m"))
            if eleccion in (1,2):
                break
        except (ValueError,KeyboardInterrupt):
            print("se ha detectado un error porfavor vuelva a intentarlo")
            continue
    
    #agarra el caso numero 1
    if eleccion == 1:
        while True:
            try:    
                eleccion = int(input("\033[35mIngrese id de reserva: \033[0m"))
                break
            except(KeyboardInterrupt,ValueError):
                print("el numero ingresado no es valido")
                continue
        for i in datos:
            if i[0] == eleccion:
                encontrado = True
                reserva_enct.append(i)
        
        if not encontrado:
            print("\033[31mID de reserva no encontrada.\033[0m")
        else:
            mostrar_tabla(reserva_enct,1)

    elif eleccion == 2:

        while True:
            try:
                eleccion = int(input("\033[35mIngrese ID de usuario: \033[0m"))
                break
            except(ValueError,KeyboardInterrupt):
                print("lo ingresado es invalido")
                continue

        #si lo encuentra lo añade a la lista
        for i in datos:
            if i[1] == eleccion:
                encontrado = True
                reserva_enct.append(i)
        
        #si no lo encuentra printea esto
        if not encontrado:
            print("\033[31mID de usuario no encontrado.\033[0m")
        else:
            mostrar_tabla(reserva_enct,1)

def borrado_reserva(admin):
    datos_reservas = cargar_datos_txt('datos/datos_reservas.txt')
    datos_shows = cargar_datos_json('datos/datos_shows.json')
    #reaparti por bloques porque ya me estaba mareando
    # === BLOQUE USUARIO NORMAL ===
    if admin == False: 
        borrado = True
        while borrado:
            reservas_d_usuario = False            
            reservas_usuario = []
        
            id_usuario = obt_id_Actual()

            for i in datos_reservas:
                if i[1] == id_usuario:
                    reservas_d_usuario = True
                    reservas_usuario.append(i)  

            if reservas_d_usuario == False:
                print("\033[31mNo hay reservas registradas a su nombre.\033[0m")
                break

            print("\n\033[34mTus reservas actuales:\033[0m")
            print(f"{'ID Reserva':<12} {'ID Show':<10} {'Ubicación':<12} {'Precio':<8}")
            print("-" * 45)
            for r in reservas_usuario:
                print(f"{r[0]:<12} {r[3]:<10} {r[2]:<12} {r[4]:<8}")
            
            while True:
                try:
                    opcion = int(input("\n\033[35m¿Qué desea hacer?\033[0m\n"
                                        "1 - Borrar una sola reserva\n"
                                        "2 - Borrar todas las reservas\n"
                                        "\033[36mSeleccione una opción: \033[0m"))
                    if opcion in (1, 2):
                        break
                    else:
                        print("Debe ser un número entre 1 y 2.")
                except (ValueError, KeyboardInterrupt):
                    print("Ingrese un valor válido.")

            id_show = []

            # === BORRAR UNA SOLA RESERVA ===
            if opcion == 1:
                try:
                    id_borrar = int(input("Ingrese el ID de la reserva que desea eliminar: "))
                    encontrada = False
                    for i in datos_reservas:
                        if i[1] == id_usuario and i[0] == id_borrar:
                            id_show.append([i[3], i[5]])
                            datos_reservas.remove(i)
                            encontrada = True
                            print(f"\033[31mReserva {id_borrar} eliminada correctamente\033[0m")
                            break
                    if not encontrada:
                        print("\033[31mNo se encontró la reserva con ese ID\033[0m")
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
                print("\033[31mTodas sus reservas han sido eliminadas\033[0m")
                borrado = False
    
            # === ACTUALIZAR CAPACIDAD ===
            for show_id, cantidad in id_show:
                for show in datos_shows:
                    if show["id-show"] == show_id:
                        show["espacios-disponibles"] += cantidad
                        show["espectadores"] -= cantidad

            print("\033[34mLos datos de capacidad fueron actualizados\033[0m")
                
            inicializar_datos_txt('datos/datos_reservas.txt', datos_reservas)
            inicializar_datos_json('datos/datos_shows.json', datos_shows)

    # === BLOQUE ADMIN ===
    if admin == True: 
        reservas_usuario = []
        reservas_d_usuario = False
        reservas_del_id = []
        show_encontrado = False
        
        while True:
            try:
                opcion = int(input("\n\033[35m¿Qué desea hacer?\033[0m\n"
                                    "1 - Borrar una sola reserva del usuario\n"
                                    "2 - Borrar todas las reservas del usuario\n"
                                    "\033[36mSeleccione una opción: \033[0m"))
                if opcion in (1, 2):
                    break
                else:
                    print("Debe ser un número entre 1 y 2.")
            except (ValueError, KeyboardInterrupt):
                print("Ingrese un valor válido.")

        if opcion == 1:
            while True:
                try:
                    eleccion = int(input("\033[35mSeleccione id de reserva a eliminar: \033[0m"))
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
                    print("Lo ingresado se considera un carácter inválido")
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
            
            
            for show_id, cantidad in id_show:
                for show in datos_shows:
                    if show["id-show"] == show_id:
                        show["espacios-disponibles"] += cantidad
                        show["espectadores"] -= cantidad

            print("\033[1;34mReserva eliminada con éxito!\033[0m")

            
            inicializar_datos_txt('datos/datos_reservas.txt', datos_reservas)
            inicializar_datos_json('datos/datos_shows.json', datos_shows)

        if opcion == 2:                   
            while True:
                try:
                    eleccion = int(input("\033[35mSeleccione id de usuario para eliminar sus reservas: \033[0m"))
                    show_encontrado = False
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
                    print("Lo ingresado se considera un carácter inválido")
                    continue

            reservas_del_id = []
            for i in datos_reservas:
                if i[1] == eleccion:
                    reservas_usuario.append(i)  
                    reservas_del_id.append(i)

            print("\n\033[34mLas reservas del usuario:\033[0m")
            print(f"{'ID Reserva':<12} {'ID Show':<10} {'Ubicación':<12} {'Precio':<8} {'Cant reservas':<8}")
            print("-" * 55)
            for r in reservas_del_id:
                print(f"{r[0]:<12} {r[3]:<10} {r[2]:<12} {r[4]:<8} {r[5]}")

            datos_reservas_borrar = []
            id_show = []
            for i in datos_reservas:
                if i[1] == eleccion:
                    datos_reservas_borrar.append(i)
                    id_show.append([i[3], i[5]])
            for i in datos_reservas_borrar:
                datos_reservas.remove(i)

            print("\033[31mTodas sus reservas han sido eliminadas\033[0m")
    
            for show_id, cantidad in id_show:
                for show in datos_shows:
                    if show["id-show"] == show_id:
                        show["espacios-disponibles"] += cantidad
                        show["espectadores"] -= cantidad

            print("\033[34mLos datos de capacidad fueron actualizados\033[0m")
            
            inicializar_datos_txt('datos/datos_reservas.txt', datos_reservas)
            inicializar_datos_json('datos/datos_shows.json', datos_shows)

                
def buscar_show(id_show):
    datos_shows = cargar_datos_json("datos/datos_shows.json")
    for s in datos_shows:
        if int(s['id-show']) == int(id_show):
            return s
    return 0

def calcular_precio(show, ubicacion, cantidad):
    base = int(show['precio'])
    if ubicacion == 'platea':
        return base * cantidad
    elif ubicacion == 'campo':
        return base * 2 * cantidad
    elif ubicacion == 'vip':
        return base * 3 * cantidad
    else:
        return base * cantidad

def edicion_reserva():        
    datos_reservas = cargar_datos_txt('datos/datos_reservas.txt')
    datos_shows = cargar_datos_json("datos/datos_shows.json")
    mostrar_tabla(datos_reservas, 1)
    show_encontrado = False
    while not show_encontrado:
        try:    
            id_a_editar = int(input("\nSeleccione el ID de reserva a editar: "))
            for r in datos_reservas:
                if r[0] == id_a_editar:  
                    reserva_encontrada = r
                    show_encontrado = True
                    break
            if not show_encontrado:
                print("\033[91mNo se encontró la reserva con ese ID.\033[0m")
                continue
        except (ValueError, KeyboardInterrupt):
            print("se ingresó algo que no es válido")
            continue
        cantidad = int(reserva_encontrada[5])
    print(f"\nEditando reserva ID: {reserva_encontrada[0]}")
    while True:
        try:
            eleccion = int(input(
                "\n\033[92m=== MENÚ DE EDICIÓN DE RESERVA ===\033[0m\n"
                "\033[35m  → [1] EDITAR UBICACIÓN\033[0m\n"
                "\033[35m  → [2] EDITAR SHOW\033[0m\n"
                "\033[1;35mSeleccione una opción: \033[0m"
            ))
            if eleccion in (1, 2):
                break
            print("Opción inválida.")
        except (ValueError, KeyboardInterrupt):
            print("se ingresó un carácter no válido")
    if eleccion == 1:
        while True:
            try:
                ubicacion = int(input(
                "\n\033[92m=== SELECCIONE NUEVA UBICACIÓN ===\033[0m\n"
                "\033[35m  → [1] PLATEA\033[0m\n"
                "\033[35m  → [2] CAMPO\033[0m\n"
                "\033[35m  → [3] VIP\033[0m\n"
                "\033[1;35mSeleccione opción: \033[0m"
                ))
                if ubicacion in (1, 2, 3):
                    break
                print("Debe ser un número entre 1 y 3")
            except (ValueError, KeyboardInterrupt):
                print("Ingrese un número válido")
        ubicaciones = {1: "platea", 2: "campo", 3: "vip"}
        nueva_ubicacion = ubicaciones[ubicacion]
        id_show=int(reserva_encontrada[3])

        show_actual = buscar_show(id_show)
        nuevo_precio = calcular_precio(show_actual, nueva_ubicacion, cantidad)
        
        reserva_encontrada[2] = nueva_ubicacion
        reserva_encontrada[4] = nuevo_precio
        
        print("\033[92mUbicación y precio actualizados correctamente.\033[0m")
    elif eleccion == 2:  
        mostrar_tabla(datos_shows)
        while True:
            try:
                nuevo_show_id = int(input("\nIngrese el ID del nuevo show: "))
                show_nuevo = buscar_show(nuevo_show_id)
                if show_nuevo == 0:
                    print("\033[91mEl ID ingresado no existe.\033[0m")
                    continue
                if show_nuevo['espacios-disponibles'] <= 0:
                    print("\033[91mNo hay capacidad disponible en ese show.\033[0m")
                    continue
                break
            except (ValueError, KeyboardInterrupt):
                print("Ingrese un valor numérico válido.")
        show_viejo = buscar_show(reserva_encontrada[3])
        if show_viejo:
            show_viejo['espacios-disponibles'] += cantidad
            show_viejo['espectadores'] -= cantidad
        
        show_nuevo['espacios-disponibles'] -= cantidad
        show_nuevo['espectadores'] += cantidad
        
        nueva_ubic = reserva_encontrada[2]
        nuevo_precio = calcular_precio(show_nuevo, nueva_ubic, cantidad)
        
        reserva_encontrada[3] = nuevo_show_id
        reserva_encontrada[4] = nuevo_precio
        
        print("\033[92mShow actualizado correctamente.\033[0m")
    inicializar_datos_txt('datos/datos_reservas.txt', datos_reservas)
    inicializar_datos_json('datos/datos_shows.json', datos_shows)
    print("\033[96mCambios guardados exitosamente.\033[0m")
