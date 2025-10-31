import json
from datos import datos_shows

def mostrar_tabla(dato, opcion):

    #matriz
    if opcion == 1:

        #Encabezado de la tabla
        print(f"\033[32m{'-'*73}\033[0m")
        print(f"\033[32m{'IDs':<8}  {'ID Usuario':<13}\033  \033[35m{'Ubicación':>10}  {'ID Show':>12}\033[0m  \033[34m{'Precio':>14}\033[0m")
        print(f"\033[32m{'-'*73}\033[0m")

        for fila in dato:
            print(f"\033[32m{fila[0]:<8}  {fila[1]:<13}\033[35m  {fila[2]:>10}  {fila[3]:>10}\033[0m  \033[34m{fila[4]:>14}\033[0m")
    
    #diccionario
    elif opcion == 2:
        #Encabezado de la tabla
        print(f"\033[32m{'-'*73}\033[0m")
        for usuario in dato:
            lista= list(usuario.keys())
        print(f"\033[32m{lista[0]:<8}  {lista[1]:<15}\033  \033[35m{lista[2]:>15}  {lista[3]:>25}\033[0m  \033[34m{lista[4]:>15} {lista[5]:>15}\033[0m")
        print(f"\033[32m{'-'*73}\033[0m")

        for fila in dato:
            for item in fila:
                if fila[item] == True:
                    print(f"\033[32m{'Activo':<25}\033[0m", end="  ")
                elif fila[item] == False:
                    print(f"\033[31m{'Inactivo':<25}\033[0m", end="  ")
                else:
                    print(f"\033[32m{fila[item]:<25}\033[0m", end="  ")
            print()


def inicializar_datos_json(ruta_archivo, datos):
    nuevos_datos = json.dumps(datos, indent=4, ensure_ascii=False)
    try:
        with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write(nuevos_datos + "\n" )
    except IOError as e:
        print(f"Error al escribir el archivo: {e}")

def inicializar_datos_txt(ruta_archivo, datos):
    try:
        linea = [f"{id_reserva},{id_usuario},{sector},{id_show},{precio}\n" for id_reserva, id_usuario, sector, id_show, precio in datos]
        with open(ruta_archivo, 'w',encoding='utf-8') as archivo:
            archivo.writelines(linea + "\n")
    except IOError as e:
        print(f"Error al escribir el archivo: {e}")


def cargar_datos_json(ruta_archivo):
    try:
        with open(ruta_archivo, 'r', encoding="utf-8") as archivo:
            datos_cargados = json.load(archivo)
            return datos_cargados
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error al cargar el archivo: {e}")

def cargar_datos_txt(ruta_archivo):
    datos_cargados = []
    try:
        with open(ruta_archivo, 'r',encoding="utf-8") as archivo:
            linea = archivo.readline().strip()
            while linea:
                id_reserva, id_usuario, sector, id_show, precio = linea.split(',')
                datos_cargados.append([int(id_reserva), int(id_usuario), sector, int(id_show), int(precio)])
                linea = archivo.readline().strip()
        return datos_cargados
    except IOError as e:
        print(f"Error al cargar el archivo: {e}")