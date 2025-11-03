from funciones.funciones_estadisticas import shows_mas_vendidos,shows_con_mayor_recaudacion,usuarios_mas_activos,usuarios_con_mas_reservas
#region tareas
#usar filter para rangos de edades

#se inicia el menu de estadisticass
def menu_estadisticas():
    while True:
        try:
        #se muestran las opciones que pueden elegir
            usuario_i = int(input(
                "\033[92m=== MENÚ DE ESTADÍSTICAS ===                 \033[0m\n"
                "\033[35m  → [1] SHOWS MÁS VENDIDOS                   \033[0m\n"
                "\033[35m  → [2] SHOWS MÁS RECAUDADOS                 \033[0m\n"
                "\033[35m  → [3] USUARIOS ACTIVOS                     \033[0m\n"
                "\033[35m  → [4] USUARIOS CON MÁS RESERVAS            \033[0m\n"
                "\033[35m  → [5] VOLVER                               \033[0m\n"
                "\033[1;35m Seleccione una opción: \033[0m"
            ))
        except (ValueError,KeyboardInterrupt):
            print()
            print("\033[91mcoloque caracteres validos\033[0m")
            continue

        func_shows = [
                lambda: shows_mas_vendidos(),
                lambda: shows_con_mayor_recaudacion(),
                lambda: usuarios_mas_activos(),
                lambda: usuarios_con_mas_reservas(),
        ]

        maximo = len(func_shows)
        if 1 <= usuario_i <= maximo:
            indice = usuario_i - 1
            func_shows[indice]()


        elif usuario_i==5:
            print("esta saliendo al menu de inicio")
            break

        #se delimita las opciones que podes con esto para que si elije mal alguna opcion pueda volver a ver las opciones y elija bien
        else:
            print("\033[91mOpción no válida\033[0m")