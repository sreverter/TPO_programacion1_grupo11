from datetime import datetime
from funciones.funciones_globales import *

datos_shows_js="datos/datos_shows.json"
datos_reserva_txt="datos/datos_reservas.txt"
def cambio_tipo_evento():
    try:
        tipo= input("\033[4;35mIngrese el nuevo tipo de evento: \033[0m")
        if len(tipo)>0:
            return tipo
        else:
            print("El tipo de evento no puede estar vacío.")
            return "Sin título"
    except (ValueError,KeyboardInterrupt):
        print("sus caracteres no son validos")

def cambio_duracion_evento(shows):
    suma = 0
    suma = int(shows['duracion-show'])
    while True:
        try:
            duracion = int(input("\033[35mIngresa la duración en minutos: \033[0m"))
            if duracion < 0:
                print("Debe ser un número positivo.")
                continue
            if (suma + duracion) > 720:
                print("\033[91mLa duración total supera las 12 horas del día. Consulte con un gerente.\033[0m")
                continue
            return duracion
        except (ValueError, KeyboardInterrupt):
            print("Ingrese caracteres válidos.")
            
def cambio_precio_evento():
    while True:
        try:
            precio=int(input("defina un precio para el show"))
            if precio <=0:
                eleccion=str(input("esta seleccionando una entrada gratuita\
                            esta seguro de su decision (s/n) ")).lower()
                
                if eleccion== "s":
                    return precio
                elif eleccion== "n":
                    continue

            elif precio >= 99999:
                eleccion=str(input("esta seleccionando una entrada extremadamente\
                            cara esta seguro de su decision (s/n) ")).lower()
                
                if eleccion== "s":
                    return precio
                elif eleccion== "n":
                    continue
            else:
                return precio
        except (ValueError, KeyboardInterrupt):
            print("\033[31mDebe ingresar un número válido.\033[0m")
            continue

        

def nuevo_id_show (datos_shows):
    if datos_shows==[]:
        return 1
    shows_ordenados = sorted(datos_shows, key=lambda x: x['id-show'])
    for shows in shows_ordenados:
        ultimo=shows['id-show']
    agregado=ultimo+1
    return agregado


def vista_show():
        datos = cargar_datos_json(datos_shows_js)
        dic_ordenado = sorted(datos, key=lambda x: x['fecha'])
        mostrar_tabla(dic_ordenado, 2)

def busqueda_Show():
    encontrado=False
    datos_shows = cargar_datos_json(datos_shows_js)
    lista_temp = []
    while True:
        try:
            elec = int(input("\033[35m\n1-BUSCAR POR ID\n2-BUSCAR POR FECHA:\033[0m"))
            if elec not in (1, 2):
                print("esa opción no es válida")
                continue
            elif elec in (1,2):
                break
            
        except (ValueError,KeyboardInterrupt):
            print("\033[31mOpción inválida\033[0m")
            continue

    if elec == 1:
        vista_show()
        while True:
            try:
                elec = int(input("\033[35mIngrese id: \033[0m"))
                break
            except (ValueError,KeyboardInterrupt):
                print("\033[31mOpción inválida.\033[0m")
                continue

        for i in datos_shows:
            if i['id-show'] == elec:
                lista_temp.append(i)
                encontrado=True
                break

        if encontrado==False:
            print("no se a podido encontrar el id de su show")

        elif encontrado:
            mostrar_tabla(lista_temp,2)
        
    elif elec == 2:
        vista_show()
        while True:
            try:
                año = int(input("\033[35mIngrese año: \033[0m"))
                mes = int(input("\033[35mIngrese mes: \033[0m"))
                dia = int(input("\033[35mIngrese dia: \033[0m"))
                fecha_buscada = datetime(año, mes, dia).date()
                break
            except ValueError:
                print("\033[31mFecha incorrecta intente de nuevo\033[0m")
                continue

        fecha_buscada=fecha_buscada.strftime("%Y-%m-%d")
        for i in datos_shows:
            if i['fecha'] == fecha_buscada:
                lista_temp.append(i)
                encontrado=True

        if not encontrado:
            print("no se a encontrado shows en esas fechas")
        if encontrado:
            lista_temp= sorted(lista_temp, key=lambda x: x['fecha'])
            mostrar_tabla(lista_temp,2) 

