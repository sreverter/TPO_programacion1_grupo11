from funciones.funciones_reservas import (vista_reserva,busqueda_Reserva,borrado_reserva,edicion_reserva,agregar_reservas)

def menu_reservas(admin):

    while True:

        try:
            if admin:
                opcion = int(input(
                    "\n\033[92m=== MENÚ DE RESERVAS (ADMIN) ===\033[0m\n"
                    "\033[35m  → [1] VER RESERVAS             \033[0m\n"
                    "\033[35m  → [2] GENERAR RESERVA          \033[0m\n"
                    "\033[35m  → [3] BORRAR RESERVA           \033[0m\n"
                    "\033[35m  → [4] BUSCAR RESERVA           \033[0m\n"
                    "\033[35m  → [5] EDITAR RESERVA           \033[0m\n"
                    "\033[35m  → [6] VOLVER                   \033[0m\n"
                    "\033[1;35m Seleccione una opción: \033[0m"
                ))
            else:
                opcion = int(input(
                    "\n\033[92m=== MENÚ DE RESERVAS ===\033[0m\n"
                    "\033[35m  → [1] VER RESERVAS             \033[0m\n"
                    "\033[35m  → [2] GENERAR RESERVA          \033[0m\n"
                    "\033[35m  → [3] BORRAR RESERVA           \033[0m\n"
                    "\033[35m  → [4] VOLVER                   \033[0m\n"
                    "\033[1;35m Seleccione una opción: \033[0m"
                ))
        except ValueError:
            print("\033[91mError: debe ingresar un número.\033[0m")
            continue
        except KeyboardInterrupt:
            print("\n\033[91mOperación cancelada.\033[0m")
            return

        if (admin and opcion == 6) or (not admin and opcion == 4):
            print("\033[35mVolviendo al menú principal...\033[0m")
            break

        if admin:
            funciones = [
                lambda: vista_reserva(True),   
                lambda: agregar_reservas(True),
                lambda: borrado_reserva(True), 
                busqueda_Reserva,             
                edicion_reserva               
            ]
        else:
            funciones = [
                lambda: vista_reserva(False), 
                lambda: agregar_reservas(False),
                lambda: borrado_reserva(False) 
            ]

        if 1 <= opcion <= len(funciones):
            funciones[opcion - 1]()
        else:
            print("\033[91mOpción inválida.\033[0m")
