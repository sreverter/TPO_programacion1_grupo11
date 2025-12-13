from funciones.funciones_usuarios import *

def menu_usuarios(admin):

    while True:

        try:
            if admin:
                opcion = int(input(
                    "\n\033[92m=== MENÚ DE USUARIOS (ADMIN) ===\033[0m\n"
                    "\033[35m  → [1] VER USUARIO                \033[0m\n"
                    "\033[35m  → [2] EDITAR USUARIO             \033[0m\n"
                    "\033[35m  → [3] BORRAR USUARIO             \033[0m\n"
                    "\033[35m  → [4] VOLVER AL MENÚ DE OPCIONES \033[0m\n"
                    "\033[1;35m Seleccione una opción: \033[0m"
                ))
            else:
                opcion = int(input(
                    "\n\033[92m=== MENÚ DE USUARIO ===\033[0m\n"
                    "\033[35m  → [1] VER USUARIO                \033[0m\n"
                    "\033[35m  → [2] EDITAR USUARIO             \033[0m\n"
                    "\033[35m  → [3] VOLVER AL MENÚ DE OPCIONES \033[0m\n"
                    "\033[1;35m Seleccione una opción: \033[0m"
                ))
        except ValueError:
            print("\033[91mError: debe ingresar un número.\033[0m")
            continue
        except KeyboardInterrupt:
            print("\n\033[91mOperación cancelada.\033[0m")
            return

        if (not admin and opcion == 3) or (admin and opcion == 4):
            print("\033[35mVolviendo al menú principal...\033[0m")
            break

        if admin:
            funciones = [
                lambda: vista_Usuarios(True),   
                lambda: edicion_usuario(True),  
                borrado_usuarios                
            ]
        else:
            funciones = [
                lambda: vista_Usuarios(False),  
                lambda: edicion_usuario(False)  
            ]

        if 1 <= opcion <= len(funciones):
            funciones[opcion - 1]()
        else:
            print("\033[91mOpción inválida.\033[0m")
