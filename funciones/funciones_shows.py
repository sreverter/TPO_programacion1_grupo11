from datetime import datetime
from funciones.funciones_globales import *
from entidades.shows import *

datos_shows_js = "datos/datos_shows.json"
datos_reserva_txt = "datos/datos_reservas.txt"

def vista_show():
    try:
        datos = cargar_datos_json(datos_shows_js)
    except OSError:
        print("\033[91mNo se pudo acceder al archivo de shows.\033[0m")
        return

    if not datos:
        print("\033[91mNo hay shows cargados.\033[0m")
        return
    try:
        dic_ordenado = sorted(datos, key=lambda x: x['fecha'])
    except KeyError:
        print("\033[91mError en el formato de los datos de fecha.\033[0m")
        return
            
    mostrar_tabla(dic_ordenado, 2)

def busqueda_Show():
    encontrado = False
    datos_shows = cargar_datos_json(datos_shows_js)
    lista_temp = []
    while True:
        try:
            elec = int(input("\033[36m\n1 - Buscar por ID\n2 - Buscar por fecha:\033[0m "))
            if elec not in (1, 2):
                print("\033[91mOpción no válida.\033[0m")
                continue
            else:
                break
        except ValueError:
            print("\033[91mEntrada inválida.\033[0m")
        except (KeyboardInterrupt, EOFError):
            return

    if elec == 1:
        vista_show()
        while True:
            try:
                elec = int(input("\033[36mIngrese ID:\033[0m "))
                break
            except ValueError:
                print("\033[91mEntrada inválida.\033[0m")
            except (KeyboardInterrupt, EOFError):
                return
            
        for i in datos_shows:
            if i['id-show'] == elec:
                lista_temp.append(i)
                encontrado = True
                break

        if not encontrado:
            print("\033[91mNo se ha podido encontrar el ID del show.\033[0m")
        else:
            mostrar_tabla(lista_temp, 2)

    elif elec == 2:
        vista_show()
        while True:
            try:
                año = int(input("\033[36mIngrese año:\033[0m "))
                mes = int(input("\033[36mIngrese mes:\033[0m "))
                dia = int(input("\033[36mIngrese día:\033[0m "))
                fecha_buscada = datetime(año, mes, dia).date()
                break
            except ValueError:
                print("\033[91mEntrada inválida.\033[0m")
            except (KeyboardInterrupt, EOFError):
                return
            
        fecha_buscada = fecha_buscada.strftime("%Y-%m-%d")
        for i in datos_shows:
            if i['fecha'] == fecha_buscada:
                lista_temp.append(i)
                encontrado = True

        if not encontrado:
            print("\033[91mNo se han encontrado shows en esa fecha.\033[0m")
        else:
            lista_temp = sorted(lista_temp, key=lambda x: x['fecha'])
            mostrar_tabla(lista_temp, 2)

def borrado_Show():
    try:
        datos_shows = cargar_datos_json(datos_shows_js)
        datos_reserva = cargar_datos_txt(datos_reserva_txt)
    except OSError:
        print("\033[91mNo se pudo acceder a los archivos.\033[0m")
        return

    if not datos_shows:
        print("\033[91mNo hay shows registrados para eliminar.\033[0m")
        return

    vista_show()

    while True:
        try:
            eleccion = int(input("\n\033[36mIngrese el ID del show que desea eliminar:\033[0m "))
            break
        except ValueError:
            print("\033[91mEntrada inválida.\033[0m")
        except (KeyboardInterrupt, EOFError):
            return
        
    show_encontrado = False
    for show in datos_shows:
        if show["id-show"] == eleccion:
            show_encontrado = True
            break

    if not show_encontrado:
        print("\033[91mNo se encontró el show especificado.\033[0m")
        return

    confirmar = input(f"\033[36m¿Está seguro de eliminar el show con ID {eleccion}? (s/n):\033[0m ").lower()
    if confirmar != "s":
        print("\033[33mOperación cancelada.\033[0m")
        return

    nuevos_shows = []
    for show in datos_shows:
        if show["id-show"] != eleccion:
            nuevos_shows.append(show)

    nuevas_reservas=[]
    for i in datos_reserva:
        try:
            id_usuario = int(i[3])
        except (ValueError, IndexError):
            continue
        if id_usuario != eleccion:
            nuevas_reservas.append(i)
    if len(nuevas_reservas) == len(datos_reserva):
        print("\033[33mNo se eliminaron reservas asociadas.\033[0m")

    inicializar_datos_json(datos_shows_js, nuevos_shows)
    inicializar_datos_txt(datos_reserva_txt, nuevas_reservas)

    print(f"\033[34mShow con ID {eleccion} y sus reservas asociadas fueron eliminados correctamente.\033[0m")

