from iniciacion_listas import datos_globales, datos_globales_reserva, solo_ids_show,precios_show
from entidades.shows import ver_m, id_alt
from datetime import datetime
import random

#region tareas
#colorear y testear todo un par de veces
#testeado en modo admin una vez casi todo si no es que todo tiene validaciones previas para evitar errores falta colorear

def vista_show():
        matriz_ordenada = sorted(datos_globales, key=lambda x: x[5])
        ver_m(matriz_ordenada)

def busqueda_Show():
    while True:
        try:
            elec = int(input("\033[35m\n1-BUSCAR POR ID\n2-BUSCAR POR FECHA:\033[0m"))
        except ValueError:
            print("\033[31mOpción inválida.\033[0m")
            continue
        if elec == 1:
            lista_temp = []
            while True:
                try:
                    elec = int(input("\033[35mIngrese id: \033[0m"))
                    break
                except ValueError:
                    print("\033[31mOpción inválida.\033[0m")
                    continue

            
            for i in datos_globales:
                if i[0] == elec:
                    lista_temp.append(i)

            if len(lista_temp) > 0:
                ver_m(lista_temp) 
                break
            else:
                print("\033[31mNo coincide con ningún id.\033[0m")



        elif elec == 2:
            while True:
                try:
                    año = int(input("\033[35mIngrese año: \033[0m"))
                    mes = int(input("\033[35mIngrese mes: \033[0m"))
                    dia = int(input("\033[35mIngrese dia: \033[0m"))
                    fecha_buscada = datetime(año, mes, dia).date()
                    break
                except ValueError:
                    print("\033[31mFecha incorrecta intente de nuevo.\033[0m")

            lista_temp = []

            for i in datos_globales:
                if i[5] == fecha_buscada:
                    lista_temp.append(i)


            if len(lista_temp) > 0:
                ver_m(lista_temp) 
                break
            else:
                print("\033[31mNo hay fechas disponibles.\033[0m")

        else:
            print("opcion invalida")

def borrado_Show():
      menu = True

      while menu == True:
        matriz_ordenada = sorted(datos_globales, key=lambda x: x[5])
        ver_m(matriz_ordenada)
        while True:
            try:
                eleccion = int(input("Ingrese ID del show: "))
                if eleccion not in solo_ids_show:
                    salida_Emer = int(input("El ID ingresado no se encuentra. Ingrese -1 para salir o cualquier otro número para intentar de nuevo: "))
                    if salida_Emer ==-1:
                        menu=False
                        print("Volviendo al menu principal")
                        break
                    continue
                break
            except ValueError:
                print("\033[31mID inválido.\033[0m")
                continue
            
        
        # Borrar el show
        for s in datos_globales[:]:
            if s[0] == eleccion:
                datos_globales.remove(s)

        # Borrar todas las reservas asociadas
        for r in datos_globales_reserva[:]:
            if r[3] == eleccion:
                datos_globales_reserva.remove(r)

        # Borrar todas las reservas asociadas
        for p in precios_show[:]:
            if p[0] == eleccion:
                precios_show.remove(p)

        # Actualizar lista de ids de shows
        solo_ids_show.clear()
        for s in datos_globales:
            solo_ids_show.append(s[0])

        print("Show eliminado")
        menu=False

