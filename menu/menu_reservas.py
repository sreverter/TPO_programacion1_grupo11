from funciones.funciones_reservas import vista_reserva,busqueda_Reserva,borrado_reserva,edicion_reserva, agregar_reservas

#se inicia el menu de reservas
def menu_reservas(admin):
    while True:
        #se ponen las opciones que puede usar el usuario para que elija
        if admin==False:
            try:
                usuario_i = int(input(
                    "\n\033[92m=== MENÚ DE RESERVA ===          \033[0m\n"
                    "\033[35m  → [1] VER RESERVA                \033[0m\n"
                    "\033[35m  → [2] GENERAR RESERVA            \033[0m\n"
                    "\033[35m  → [3] BORRAR RESERVA            \033[0m\n"
                    "\033[35m  → [4] VOLVER AL MENU DE OPCIONES \033[0m\n"
                    "\033[1;35m Seleccione una opción: \033[0m"
                    ))
            except ValueError:
                print("error de tipeo.")
                return
            except KeyboardInterrupt:
                print("Edición cancelada.")
                return

        #se ponen las opciones que puede usar el admin para que elija (mas opciones debido a mayor autoridad) 
        if admin==True:
            try:
                usuario_i = int(input(
                    "\n\033[92m=== MENÚ DE RESERVA ===         \033[0m\n"
                    "\033[35m  → [1] VER RESERVA               \033[0m\n"
                    "\033[35m  → [2] GENERAR RESERVA           \033[0m\n"
                    "\033[35m  → [3] BORRAR RESERVA            \033[0m\n"
                    "\033[35m  → [4] BUSCAR RESERVA            \033[0m\n"
                    "\033[35m  → [5] EDITAR RESERVA            \033[0m\n"
                    "\033[35m  → [6] VOLVER AL MENU DE OPCIONES\033[0m\n"
                    "\033[1;35m Seleccione una opción: \033[0m"
                ))
            except ValueError:
                print("error de tipeo.")
                return
            except KeyboardInterrupt:
                print("Edición cancelada.")
                return  

        if admin:
            func_reservas = [
                lambda: vista_reserva(admin),
                lambda: agregar_reservas(admin),
                lambda: borrado_reserva(admin),
                lambda: busqueda_Reserva(),
                lambda: edicion_reserva(),
                
            ]
        else:
            func_reservas = [
                lambda: vista_reserva(admin),
                lambda: agregar_reservas(admin),
                lambda: borrado_reserva(admin),
            ]

        maximo = len(func_reservas)
        if 1 <= usuario_i <= maximo:
            indice = usuario_i - 1
            func_reservas[indice]()


        elif (usuario_i==6 and admin==True) or (usuario_i==4 and admin==False):
            print("\033[35mesta saliendo al menu de inicio\033[0m")
            break
        else:
            print("\033[91mOpción no válida\033[0m")