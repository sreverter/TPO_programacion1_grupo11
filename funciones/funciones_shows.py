from datetime import datetime
from funciones.funciones_globales import *
from entidades.shows import *

datos_shows_js = "datos/datos_shows.json"
datos_reserva_txt = "datos/datos_reservas.txt"

def vista_show():
    datos = cargar_datos_json(datos_shows_js)
    if not datos:
            print("\033[91mNo hay shows registrados.\033[0m")
            return
    dic_ordenado = sorted(datos, key=lambda x: x['fecha'])
    mostrar_tabla(dic_ordenado, 2)

def busqueda_Show():
    datos_shows = cargar_datos_json(datos_shows_js)
    if not datos_shows:
        print("No hay shows.")
        return
    while True:
        try:
            elec = int(input("\033[36m\n1 - Buscar por ID\n2 - Buscar por fecha:\033[0m "))
            if elec not in (1, 2):
                print("\033[91mOpción no válida.\033[0m")
            break
        except ValueError:
            print("\033[91mError de tipeo.\033[0m")
        except (KeyboardInterrupt, EOFError):
            return
    
    lista_temp = []
    if elec == 1:
        vista_show()
        while True:
            try:
                id_show = int(input("\033[36mIngrese ID:\033[0m "))
                break
            except ValueError:
                print("\033[91mDebe ingresar un número válido.\033[0m")
            except (KeyboardInterrupt, EOFError):
                return

        for show in datos_shows:
            if show['id-show'] == id_show:
                lista_temp.append(show)
                break 

        if not lista_temp:
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
                fecha_obj = datetime(año, mes, dia).date()
                fecha_buscada = fecha_obj.strftime("%Y-%m-%d")
                break
            except ValueError:
                print("\033[91mFecha incorrecta o números inválidos.\033[0m")
            except (KeyboardInterrupt, EOFError):
                return
            
        for i in datos_shows:
            if i['fecha'] == fecha_buscada:
                lista_temp.append(i)

        if not lista_temp:
            print("\033[91mNo se han encontrado shows en esa fecha.\033[0m")
        else:
            lista_temp = sorted(lista_temp, key=lambda x: x['fecha'])
            mostrar_tabla(lista_temp, 2)
def borrado_Show():
    datos_shows = cargar_datos_json(datos_shows_js)
    if not datos_shows:
        print("\033[91mNo hay shows registrados para eliminar.\033[0m")
        return
    vista_show()

    while True:
        try:
            eleccion = int(input("\n\033[36mIngrese el ID del show que desea eliminar:\033[0m "))
            
            show_encontrado = None
            for show in datos_shows:
                if show["id-show"] == eleccion:
                    show_encontrado = show
                    break
            
            if show_encontrado:
                break
            else:
                print("\033[91mNo se encontró el show especificado.\033[0m")
                return 
        except ValueError:
            print("\033[91mError de tipeo.\033[0m")
        except (KeyboardInterrupt, EOFError):
            return

        try:
            confirmar = input(f"\033[36m¿Está seguro de eliminar el show con ID {eleccion}? (s/n):\033[0m ").lower()
            if confirmar == "n": return
            if confirmar == "s": break
        except (KeyboardInterrupt, EOFError):
            return

    datos_shows.remove(show_encontrado)
    inicializar_datos_json(datos_shows_js, datos_shows)

    datos_reserva = cargar_datos_txt(datos_reserva_txt)
    reservas_nuevas = []
    count_reservas = 0
    
    for r in datos_reserva:
        try:
            id_show_reserva = int(r[3])
            if id_show_reserva != eleccion:
                reservas_nuevas.append(r)
            else:
                count_reservas += 1
        except (ValueError, IndexError):
            continue

    if count_reservas > 0:
        inicializar_datos_txt(datos_reserva_txt, reservas_nuevas)
        print(f"\033[34mSe eliminó el show y {count_reservas} reservas asociadas.\033[0m")
    else:
        print("\033[34mShow eliminado. No tenía reservas asociadas.\033[0m")

