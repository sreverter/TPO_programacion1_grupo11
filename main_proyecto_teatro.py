from ingreso import *
from menu.menu_reservas import menu_reservas
from menu.menu_usuarios import menu_usuarios
from menu.menu_shows import menu_shows
from menu.menu_estadisticas import menu_estadisticas
from colores import color



#el admin empieza siempre en false
admin=False
#esto se va a usar para empezar el proceso de logeo
ingreso = True
#esto es lo que empieza el programa
start = True

#empieza el programa

while start==True:
    #empieza el logeo
    while ingreso == True:

        #esto determina si se esta registrando o logueando
        destino_ingreso = menu_login()

        #esto determina si es un admin o un usuario
        if destino_ingreso == 0:
            log = login()

            #caso admin
            if log == "ADMIN":
                admin = True
                menu = True
                ingreso = False

            #caso usuario
            elif log == "Usuario":
                admin = False
                menu = True
                ingreso = False

        #caso de registro
        elif destino_ingreso == 1:
            reg=registrar()

    # PROGRAMA PRINCIPAL
    while menu:
        #caso admin
        if admin==True:
            try:
                usuario =int(input(
                    f"\n\033[92m=== MENÚ DE OPCIONES ===\033[0m\n"
                    f"{color["violeta_brillante"]}  → [1] SHOWS              {color["reset"]}\n"
                    f"{color["violeta_brillante"]}  → [2] RESERVAS           {color["reset"]}\n"
                    f"{color["violeta_brillante"]}  → [3] USUARIOS           {color["reset"]}\n"
                    f"{color["violeta_brillante"]}  → [4] ESTADISTICAS       {color["reset"]}\n"
                    f"{color["violeta_brillante"]}  → [5] SALIR DE LA SESIÓN {color["reset"]}\n"
                    f"{color["violeta_brillante"]}  → [6] SALIR DEL PROGRAMA {color["reset"]}\n"
                    f"{color["verde_brillante"]} Seleccione una opción: {color["reset"]}"
                ))
            except (ValueError,KeyboardInterrupt):
                print()
                print("Ingrese un caracter numerico del 1 al 5")
                continue
        #caso usuario
        if admin==False:
            try:
                usuario =int(input(
                    "\n\033[92m=== MENÚ DE OPCIONES ===\033[0m\n"
                    "\033[35m  → [1] SHOWS             \033[0m\n"
                    "\033[35m  → [2] RESERVAS          \033[0m\n"
                    "\033[35m  → [3] USUARIOS          \033[0m\n"
                    "\033[35m  → [4] SALIR DE LA SESIÓN\033[0m\n"
                    "\033[35m  → [5] SALIR DEL PROGRAMA\033[0m\n"
                    "\033[1;35m Seleccione una opción: \033[0m"
                ))
            except (ValueError,KeyboardInterrupt):
                print()
                print("Ingrese un caracter numerico del 1 al 5")
                continue
        # SUBMENÚS
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

        #forma de entrar a los indices
        try:
            maximo = len(func_start)
            if 1 <= usuario <= maximo:
                indice = usuario - 1
                func_start[indice]()
                continue
        except Exception as e:
            print(f"{color['rojo_brillante']}Error en el submenú: {e}{color['reset']}")

        #salida de sesion donde se vuelve el admin a false y empezas el logueo de nuevo
        if (usuario == 5 and admin) or (usuario == 4 and admin == False):
            admin = False
            ingreso = True
            menu = False
            dni_en_uso=[]

        # salida
        elif (usuario == 6 and admin) or (usuario == 5 and admin == False):
            start = False
            break
        
        else:
            print("Su número está fuera de los parametros dados.")