import json


def mostrar_tabla(dato, opcion):

    #matriz
    if opcion == 1:

        #Encabezado de la tabla
        print(f"\033[32m{'-'*80}\033[0m")
        print(f"\033[32m{'IDs':<8}  {'ID Usuario':<13}\033  \033[35m{'Ubicación':>10}  {'ID Show':>12}\033[0m  \033[34m{'Precio':>14}  \033[34m{'cantidad':>14}\033[0m")
        print(f"\033[32m{'-'*80}\033[0m")

        # for fila in dato:
        #     print(f"\033[32m{fila[0]:<8}  {fila[1]:<13}\033[35m  {fila[2]:>10}  {fila[3]:>10}\033[0m  \033[34m{fila[4]:>14} {fila[5]:>14}\033[0m")

        def imprimir_filas(filas, i=0):
            if i >= len(filas):
                return
            fila = filas[i]
            print(f"\033[32m{fila[0]:<8}  {fila[1]:<13}\033[35m  {fila[2]:>10}  {fila[3]:>10}\033[0m  \033[34m{fila[4]:>14} {fila[5]:>14}\033[0m")
            imprimir_filas(filas, i + 1)

        imprimir_filas(dato)
    
    #diccionario
    elif opcion == 2:
        # Detectar tipo por claves
        if "dni" in dato[0]:
            tipo = "usuario"
        elif "id-show" in dato[0]:
            tipo = "show"

        if tipo == "usuario":
            print(f"\033[32m{'-'*120}\033[0m")
            print(f"\033[32m{'ID':<5} {'Nombre':<25} {'DNI':<12} {'Teléfono':<20} {'Correo':<35} {'Estado':<10}\033[0m")
            print(f"\033[32m{'-'*120}\033[0m")
            for fila in dato:
                estado = "\033[32mActivo\033[0m" if fila['estado'] else "\033[31mInactivo\033[0m"
                print(f"{fila['id']:<5} {fila['nombre']:<25} {fila['dni']:<12} {fila['telefono']:<20} {fila['correo']:<35} {estado:<10}")

        elif tipo == "show":
            print(f"\033[32m{'-'*113}\033[0m")
            print(f"\033[32m{'ID Show':<10} {'Nombre Show':<35} {'Duración':<10} {'Espectadores':<15} {'Espacios Disp.':<15} {'Fecha':<15} {'precio':<15}\033[0m")
            print(f"\033[32m{'-'*113}\033[0m")
            for fila in dato:
                print(f"{fila['id-show']:<10} {fila['nombre-show']:<35} {fila['duracion-show']:<10} "
                    f"{fila['espectadores']:<15} {fila['espacios-disponibles']:<15} {fila['fecha']:<15} {fila['precio']}")


def inicializar_datos_json(ruta_archivo, datos):
    nuevos_datos = json.dumps(datos, indent=4, ensure_ascii=False)
    try:
        with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write(nuevos_datos + "\n" )
    except IOError as e:
        print(f"Error al escribir el archivo: {e}")

def inicializar_datos_txt(ruta_archivo, datos):
    try:
        linea = [f"{id_reserva},{id_usuario},{sector},{id_show},{precio},{cantidad}\n" for id_reserva, id_usuario, sector, id_show, precio, cantidad in datos]
        with open(ruta_archivo, 'w',encoding='utf-8') as archivo:
            archivo.writelines(linea)#esta linea
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
                id_reserva, id_usuario, sector, id_show, precio, cantidad = linea.split(',')
                datos_cargados.append([int(id_reserva), int(id_usuario), sector, int(id_show), int(precio), int(cantidad)])
                linea = archivo.readline().strip()
        return datos_cargados
    except IOError as e:
        print(f"Error al cargar el archivo: {e}")

def checkear_dato_repetido(datos_checkear, dato_a_checkear, clave):
    lista_sin_repetidos = []
    for dato in datos_checkear:
        lista_sin_repetidos.append(dato[clave])
    conjunto_datos = set(lista_sin_repetidos)
    if dato_a_checkear in conjunto_datos:
        return True
    return False

def mostrar_archivo_texto(ruta_archivo):
    try:
        with open(ruta_archivo, 'rt', encoding="utf-8") as archivo:
            print('Reservas')
            print(f'{"ID Reserva":<12}{"ID Usuario":<12}{"Sector":<10}{"ID Show":<10}{"Precio":<10}{"Cantidad":<10}')
            linea = archivo.readline()
            while linea != '':
                datos = linea.strip().split(",")
                id_reserva = datos[0]
                id_usuario = datos[1]
                sector = datos[2]
                id_show = datos[3]
                precio = datos[4]
                cantidad = datos[5]
                print(f'{id_reserva:<12}{id_usuario:<12}{sector:<10}{id_show:<10}{precio:<10}{cantidad:<10}')
                linea = archivo.readline()
    except IOError as e:
        print(f"Error al leer el archivo: {e}")

def busqueda_en_txt(ruta_archivo, buscar, dato):
    try:
        with open(ruta_archivo, 'rt', encoding="utf-8") as archivo:
            linea = archivo.readline()
            encontrado = []
            while linea != '':
                datos = linea.strip().split(",")
                id_reserva = int(datos[0])
                id_usuario = int(datos[1])
                sector = datos[2]
                id_show = int(datos[3])
                precio = int(datos[4])
                cantidad = int(datos[5]) 
                match dato:
                    case 1:
                        if id_usuario == buscar:
                            encontrado.append([id_reserva, id_usuario, sector, id_show, precio, cantidad])
                            return encontrado
                    case 2:
                        if id_reserva == buscar:
                            encontrado.append([id_reserva, id_usuario, sector, id_show, precio, cantidad])
                            return encontrado
                linea = archivo.readline()
    except IOError as e:
        print(f"Error al leer el archivo: {e}")