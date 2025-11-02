from iniciacion_listas import datos_globales_reserva, datos_globales,datos_globales_usuarios, dni_en_uso,precios_show, matriz_act
from entidades.reserva import ver_m2, id_alt_r, ver_busqueda_reserva
from entidades.usuarios import *
from entidades.shows import ver_m
from funciones.funciones_globales import *
from datetime import datetime

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
    datos = cargar_datos_txt('datos/datos_reservas.txt')
    if admin:
        #se muestra la matriz de las resrvas que hay
        mostrar_tabla(datos, 1)
        
    #muestra las reservas que hizo ese usuario exclusivamente 
    elif admin == False:
        #se limpoia la lista para que si se agrega alguna se pueda actualizar
        matriz_act.clear()
        # datos.clear()
        #se obtiene el id de usuario
        usuario_Act = obt_id_Actual()
        #se revisa que exista ese usuario en los datos de reservas y se añade a la lista
        for i in datos:
            if int(i[1]) == usuario_Act:  
                matriz_act.append(i)
        #si hay mas de una reserva te muestra la cantidad de reservas que hizo el usuario
        if len(matriz_act) > 0:
            mostrar_tabla(matriz_act, 1)
        #si no hay reservas te printea no hay reservas 
        else:
            print("no hay ninguna reserva")

def agregar_reservas(admin):
        #se genera un id aleatorio
        id_reserva = id_alt_r() 
        #si no es un admin se busca el id del usuario
        if admin == False:
            id_usuario = obt_id_Actual()
        #si es admin se genera un id aleatorio
        else:
            id_usuario = id_user()
        #se muestran todos los shows
        ver_m(datos_globales) 
        
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
                    if show <= 999 or show > 9999:
                        print("el id que ingreso no es valido")
                        continue
                    #se definen parametros booleanos para poder buscar si puede o no reservar ahi

                    show_encontrado = False
                    tiene_capacidad = False
                    indice_show = -1
                    
                    #se revisa que tenga capacidad ademas de buscar si esta en la base de shows
                    for i in range(len(datos_globales)):
                        if datos_globales[i][0] == show:
                            show_encontrado = True
                            indice_show = i  
                            if datos_globales[i][4] > 0 and datos_globales[i][4]>= num_reserva:
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
        datos_globales[indice_show][4] -= num_reserva  
        datos_globales[indice_show][3] += num_reserva

        for i in precios_show:
            if i[0] == show:
                precio_platea = i[1]*num_reserva


        for i in precios_show:
            if i[0] == show:
                    precio_campo = i[2]*num_reserva

        for i in precios_show:
            if i[0] == show:
                    precio_vip = i[3]*num_reserva
 
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
            ubicacion_e = "Platea   "
            for i in precios_show:
                if i[0] == show:
                    precio_act = i[1]*num_reserva

        elif ubicacion_u == 2:
            ubicacion_e = "Campo    "
            for i in precios_show:
                if i[0] == show:
                        precio_act = i[2]*num_reserva
        
        elif ubicacion_u == 3:
            for i in precios_show:
                ubicacion_e = "Vip       "
                if i[0] == show:
                        precio_act = i[3]*num_reserva
        print(f"\033[1;34mReserva generada con exito. El precio de su entrada termino en ${precio_act}\033[0m")
        
        #agrega los datos a la base de datos
        datos_globales_reserva.append([id_reserva, id_usuario, ubicacion_e, show, precio_act])

def busqueda_Reserva():

    #crea una lista 
    reserva_enct = []
    
    #se crea un booleano para definir cuando se encuentra
    encontrado = False

    #se le dice que es lo que puede hacer
    while True:
        try:
            eleccion = int(input("\033[35m → [1] BUSCAR RESERVA POR ID DE RESERVA\n → [2] BUSCAR RESERVA POR ID USUARIO:\033[0m"))
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
        #si lo encuentra lo añade a la lista 
        for i in datos_globales_reserva:
            if i[0] == eleccion:
                encontrado = True
                reserva_enct.append(i)
        
        #si no lo encuentra printea eso
        if not encontrado:
            print("\033[31mID de reserva no encontrada.\033[0m")
        else:
            #si lo encuentra muestra la reserva
            ver_busqueda_reserva(reserva_enct)
    
    #agarra el caso 2
    elif eleccion == 2:

        #se le indica que ponga su id de usuario
        while True:
            try:
                eleccion = int(input("\033[35mIngrese ID de usuario: \033[0m"))
                break
            except(ValueError,KeyboardInterrupt):
                print("lo ingresado es invalido")
                continue

        #si lo encuentra lo añade a la lista
        for i in datos_globales_reserva:
            if i[1] == eleccion:
                encontrado = True
                reserva_enct.append(i)
        
        #si no lo encuentra printea esto
        if not encontrado:
            print("\033[31mID de usuario no encontrado.\033[0m")
        else:

            #si lo encuentra muestra la reservas que tiene ese usuario
            ver_busqueda_reserva(reserva_enct)