def borrado_Show():
    datos_shows=cargar_datos_json(datos_shows_js)
    datos_reserva=cargar_datos_txt(datos_reserva_txt)

    if not datos_shows:
        print("\033[31mNo hay shows registrados para eliminar\033[0m")
        return

    vista_show()

    while True:
        try:
            eleccion = int(input("\n\033[35mIngrese el ID del show que desea eliminar: \033[0m"))
            break
        except (ValueError, KeyboardInterrupt):
            print("\033[31mDebe ingresar un número válido\033[0m")
    
    show_encontrado = False
    for show in datos_shows:
        if show["id-show"] == eleccion: #test
            show_encontrado = True
            break
    
    if not show_encontrado:
        print("no se encontro el show que estaba buscando")
        return
    
    confirmar = input(f"¿Está seguro de eliminar el show con ID {eleccion}? (s/n): ").lower()
    if confirmar != "s":
        print("\033[33mOperación cancelada.\033[0m")
        return

    nuevos_shows = []
    for show in datos_shows:
        if show["id-show"] != eleccion:
            nuevos_shows.append(show)

    nuevas_reservas=[]
    for i in datos_reserva:
        id_usuario=int(i[3])
        if id_usuario != eleccion:
            nuevas_reservas.append(i)
    if len(nuevas_reservas) == len(datos_reserva):
        print("No se eliminaron reservas asociadas.")

    # Guardar shows actualizados
    inicializar_datos_json(datos_shows_js, nuevos_shows)
    inicializar_datos_txt(datos_reserva_txt, nuevas_reservas)

    print(f"\033[1;34mShow con ID {eleccion} y sus reservas asociadas fueron eliminados correctamente\033[0m")
    

def edicion_show():
    datos_shows=cargar_datos_json(datos_shows_js)
    id_encontrado = False
    while True:
        try:
            eleccion = int(input("\033[1;35mSeleccione el id del show: \033[0m"))
            for i in datos_shows:
                if i['id-show']==eleccion:
                    id_encontrado=True
            if id_encontrado==False:
                print("\033[31mID no encontrado.\033[0m")
            elif id_encontrado:
                break
        except(ValueError,KeyboardInterrupt):
            print("hubo un error porfavor ingrese un numero correcto")

    while True:
        try:
            opcion = int(input(
                    "\n\033[92m=== MENÚ DE EDICIÓN ===      \033[0m\n"
                    "\033[35m  → [0] Editar tipo de evento  \033[0m\n"
                    "\033[35m  → [1] Editar duración        \033[0m\n"
                    "\033[35m  → [2] Editar precio          \033[0m\n"
                    "\033[35m  → [3] Editar todos los datos \033[0m\n"
                    "\033[1;35mSeleccione una opción: \033[0m"
                    ))
            if opcion in (0, 1, 2, 3):
                break
            else:
                print("numero no dentro de los parametros que dimos del 0 al 2")
        except (ValueError, KeyboardInterrupt):
            print("\033[91mIngrese un caracter válido.\033[0m")

    for shows in datos_shows:
        if shows["id-show"] == eleccion:
            if opcion == 0:
                shows['nombre-show']=cambio_tipo_evento()
            elif opcion == 1:
                shows['duracion-show']=cambio_duracion_evento(shows)
            elif opcion==2:
                shows['precio']=cambio_precio_evento()
            elif opcion == 3:
                shows['nombre-show']=cambio_tipo_evento()
                shows['duracion-show']=cambio_duracion_evento(shows)
                shows['precio']=cambio_precio_evento()
            break
    inicializar_datos_json(datos_shows_js,datos_shows)

def agregar_shows():
    datos_shows=cargar_datos_json(datos_shows_js)
    id_show=nuevo_id_show(datos_shows)
    tipo_evento=cambio_tipo_evento()

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
    for show in datos_shows:
        fechas=show['fecha']
        if fechas ==str(fecha_buscada):
            lista_temp.append(show)
    
    suma_duraciones=0
    for show in lista_temp:
        duracion_show = show.get("duracion-show", 0)
        suma_duraciones += duracion_show
    
    precio = cambio_precio_evento()

    if (suma_duraciones + duracion) < 720:
        nuevo_show={
            "id-show": id_show,
            "nombre-show": tipo_evento,
            "duracion-show": duracion,
            "espectadores": espectadores,
            "espacios-disponibles": espacios_disponibles,
            "fecha": str(fecha_buscada),
            "precio": precio,
        }
        
        print("\033[1;34mShow creado con exito.\033[0m")   
        datos_shows.append(nuevo_show)
        inicializar_datos_json(datos_shows_js,datos_shows)
            
    else:
        print("\033[31mNo hay espacio en el dia para el show ingresado.\033[0m")