def edicion_show():
    show_encontrado=None
    id_encontrado = False
    while True:
        try:
            eleccion = int(input("\033[1;35mSeleccione el id del show: \033[0m"))
            for i in datos_globales:
                if eleccion==i[0]:
                    id_encontrado=True
                    show_encontrado=i
            if show_encontrado is None:
                print("\033[31mID no encontrado.\033[0m")
            elif id_encontrado:
                break
        except(ValueError,KeyboardInterrupt):
            print("hubo un error porfavor ingrese un numero correcto")

    if id_encontrado and show_encontrado:
        while True:
            try:
                opcion = int(input(
                        "\n\033[92m=== MENÚ DE EDICIÓN ===      \033[0m\n"
                        "\033[35m  → [0] Editar tipo de evento  \033[0m\n"
                        "\033[35m  → [1] Editar duración        \033[0m\n"
                        "\033[35m  → [2] Editar todos los datos \033[0m\n"
                        "\033[1;35mSeleccione una opción: \033[0m"
                        ))
                if opcion in (0, 1, 2):
                    break
                else:
                    print("numero no dentro de los parametros que dimos del 0 al 2")
            except (ValueError, KeyboardInterrupt):
                print("\033[91mIngrese un caracter válido.\033[0m")

        if opcion == 0:
            try:
                tipo= input("\033[4;35mIngrese el nuevo tipo de evento: \033[0m")
                if len(tipo)>0:
                    show_encontrado[1]=tipo 
                    show_encontrado[1]=show_encontrado[1].ljust(20, " ")
                else:
                    print("el tipo de evento no puede estar vacio")
            except (ValueError,KeyboardInterrupt):
                print("sus caracteres no son validos")
        elif opcion == 1:
            fecha = show_encontrado[5]
            suma = 0

            for u in datos_globales:
                if u[5] == fecha and u[0] !=show_encontrado[0]:
                    suma +=u[2]

            try:
                    duracion = int(input("\033[35mIngresa la duracion de minutos: \033[0m"))
                    while duracion <0:
                        print("tiene que ser un numero positivo")
                        duracion = int(input("\033[35mIngrese la cantidad de minutos: \033[0m"))
                        continue
                    while (suma + duracion) > 720:
                        print("\033[91mIngrese un número válido.\033[0m")
                        duracion = int(input("\033[35mIngresa la cantidad de minutos: \033[0m"))
                    show_encontrado[2] = duracion
            except (ValueError, KeyboardInterrupt):
                print("ingrese caracteres validos")

        elif opcion == 2:
            try:
                tipo= input("\033[4;35mIngrese el nuevo tipo de evento: \033[0m")
                if len(tipo)>0:
                    show_encontrado[1]=tipo 
                    show_encontrado[1]=show_encontrado[1].ljust(20, " ")
                else:
                    print("el tipo de evento no puede estar vacio")
            except (ValueError,KeyboardInterrupt):
                print("sus caracteres no son validos")
            show_encontrado[1]=show_encontrado[1].ljust(20, " ")
            fecha = show_encontrado[5]

            suma = 0

            for u in datos_globales:
                if u[5] == fecha and u[0]!= show_encontrado[0]:
                    suma +=u[2]
            try:
                if suma < 720:
                    duracion = int(input("\033[35mIngrese la cantidad de minutos: \033[0m"))
                    while duracion <0:
                        print("tiene que ser un numero positivo")
                        duracion = int(input("\033[35mIngrese la cantidad de minutos: \033[0m"))
                        continue
                    while (suma + duracion) >= 720:
                        print("\033[31mExceso de minutos en el dia, ingrese un valor menor.\033[0m")
                        duracion = int(input("\033[35mIngrese la cantidad de minutos: \033[0m"))
                    show_encontrado[2] = duracion
            except (ValueError, KeyboardInterrupt):
                    print("\033[31mDebe ingresar un número válido.\033[0m")


def agregar_shows():

        id_show = id_alt()

        tipo_Evento = input("\033[35mIngrese el tipo de evento: \033[0m")
        tipo_Evento=tipo_Evento.ljust(20, " ")
        while True:
            try:
                duracion = int(input("\033[35mIngrese la cantidad de minutos: \033[0m"))
                if duracion > 0 and duracion < 720:
                    break  
                else:
                    print("Error: Tiene que ser un número positivo y menor a 720 minutos")
            except (ValueError, KeyboardInterrupt):
                print("\033[31mDebe ingresar un número válido.\033[0m")
                continue

        espectadores = 0

        espacios_disponibles = 999
        while True:
            try:
                año = int(input("\033[35mIngrese año: \033[0m"))
                mes = int(input("\033[35mIngrese mes: \033[0m"))
                dia = int(input("\033[35mIngrese dia: \033[0m"))
                fecha_buscada = datetime(año, mes, dia).date()
                break
            except (ValueError,KeyboardInterrupt):
                print("\033[31mFecha incorrecta intente de nuevo.\033[0m")

        lista_temp = []

        for i in datos_globales:
            if i[5] == fecha_buscada:
                lista_temp.append(i)

        suma = 0
        columna = 2
        for f in lista_temp:
            suma += f[columna]
        
        if (suma + duracion) < 720:

            datos_globales.append([id_show,tipo_Evento,duracion,espectadores,espacios_disponibles,fecha_buscada])

            id_Act = id_show
            precio_b = random.randint(7200,12000)
            precio_b2 = precio_b * 2
            precio_b3 = precio_b * 3
            precios_show.append([id_Act,precio_b,precio_b2,precio_b3])
            

            print("\033[1;34mShow creado con exito.\033[0m")   
             
        else:
            print("\033[31mNo hay espacio en el dia para el show ingresado.\033[0m")