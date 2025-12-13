def cambio_tipo_evento():
    try:
        tipo = input("\033[36mIngrese el nuevo tipo de evento:\033[0m ")
        if len(tipo) > 0:
            return tipo
        else:
            print("\033[91mEl tipo de evento no puede estar vacío.\033[0m")
            return "Sin título"
    except ValueError:
        print("error de tipeo.")
        return
    except KeyboardInterrupt:
        print("Edición cancelada.")
        return
def cambio_duracion_evento(shows):
    suma = 0
    suma = int(shows['duracion-show'])
    while True:
        try:
            duracion = int(input("\033[36mIngrese la duración en minutos:\033[0m "))
            if duracion < 0:
                print("\033[91mDebe ser un número positivo.\033[0m")
                continue
            if (suma + duracion) > 720:
                print("\033[91mLa duración total supera las 12 horas del día. Consulte con un gerente.\033[0m")
                continue
            return duracion
        except ValueError:
            print("error de tipeo.")
            return None
        except KeyboardInterrupt:
            print("Edición cancelada.")
            return None

def cambio_precio_evento():
    while True:
        try:
            precio = int(input("\033[36mDefina un precio para el show:\033[0m "))
            if precio == 0:
                eleccion = str(input("\033[36mEstá seleccionando una entrada gratuita. ¿Está seguro de su decisión? (s/n):\033[0m ")).lower()
                if eleccion == "s":
                    return precio
                elif eleccion == "n":
                    continue
            elif precio >= 99999:
                eleccion = str(input("\033[36mEstá seleccionando una entrada extremadamente cara. ¿Está seguro de su decisión? (s/n):\033[0m ")).lower()
                if eleccion == "s":
                    return precio
                elif eleccion == "n":
                    continue
            else:
                print("precio no puede ir a negativos")
        except ValueError:
            print("error de tipeo.")
            continue
        except KeyboardInterrupt:
            print("Edición cancelada.")
            continue
def nuevo_id_show(datos_shows):
    if datos_shows == []:
        return 1
    shows_ordenados = sorted(datos_shows, key=lambda x: x['id-show'])
    def obtener_ultimo_id(lista, i=0):
        if i == len(lista) - 1:
            return lista[i]['id-show']
        return obtener_ultimo_id(lista, i + 1)
    ultimo = obtener_ultimo_id(shows_ordenados)
    agregado = ultimo + 1
    return agregado
def menu_edicion_shows():
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
                    return opcion
                else:
                    print("\033[91mNúmero fuera del rango permitido.\033[0m")
            except ValueError:
                print("\033[91mEntrada inválida.\033[0m")
            except (KeyboardInterrupt, EOFError):
                print("saliendo de la edicion de shows")
                return None