def edicion_show():
    datos_shows = cargar_datos_json(datos_shows_js)
    if not datos_shows:
        print("No hay shows.")
        return
    show_a_editar = None
    while True:
        try:
            eleccion = int(input("\033[36mSeleccione el ID del show:\033[0m "))
            for i in datos_shows:
                if i['id-show'] == eleccion:
                    show_a_editar = i
                    break
            if show_a_editar:
                break
            else:
                print("\033[91mID no encontrado.\033[0m")
        except (ValueError, KeyboardInterrupt):
            print("\033[91mIngrese un número válido.\033[0m")

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
            print("\033[91mError de tipeo.\033[0m")
        except (KeyboardInterrupt, EOFError):
            return
    cambio=True
    for shows in datos_shows:
        if shows["id-show"] == eleccion:
            if opcion == 0:
                nuevo_nombre = cambio_tipo_evento()
                if nuevo_nombre is not None:
                    shows['nombre-show'] = nuevo_nombre
                    cambio = True
            elif opcion == 1:
                fecha_actual = shows['fecha']
                shows_mismo_dia = []
                for s in datos_shows:
                    if s['fecha'] == fecha_actual:
                        shows_mismo_dia.append(s)

                duracion_antigua = int(shows['duracion-show'])
                nueva_duracion = cambio_duracion_evento(shows_mismo_dia, duracion_antigua)

                if nueva_duracion is not None:
                    shows['duracion-show'] = nueva_duracion
                    cambio = True

            elif opcion == 2:
                nuevo_precio = cambio_precio_evento()
                if nuevo_precio is not None:
                    shows['precio'] = nuevo_precio
                    cambio = True

            elif opcion == 3:
                nuevo_nombre = cambio_tipo_evento()
                if nuevo_nombre is not None:
                    shows['nombre-show'] = nuevo_nombre
                    cambio = True
                
                fecha_actual = shows['fecha']
                shows_mismo_dia = []
                for s in datos_shows:
                    if s['fecha'] == fecha_actual:
                        shows_mismo_dia.append(s)
                
                duracion_antigua = int(shows['duracion-show'])
                nueva_duracion = cambio_duracion_evento(shows_mismo_dia, duracion_antigua)
                
                if nueva_duracion is not None:
                    shows['duracion-show'] = nueva_duracion
                    cambio = True

                nuevo_precio = cambio_precio_evento()
                if nuevo_precio is not None:
                    shows['precio'] = nuevo_precio
                    cambio = True
            break
    if cambio:
        inicializar_datos_json(datos_shows_js, datos_shows)
        print("\033[34mShow editado correctamente.\033[0m")
    else:
        print("\033[33mNo se guardaron cambios.\033[0m")

def agregar_shows():
    datos_shows = cargar_datos_json(datos_shows_js)
    
    while True:
        try:
            año = int(input("\033[36mIngrese año:\033[0m "))
            mes = int(input("\033[36mIngrese mes:\033[0m "))
            dia = int(input("\033[36mIngrese día:\033[0m "))
            fecha_obj = datetime(año, mes, dia).date()
            fecha_buscada = fecha_obj.strftime("%Y-%m-%d")
            break
        except ValueError:
            print("\033[91mFecha inválida.\033[0m")
        except (KeyboardInterrupt, EOFError):
            return

    shows_del_dia = []
    for show in datos_shows:
        if show['fecha'] == fecha_buscada:
            shows_del_dia.append(show)
            
    print(f"\033[96mValidando disponibilidad para el {fecha_buscada}...\033[0m")
    
    duracion = cambio_duracion_evento(shows_del_dia, 0) 

    if duracion is None:
        print("Acción cancelada por el usuario.")
        return

    tipo_evento = cambio_tipo_evento()
    if tipo_evento is None: return

    precio = cambio_precio_evento()
    if precio is None: return
    
    id_show = nuevo_id_show(datos_shows)
    espectadores = 0
    espacios_disponibles = 999

    nuevo_show = {
            "id-show": id_show,
            "nombre-show": tipo_evento,
            "duracion-show": duracion,
            "espectadores": espectadores,
            "espacios-disponibles": espacios_disponibles,
            "fecha": str(fecha_buscada),
            "precio": precio
    }
    
    datos_shows.append(nuevo_show)
    inicializar_datos_json(datos_shows_js, datos_shows)
    print("\033[34mShow creado con éxito.\033[0m")