def edicion_show():
    datos_shows = cargar_datos_json(datos_shows_js)
    id_encontrado = False
    while True:
        try:
            eleccion = int(input("\033[36mSeleccione el ID del show:\033[0m "))
            for i in datos_shows:
                if i['id-show'] == eleccion:
                    id_encontrado = True
            if not id_encontrado:
                print("\033[91mID no encontrado.\033[0m")
            else:
                break
        except ValueError:
            print("\033[91mEntrada inválida.\033[0m")
        except (KeyboardInterrupt, EOFError):
            return
    while True:
        try:
            opcion = int(input(
                "\n\033[92m=== MENÚ DE EDICIÓN ===\033[0m\n"
                "\033[36m  → [0] Editar tipo de evento\033[0m\n"
                "\033[36m  → [1] Editar duración\033[0m\n"
                "\033[36m  → [2] Editar precio\033[0m\n"
                "\033[36m  → [3] Editar todos los datos\033[0m\n"
                "\033[36mSeleccione una opción:\033[0m "
            ))
            if opcion in (0, 1, 2, 3):
                break
            else:
                print("\033[91mNúmero fuera del rango permitido.\033[0m")
        except ValueError:
            print("\033[91mEntrada inválida.\033[0m")
        except (KeyboardInterrupt, EOFError):
            return
    cambio=False
    for shows in datos_shows:
        if shows["id-show"] == eleccion:
            if opcion == 0:
                shows['nombre-show'] = cambio_tipo_evento()
                cambio=True
            elif opcion == 1:
                shows = cambio_duracion_evento(shows)
                if shows == None:
                    continue
                shows['duracion-show']=shows
                cambio=True 
            elif opcion == 2:
                shows['precio'] = cambio_precio_evento()
                cambio=True
            elif opcion == 3:
                shows['nombre-show'] = cambio_tipo_evento()
                shows = cambio_duracion_evento(shows)
                if shows == None:
                    continue
                shows['duracion-show']=shows 
                shows['precio'] = cambio_precio_evento()
                cambio=True
            break
    if cambio:
        inicializar_datos_json(datos_shows_js, datos_shows)
        print("\033[34mShow editado correctamente.\033[0m")

def agregar_shows():
    datos_shows = cargar_datos_json(datos_shows_js)
    id_show = nuevo_id_show(datos_shows)
    tipo_evento = cambio_tipo_evento()

    while True:
        try:
            duracion = int(input("\033[36mIngrese la cantidad de minutos:\033[0m "))
            if duracion > 0 and duracion < 720:
                break
            else:
                print("\033[91mDebe ser un número positivo menor a 720.\033[0m")
        except ValueError:
            print("\033[91mEntrada inválida.\033[0m")
            continue
        except (KeyboardInterrupt, EOFError):
            return

    espectadores = 0
    espacios_disponibles = 999

    while True:
        try:
            año = int(input("\033[36mIngrese año:\033[0m "))
            mes = int(input("\033[36mIngrese mes:\033[0m "))
            dia = int(input("\033[36mIngrese día:\033[0m "))
            fecha_buscada = datetime(año, mes, dia).date()
            break
        except ValueError:
            print("\033[91mEntrada inválida.\033[0m")
            continue
        except (KeyboardInterrupt, EOFError):
            return
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
        nuevo_show = {
            "id-show": id_show,
            "nombre-show": tipo_evento,
            "duracion-show": duracion,
            "espectadores": espectadores,
            "espacios-disponibles": espacios_disponibles,
            "fecha": str(fecha_buscada),
            "precio": precio
        }
        print("\033[34mShow creado con éxito.\033[0m")
        datos_shows.append(nuevo_show)
        inicializar_datos_json(datos_shows_js, datos_shows)
    else:
        print("\033[91mNo hay espacio disponible ese día para agregar el show.\033[0m")