def borrado_reserva(admin):
    if admin == False: 
        borrado=True
        while borrado==True:
            reservas_d_usuario = False            
            reservas_usuario = []  # lista vacía para guardar reservas del usuario
        
            # agarrar el id del usuario
            id_usuario = obt_id_Actual()

            # buscar todas las reservas del usuario
            for i in datos_globales_reserva:
                if i[1] == id_usuario:
                    reservas_d_usuario = True
                    reservas_usuario.append(i)  

            # si no hay reservas printeamos esto para sepa
            if reservas_d_usuario == False:
                print("\033[31mNo hay reservas registradas a su nombre.\033[0m")
                break
            # mostrar reservas del usuario
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
            pasa=False

            #BORRAR UNA SOLA RESERVA 
            if opcion == 1:
                try:
                    id_borrar = int(input("Ingrese el ID de la reserva que desea eliminar: "))
                    encontrada = False
                    for i in datos_globales_reserva[:]:
                        if i[1] == id_usuario and i[0] == id_borrar:
                            datos_globales_reserva.remove(i)
                            id_show.append(i[3])
                            encontrada = True
                            pasa=True
                            print(f"\033[31mReserva {id_borrar} eliminada correctamente\033[0m")
                            break
                    if not encontrada:
                        print("\033[31mNo se encontro la reserva con ese ID\033[0m")
                except (ValueError, KeyboardInterrupt):
                    print("\033[31mID inválido\033[0m")
            
            #BORRAR TODAS LAS RESERVAS
            elif opcion == 2:
                for i in datos_globales_reserva[:]:
                    if i[1] == id_usuario:
                        datos_globales_reserva.remove(i)
                        id_show.append(i[3])
                        pasa=True
                print("\033[31mTodas sus reservas han sido eliminadas\033[0m")
            if pasa:
                #Actualizar capacidad de shows
                for show_id in id_show:
                    for i in datos_globales:
                        if i[0] == show_id:
                            i[3] -= 1
                            i[4] += 1
                print("\033[34mLos datos de capacidad fueron actualizados\033[0m")
                break

    #BORRAR RESERVA
    if admin==True: 
        
        #creamos un booleano para identificar cunado encuentre el show
        show_encontrado=False
        
        #se le pide el id del show para eliminarlo
        while True:
            try:
                eleccion = int(input("\033[35mSeleccione id de reserva a eliminar: \033[0m"))
                
                #busca el show y cuenado lo encuentra el booleano se pone como true y se printea la confirmacion del id
                for i in datos_globales_reserva:
                    if i[0]==eleccion:
                        show_encontrado=True
                        print("\033[96mID de reserva confirmado.\033[0m")
                
                #si no se encuentra la reserva se printea para 
                # que sepa que esa reserva no existe o no es valida y se le pide que lo vuelva a ingresar        
                if not show_encontrado:
                    print("\033[91mEsa reserva no es valida.\033[0m")
                    continue
                else:
                    break
            except(KeyboardInterrupt,ValueError):
                print("lo ingresado se coinsidera un caracter invalido")
                continue

        #se crea otra lista vacia
        id_show = []
        
        #busca por datos globales lo copia y lo remueve de 
        #datos globales reserva y mete el dato de show en el id_show para despues facilitar la busqueda
        for i in datos_globales_reserva[:]:
            if i[0] == eleccion:
                datos_globales_reserva.remove(i)
                id_show.append(i[3])
        
        #busca en id del show el show y si lo encuentra saca un espectador y agrega un espacio
        for i in datos_globales:
            if i[0] == id_show[0]:
                i[3] -= 1
                i[4] += 1
        
        
        print("\033[1;34mReserva eliminada con exito!\033[0m")
        
