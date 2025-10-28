from funciones.funciones_usuarios import vista_Usuarios,borrado_usuarios,edicion_usuario

def menu_usuarios(admin):
    while True:
        if admin==False:
                try:
                    usuario_i=int(input(
                    "\n\033[92m=== MENÚ DE USUARIO ===          \033[0m\n"
                    "\033[35m  → [1] VER USUARIO                \033[0m\n"
                    "\033[35m  → [2] EDITAR Usuario             \033[0m\n"
                    "\033[35m  → [3] VOLVER AL MENU DE OPCIONES \033[0m\n"
                    "\033[1;35m Seleccione una opción: \033[0m"
                    ))
                except (ValueError,KeyboardInterrupt):
                    print() 
                    print("\033[91mcoloque caracteres validos\033[0m")
                    continue
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
            except (ValueError,KeyboardInterrupt):
                print()
                print("\033[91mcoloque caracteres validos\033[0m")
                continue

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
            print("esta saliendo al menu de inicio")
            break
        #se delimita las opciones que podes con esto para que si elije mal alguna opcion pueda volver a ver las opciones y elija bien
        else:
            print("\033[91mOpción no válida\033[0m")