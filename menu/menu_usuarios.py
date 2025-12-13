from funciones.funciones_usuarios import *

def menu_usuarios(admin):
    while True:
        if admin==False:
                try:
                    usuario_i=int(input(
                    "\n\033[92m=== MENÚ DE USUARIO ===          \033[0m\n"
                    "\033[35m  → [1] VER USUARIO                \033[0m\n"
                    "\033[35m  → [2] EDITAR USUARIO            \033[0m\n"
                    "\033[35m  → [3] VOLVER AL MENU DE OPCIONES \033[0m\n"
                    "\033[1;35m Seleccione una opción: \033[0m"
                    ))
                    if usuario_i in (0, 1,2,3,4,5,6):
                        return usuario_i
                    else:
                        print(f"\033[91m Opción inválida, intente de nuevo.\033[0m")
                except ValueError:
                    print("error de tipeo.")
                    return
                except KeyboardInterrupt:
                    print("Edición cancelada.")
                    return
        if admin==True:
            try:
                usuario_i=int(input(
                "\n\033[92m=== MENÚ DE USUARIO ===          \033[0m\n"
                "\033[35m  → [1] VER USUARIO                \033[0m\n"
                "\033[35m  → [2] EDITAR USUARIO             \033[0m\n"
                "\033[35m  → [3] BORRAR USUARIO             \033[0m\n"
                "\033[35m  → [4] VOLVER AL MENU DE OPCIONES \033[0m\n"
                "\033[1;35m Seleccione una opción: \033[0m"
                ))
                if usuario_i in (0, 1,2,3,4,5,6):
                    return usuario_i
                else:
                    print(f"\033[91m Opción inválida, intente de nuevo.\033[0m")
            except ValueError:
                print("error de tipeo.")
                return
            except KeyboardInterrupt:
                print("Edición cancelada.")
                return

        if admin:
            func_usuarios = [
                lambda: vista_Usuarios(admin),
                lambda: edicion_usuario(admin),
                lambda: borrado_usuarios(),
            ]
        else:
            func_usuarios = [
                lambda: vista_Usuarios(admin),
                lambda: edicion_usuario(admin),
            ]

        maximo = len(func_usuarios)
        if 1 <= usuario_i <= maximo:
            indice = usuario_i - 1
            func_usuarios[indice]()


        elif usuario_i==4 and admin==True or usuario_i==3 and admin==False:
            print("\033[35mesta saliendo al menu de inicio\033[0m")
            break
        else:
            print("\033[91mOpción no válida\033[0m")