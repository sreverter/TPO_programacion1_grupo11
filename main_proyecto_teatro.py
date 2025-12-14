from ingreso import *
from menu.menu_reservas import menu_reservas
from menu.menu_usuarios import menu_usuarios
from menu.menu_shows import menu_shows
from menu.menu_estadisticas import menu_estadisticas
from funciones.funciones_globales import *
from datos import *

# FLAGS
admin = False
ingreso = True
menu = False
start = True
usuario = 0

while start:

    # ================= LOGIN =================
    while ingreso:
        try:
            destino_ingreso = menu_login()

            if destino_ingreso is None:
                start = False
                ingreso = False
                break

            if destino_ingreso == 0:
                log = login()

                if log == "ADMIN":
                    admin = True
                    menu = True
                    ingreso = False

                elif log == "Usuario":
                    admin = False
                    menu = True
                    ingreso = False

            elif destino_ingreso == 1:
                registrar()

        except (KeyboardInterrupt, EOFError):
            print("\n\033[93mEjecución interrumpida por el usuario. Saliendo...\033[0m")
            start = False
            ingreso = False
            break

    if not start:
        break

    # ================= MENÚ PRINCIPAL =================
    while menu:
        try:
            if admin:
                usuario = int(input(
                    "\n\033[92m=== MENÚ DE OPCIONES ===\033[0m\n"
                    "\033[35m  → [1] SHOWS             \033[0m\n"
                    "\033[35m  → [2] RESERVAS          \033[0m\n"
                    "\033[35m  → [3] USUARIOS          \033[0m\n"
                    "\033[35m  → [4] ESTADISTICAS      \033[0m\n"
                    "\033[35m  → [5] SALIR DE LA SESIÓN\033[0m\n"
                    "\033[35m  → [6] SALIR DEL PROGRAMA\033[0m\n"
                    "\033[1;35m Seleccione una opción: \033[0m"
                ))
            else:
                usuario = int(input(
                    "\n\033[92m=== MENÚ DE OPCIONES ===\033[0m\n"
                    "\033[35m  → [1] SHOWS             \033[0m\n"
                    "\033[35m  → [2] RESERVAS          \033[0m\n"
                    "\033[35m  → [3] USUARIOS          \033[0m\n"
                    "\033[35m  → [4] SALIR DE LA SESIÓN\033[0m\n"
                    "\033[35m  → [5] SALIR DEL PROGRAMA\033[0m\n"
                    "\033[1;35m Seleccione una opción: \033[0m"
                ))

        except (KeyboardInterrupt, EOFError):
            print("\n\033[93mEjecución interrumpida por el usuario. Saliendo...\033[0m")
            start = False
            menu = False
            break

        except ValueError:
            print("\033[91mDebe ingresar un número válido.\033[0m")
            continue

        # -------- SUBMENÚS --------
        if admin:
            func_start = [
                lambda: menu_shows(admin),
                lambda: menu_reservas(admin),
                lambda: menu_usuarios(admin),
                lambda: menu_estadisticas(),
            ]
        else:
            func_start = [
                lambda: menu_shows(admin),
                lambda: menu_reservas(admin),
                lambda: menu_usuarios(admin),
            ]

        maximo = len(func_start)

        if 1 <= usuario <= maximo:
            func_start[usuario - 1]()
            continue

        if (usuario == 5 and admin) or (usuario == 4 and not admin):
            admin = False
            ingreso = True
            menu = False
            dni_en_uso.clear()
            break

        if (usuario == 6 and admin) or (usuario == 5 and not admin):
            start = False
            menu = False
            break

        print("\033[91mSu número está fuera de los parámetros dados.\033[0m")
