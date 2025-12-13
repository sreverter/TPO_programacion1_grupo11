from funciones.funciones_estadisticas import (shows_mas_vendidos,shows_con_mayor_recaudacion,usuarios_mas_activos,usuarios_con_mas_reservas)

def menu_estadisticas():

    while True:
        try:
            opcion = int(input(
                "\n\033[92m=== MENÚ DE ESTADÍSTICAS ===\033[0m\n"
                "\033[35m  → [1] SHOWS MÁS VENDIDOS        \033[0m\n"
                "\033[35m  → [2] SHOWS MÁS RECAUDADOS      \033[0m\n"
                "\033[35m  → [3] USUARIOS MÁS ACTIVOS      \033[0m\n"
                "\033[35m  → [4] USUARIOS CON MÁS RESERVAS \033[0m\n"
                "\033[35m  → [5] VOLVER                    \033[0m\n"
                "\033[1;35m Seleccione una opción: \033[0m"
            ))
        except ValueError:
            print("\033[91mError: debe ingresar un número.\033[0m")
            continue
        except KeyboardInterrupt:
            print("\n\033[91mOperación cancelada.\033[0m")
            return

        if opcion == 5:
            print("\033[35mVolviendo al menú principal...\033[0m")
            break

        funciones = [
            shows_mas_vendidos,          
            shows_con_mayor_recaudacion, 
            usuarios_mas_activos,        
            usuarios_con_mas_reservas    
        ]

        if 1 <= opcion <= len(funciones):
            funciones[opcion - 1]()
        else:
            print("\033[91mOpción inválida.\033[0m")
