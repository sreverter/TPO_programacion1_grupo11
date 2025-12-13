import json
import os


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
            print(f"\033[1m{"Reservas"}\033[0m")
            print(f"\033[32m{'-'*64}\033[0m")
            print(
            f"\033[32m{'|'}\033[0m"
            f'\033[38;5;183m{"ID Reserva":<12}\033[0m'  # Lavanda suave
            f'\033[38;5;120m{"ID Usuario":<12}\033[0m'  # Verde Menta
            f'\033[38;5;117m{"Sector":<10}\033[0m'      # Celeste Pálido
            f'\033[38;5;215m{"ID Show":<10}\033[0m'     # Durazno/Naranja suave
            f'\033[38;5;229m{"Precio":<10}\033[0m'      # Amarillo Crema
            f'\033[38;5;211m{"Cantidad":<8}\033[0m'    # Rosa suave
            f"\033[32m{'|'}\033[0m"
            )
            linea = archivo.readline()
            while linea != '':
                datos = linea.strip().split(",")
                id_reserva = datos[0]
                id_usuario = datos[1]
                sector = datos[2]
                id_show = datos[3]
                precio = datos[4]
                cantidad = datos[5]
                print(
                f"\033[32m{'|'}\033[0m"
                f'\033[38;5;183m{id_reserva:<12}\033[0m'  
                f'\033[38;5;120m{id_usuario:<12}\033[0m'  
                f'\033[38;5;117m{sector:<10}\033[0m'      
                f'\033[38;5;215m{id_show:<10}\033[0m'     
                f'\033[38;5;229m{precio:<10}\033[0m'      
                f'\033[38;5;211m{cantidad:<8}\033[0m'    
                f"\033[32m{'|'}\033[0m"
                )
                linea = archivo.readline()
    except IOError as e:
        print(f"Error al leer el archivo: {e}")

def busqueda_en_txt(ruta_archivo, buscar, dato):
    try:
        with open(ruta_archivo, 'rt', encoding="utf-8") as archivo:
            linea = archivo.readline()
            reservas_encontrados = []
            while linea != '':
                datos = linea.strip().split(",")
                id_reserva = int(datos[0])
                id_usuario = int(datos[1])
                sector = datos[2]
                id_show = int(datos[3])
                precio = int(datos[4])
                cantidad = int(datos[5]) 
                if dato == 1:
                    if id_usuario == buscar:
                        encontrado = [id_reserva, id_usuario, sector, id_show, precio, cantidad]
                        reservas_encontrados.append(encontrado)
                    linea = archivo.readline()
                elif dato == 2:
                    if id_reserva == buscar:
                        encontrado = [id_reserva, id_usuario, sector, id_show, precio, cantidad]
                        reservas_encontrados.append(encontrado)
                    linea = archivo.readline()
            return reservas_encontrados

    except IOError as e:
        print(f"Error al leer el archivo: {e}")

def borrado_en_txt(ruta_archivo, borrar, opcion):
    temp = 'datos/datos_reservas_temp.txt'
    encontrado = False

    if opcion == 1:
        try:
            arch = open(ruta_archivo, "rt", encoding="UTF-8")
            aux = open(temp, "wt", encoding="UTF-8")
            for linea in arch:
                datos = linea.strip().split(",")
                id_reserva = int(datos[0])
                if id_reserva != int(borrar):
                    aux.write(linea)
                else:
                    encontrado = True

        except FileNotFoundError:
            print("El archivo no existe.")
        except OSError as error:
            print("Error en el acceso al archivo:", error)
        finally:
            try:
                arch.close()
                aux.close()
            except:
                print("Error en el cierre del archivo:")

        if encontrado == True:
            try:
                os.remove(ruta_archivo)
                os.rename(temp, ruta_archivo) # renombra el temporal
                print(f"Reserva con ID {borrar} eliminado correctamente.")
            except OSError as error:
                print("Error al reemplazar el archivo:", error)
        else:
            os.remove(temp)  # eliminamos el temporal si no se usó
            print(f"No se encontró la reserva con ID {borrar}.")
    
    elif opcion == 2:
        try:
            arch = open(ruta_archivo, "rt", encoding="UTF-8")
            aux = open(temp, "wt", encoding="UTF-8")
            for linea in arch:
                datos = linea.strip().split(",")
                id_usuario = int(datos[1])
                if id_usuario != int(borrar):
                    aux.write(linea)
                else:
                    encontrado = True

        except FileNotFoundError:
            print("El archivo no existe.")
        except OSError as error:
            print("Error en el acceso al archivo:", error)
        finally:
            try:
                arch.close()
                aux.close()
            except:
                print("Error en el cierre del archivo:")

        if encontrado == True:
            try:
                os.remove(ruta_archivo)
                os.rename(temp, ruta_archivo) # renombra el temporal
                print(f"Reservas con ID de usuario {borrar} eliminadas correctamente.")
            except OSError as error:
                print("Error al reemplazar el archivo:", error)
        else:
            os.remove(temp)  # eliminamos el temporal si no se usó
            print(f"No se encontró la reserva con ID {borrar}.")

def modificacion_en_txt(ruta_archivo, id_reserva_modif, nuevo_show_id=None, nuevo_sector=None, nuevo_precio=None):
    temp = 'datos/datos_reservas_temp.txt'
    encontrado = False

    try:
        arch = open(ruta_archivo, "rt", encoding="UTF-8")
        aux = open(temp, "wt", encoding="UTF-8")

        for linea in arch:
            datos = linea.strip().split(",")
            id_reserva = int(datos[0])
            id_usuario = int(datos[1])
            sector = datos[2]
            id_show = int(datos[3])
            # precio = int(datos[4])
            cantidad = int(datos[5])

            if nuevo_show_id is None:
                if id_reserva == id_reserva_modif:
                    encontrado = True
                    nueva_linea = f"{id_reserva},{id_usuario},{nuevo_sector},{id_show},{nuevo_precio},{cantidad}\n"
                    print(nueva_linea)
                    aux.write(nueva_linea)
                    print(f"Reserva {id_reserva} modificada.")
                else:
                    aux.write(linea)
            else:
                if id_reserva == id_reserva_modif:
                    encontrado = True
                    nueva_linea = f"{id_reserva},{id_usuario},{sector},{nuevo_show_id},{nuevo_precio},{cantidad}\n"
                    print(nueva_linea)
                    aux.write(nueva_linea)
                    print(f"Reserva {id_reserva} modificada.")
                else:
                    aux.write(linea)
    except FileNotFoundError:
        print("El archivo no existe.")
    except OSError as error:
        print("Error en el acceso al archivo:", error)
    finally:
        try:
            arch.close()
            aux.close()
        except:
            print("Error en el cierre del archivo:")

    if encontrado:
        try:
            os.remove(ruta_archivo)
            os.rename(temp, ruta_archivo)
        except OSError as error:
            print("Error al reemplazar el archivo:", error)
    else:
        os.remove(temp)
        print(f"No se encontró la reserva {id_reserva_modif}.")