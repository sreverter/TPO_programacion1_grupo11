from funciones.funciones_shows import *
def menu_shows(admin):
    while True:
        if admin==False:
            try:    
                usuario_i=int(input(
                "\n\033[92m=== MENÚ DE SHOWS ===         \033[0m\n"
                "\033[35m  → [1] VER SHOWS               \033[0m\n"
                "\033[35m  → [2] BUSCAR SHOWS            \033[0m\n"
                "\033[35m  → [3] VOLVER AL MENU PRINCIPAL\033[0m\n"
                "\033[1;35m Seleccione una opción: \033[0m" ))
                if usuario_i in (1,2,3):
                    break
                else:
                    print(f"\033[91m Opción inválida, intente de nuevo.\033[0m")

            except ValueError:
                print("error de tipeo.")
                continue
            except KeyboardInterrupt:
                print("Edición cancelada.")
                continue

        if admin:
            try:
                usuario_i=int(input(
                "\n\033[92m=== MENÚ DE SHOWS ===         \033[0m\n"
                "\033[35m  → [1] VER SHOWS               \033[0m\n"
                "\033[35m  → [2] BUSCAR SHOWS            \033[0m\n"
                "\033[35m  → [3] BORRAR SHOW             \033[0m\n"
                "\033[35m  → [4] EDITAR SHOW             \033[0m\n"
                "\033[35m  → [5] GENERAR SHOW            \033[0m\n"
                "\033[35m  → [6] VOLVER AL MENU PRINCIPAL\033[0m\n"
                "\033[1;35m Seleccione una opción: \033[0m" ))
                if usuario_i in (1,2,3,4,5,6):
                    break
                else:
                    print(f"\033[91m Opción inválida, intente de nuevo.\033[0m")

            except ValueError:
                print("error de tipeo.")
                continue
            except KeyboardInterrupt:
                print("Edición cancelada.")
                continue

        if admin:
            func_shows = [
                lambda: vista_show(),
                lambda: busqueda_Show(),
                lambda: borrado_Show(),
                lambda: edicion_show(),
                lambda: agregar_shows()
            ]
        else:
            func_shows = [
                lambda: vista_show(),
                lambda: busqueda_Show()
            ]

        maximo = len(func_shows)
        if 1 <= usuario_i <= maximo:
            indice = usuario_i - 1
            func_shows[indice]()

        elif (usuario_i==6 and admin==True) or (usuario_i==3 and admin==False):
            print("\033[35mesta saliendo al menu de inicio\033[0m")
            break
        else:
            print("\033[91mOpción no válida\033[0m")