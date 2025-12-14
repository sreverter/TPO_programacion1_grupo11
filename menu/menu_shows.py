from funciones.funciones_shows import *

def menu_shows(admin):

    while True:

        try:
            if admin:
                opcion = int(input(
                    "\n\033[92m=== MENÚ DE SHOWS (ADMIN) ===\033[0m\n"
                    "\033[35m  → [1] VER SHOWS               \033[0m\n"
                    "\033[35m  → [2] BUSCAR SHOWS            \033[0m\n"
                    "\033[35m  → [3] BORRAR SHOW             \033[0m\n"
                    "\033[35m  → [4] EDITAR SHOW             \033[0m\n"
                    "\033[35m  → [5] GENERAR SHOW            \033[0m\n"
                    "\033[35m  → [6] VOLVER AL MENÚ PRINCIPAL\033[0m\n"
                    "\033[1;35m Seleccione una opción: \033[0m"
                ))
            else:
                opcion = int(input(
                    "\n\033[92m=== MENÚ DE SHOWS ===\033[0m\n"
                    "\033[35m  → [1] VER SHOWS               \033[0m\n"
                    "\033[35m  → [2] BUSCAR SHOWS            \033[0m\n"
                    "\033[35m  → [3] VOLVER AL MENÚ PRINCIPAL\033[0m\n"
                    "\033[1;35m Seleccione una opción: \033[0m"
                ))
        except ValueError:
            print("\033[91mError: debe ingresar un número.\033[0m")
            continue
        except KeyboardInterrupt:
            print("\n\033[91mOperación cancelada.\033[0m")
            return


        if (not admin and opcion == 3) or (admin and opcion == 6):
            print("\033[35mVolviendo al menú principal...\033[0m")
            break

        if admin:
            funciones = [
                vista_show,     
                busqueda_Show,  
                borrado_Show,   
                edicion_show,   
                agregar_shows   
            ]
        else:
            funciones = [
                vista_show,     
                busqueda_Show   
            ]

        if 1 <= opcion <= len(funciones):
            funciones[opcion - 1]()
        else:
            print("\033[91mOpción inválida.\033[0m")
