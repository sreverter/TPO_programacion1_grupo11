def cambio_tipo_evento():
    try:
        tipo = input("\033[36mIngrese el nuevo tipo de evento:\033[0m ")
        if len(tipo) > 0:
            return tipo
        else:
            print("\033[91mEl tipo de evento no puede estar vacío.\033[0m")
            return "Sin título"
    except (KeyboardInterrupt, EOFError):
        print("\033[91mSaliendo de la edicion de tipo de evento.\033[0m")
        return None

def cambio_duracion_evento(datos_shows, duracion_a_descontar):
    minutos_ocupados_total = 0
    for s in datos_shows:
        try:
            minutos_ocupados_total += int(s['duracion-show'])
        except (ValueError, KeyError):
            continue
    minutos_reales_ocupados = minutos_ocupados_total - duracion_a_descontar
    espacio_libre = 720 - minutos_reales_ocupados
    print(f"\033[93mTiempo ocupado: {minutos_reales_ocupados} min. Tiempo disponible: {espacio_libre} min.\033[0m")

    while True:
        try:
            duracion_nueva = int(input("\033[36mIngrese la duración en minutos:\033[0m "))
            if duracion_nueva <= 0:
                print("\033[91mDebe ser un número positivo.\033[0m")
                continue
            if duracion_nueva > espacio_libre:
                print(f"\033[91mError: La duración supera las 12 horas (720 min).\033[0m")
                print(f"\033[91mMáximo disponible: {espacio_libre} minutos.\033[0m")
                continue
            return duracion_nueva
        except ValueError:
            print("\033[91mIngrese caracteres numéricos válidos.\033[0m")
        except (KeyboardInterrupt, EOFError):
            return None

def cambio_precio_evento():
    while True:
        try:
            precio = int(input("\033[36mDefina un precio para el show:\033[0m "))
            if precio < 0:
                print("\033[91mEl precio no puede ser negativo.\033[0m")
                continue
            if precio == 0:
                eleccion = input("\033[36mEstá seleccionando una entrada gratuita. ¿Está seguro? (s/n):\033[0m ").lower()
                if eleccion == "s":
                    return precio
                else:
                    continue
            elif precio >= 99999:
                eleccion = input("\033[36mEstá seleccionando una entrada muy cara. ¿Está seguro? (s/n):\033[0m ").lower()
                if eleccion == "s":
                    return precio
                else:
                    continue
            else:
                return precio
        except ValueError:
            print("\033[91mDebe ingresar un número entero válido.\033[0m")
        except (KeyboardInterrupt, EOFError):
            return None


def nuevo_id_show(datos_shows):
    if not datos_shows:
        return 1
    
    mayor_id = 0
    for show in datos_shows:
        try:
            id_actual = int(show['id-show'])
            if id_actual > mayor_id:
                mayor_id = id_actual
        except (ValueError, KeyError):
            continue
            
    return mayor_id + 1

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
                continue
            except (KeyboardInterrupt, EOFError):
                print("\033[91saliendo de la edicion de shows\033[0m")
                return None