def edicion_reserva():        
        #se le muestra las reservas que hay para identificar el id mas rapidamente
        ver_m2(datos_globales_reserva)

        show_encontrado=False

        while show_encontrado == False:
            #se le pide que ingrese un id
            while  True:
                try:
                    id_a_editar = int(input("\nSeleccione el ID de reserva a editar: "))
                    #busca la reserva y si la encuentra se convierte reserva encontrada en esa reserva enteramente 
                    for reserva in datos_globales_reserva:
                        if reserva[0] == id_a_editar:  
                            reserva_encontrada = reserva
                            show_encontrado=True

                    #si no lo encuentra se printe esto
                    if show_encontrado:
                        break
                    else:
                        print("\033[91mNo se encontró la reserva con ese ID.\033[0m")
                        continue
                except(ValueError, KeyboardInterrupt):
                    print("se ingreso algo que no es valido")
                    continue
        
        #se printea esto para que sepas que id estas modificando
        print(f"\nEditando reserva ID: {reserva_encontrada[0]}")
        
        #se le pide que elija una opcion de edicion
        while True:
            try:
                eleccion = int(input(
                    "\n\033[92m=== MENÚ DE EDICIÓN DE RESERVA ===\033[0m\n"
                    "\033[35m  → [1] EDITAR UBICACIÓN\033[0m\n"
                    "\033[35m  → [2] EDITAR SHOW\033[0m\n"
                    "\033[1;35mSeleccione una opción: \033[0m"
                ))
                break
            except (ValueError,KeyboardInterrupt):
                print("se ingreso un caracter no  valido")
                continue
        #EDITAR UBICACIÓN
        if eleccion == 1:
            #si elije la opcion uno se le pide que ingrese a que ubicacion quiere pasar   
            while True:
                try:
                    ubicacion = int(input(
                    "\n\033[92m=== SELECCIONE NUEVA UBICACIÓN ===\033[0m\n"
                    "\033[35m  → [1] PLATEA\033[0m\n"
                    "\033[35m  → [2] CAMPO\033[0m\n"
                    "\033[35m  → [3] VIP\033[0m\n"
                    "\033[1;35mSeleccione opción: \033[0m"
                    ))
                    while ubicacion not in (1,2,3):
                        print("el numero colocado no es el que se pidio")
                        continue
                    else:
                        break
                except (KeyboardInterrupt,ValueError):
                    print("se ingreso un numero que no esta habilitado")
                    continue
                
            #si no entra dentro de los numeros pedidos se le pide que ingrese nuevamente 
            #la ubicacion y se le indica que no es valida esa ubicacion


            
            #depende de la ubicaion se le asigna un precio correspondiente con ese show y esa ubicacion
            if ubicacion == 1:
                reserva_encontrada[2] = "Platea   "
                for precio_info in precios_show:
                    if precio_info[0] == reserva_encontrada[3]:  
                        reserva_encontrada[4] = precio_info[1]  
                
            elif ubicacion == 2:
                reserva_encontrada[2] = "Campo    "
                for precio_info in precios_show:
                    if precio_info[0] == reserva_encontrada[3]:
                        reserva_encontrada[4] = precio_info[2]  

            elif ubicacion == 3:
                reserva_encontrada[2] = "Vip       "
                for precio_info in precios_show:
                    if precio_info[0] == reserva_encontrada[3]:
                        reserva_encontrada[4] = precio_info[3]  



            print("\033[92mUbicación y precio actualizados correctamente.\033[0m")
    
        #EDITAR SHOW
        elif eleccion == 2:  
            
            #muestra todos los shows para que elijas nuevamente a que show queres ingresar para el cambio
            ver_m(datos_globales)

            #se busca el id del show y se pone un while para buscarlo
            show_valido=False
            validacion=True
            while validacion==True:
            #se le pide el id del show
                while True:
                    try:
                        nuevo_show = int(input("\nIngrese el ID del nuevo show: "))
                        break
                    except (KeyboardInterrupt,ValueError):
                        print("se ingreso algun caracter no numerico")
                        continue
            
                #busca el show y si lo encuentra pone la variable como verdadera
                for show in datos_globales:
                    if show[0] == nuevo_show:
                        show_valido = True

                #si lo encuentra lo deja pasar y printea que si encontro el show
                if show_valido:
                    print("se a encontrado el show")
                    validacion=False

                elif show_valido==False:
                    print("\033[91mEl ID de show no existe\033[0m")


            for show in datos_globales:
                #se busca si hay o no disponibilidad en el show
                if show[0] == nuevo_show and show[4] <= 0:
                    print("\033[91mNo hay capacidad disponible en ese show.\033[0m")
                
                #si lo hay se agrega una persona en los espectadores y uno menos en el espacio disponibles
                #y se le saca a el show antiguo del espectador
                elif show[0] == nuevo_show and show[4] > 0:
                    for show_viejo in datos_globales:
                        
                        #si ve que el show viejo coincide con el show de la reserva 
                        if show_viejo[0] == reserva_encontrada[3]:
                            show_viejo[4] += 1  
                            show_viejo[3] -= 1  
                    
                    show[4] -= 1  
                    show[3] += 1  
                
                    #se cambia el dato de el viejo show por el nuevo
                    reserva_encontrada[3] = nuevo_show  
                    
                    #se crea una variable que usa el strip para sacar los espacios y pasa los precios a ese otro show
                    ubicacion_actual = reserva_encontrada[2].strip()
                    print(ubicacion_actual)
                    
                    #cambia el precio basado en el show que se coloco y coordina con la ubicacion que tenia anteriormente
                    precios_cambio=0
                    while precios_cambio==0:
                        for precios in  precios_show:
                            if precios[0]==nuevo_show:
                                if ubicacion_actual=="platea":
                                    precios_cambio=precios[1]
                                elif ubicacion_actual=="campo":
                                    precios_cambio=precios[2]
                                elif ubicacion_actual=="vip":
                                    precios_cambio=precios[3]

                    #se cambia el precio por el del show en teoria
                    reserva_encontrada[4]=precios_cambio                  

                    print("\033[92mShow actualizado correctamente.\033[0m")