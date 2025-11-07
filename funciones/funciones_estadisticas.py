from funciones.funciones_globales import *  #se importa las funciones de carga json
#se define las rutas de lo que vamos a usar
datos_usuarios_js="datos/datos_usuarios.json"
datos_reserva_txt="datos/datos_reservas.txt"
datos_show_js = "datos/datos_shows.json"

# se crea funcion donde se carga el json en una var


def shows_mas_vendidos():
    lista_shows = cargar_datos_json(datos_show_js)

    def buscar_mayor(posicion):
        if posicion == len(lista_shows) - 1:
            return lista_shows[posicion]

        mayor_del_resto = buscar_mayor(posicion + 1)

        if lista_shows[posicion]["espectadores"] > mayor_del_resto["espectadores"]:
            return lista_shows[posicion]
        else:
            return mayor_del_resto

    mayor = buscar_mayor(0)

    print(f"Show con más espectadores: {mayor['nombre-show']}")
    print(f"Espectadores: {mayor['espectadores']}")
    print(f"Fecha: {mayor['fecha']}")

def shows_con_mayor_recaudacion():
    listas_reservas = cargar_datos_txt(datos_reserva_txt)
    print(type(listas_reservas))

    # Usamos map para extraer solo (id_show, precio)
    id_precios = map(lambda fila: (fila[3], float(fila[4])), listas_reservas)

    # Creamos el diccionario de recaudación
    recaudacion = {}
    for id_show, precio in id_precios:
        recaudacion[id_show] = recaudacion.get(id_show, 0) + precio

    # Ordenamos por recaudación (de mayor a menor)
    recaudacion = dict(sorted(recaudacion.items(), key=lambda item: item[1], reverse=True))

    # Mostramos resultados
    print("\n\033[92m=== RECAUDACIÓN POR SHOW ===\033[0m")
    for show, total in recaudacion.items():
        print(f"Show {show} → $ {total:.2f}")


def usuarios_mas_activos():
    listas_usuarios = cargar_datos_json(datos_usuarios_js)
    
    # Contar usuarios activos e inactivos
    lista_act = sum(1 for i in listas_usuarios if i["estado"] is True)
    lista_in = sum(1 for i in listas_usuarios if i["estado"] is False)

    activo = lista_act
    inactivo = lista_in

    # Definir altura máxima del gráfico (en bloques)
    altura_max = 10
    maximo = lista_act if lista_act >= lista_in else lista_in
    paso = (maximo + altura_max - 1) // altura_max if maximo > 0 else 1  # escala sin math.ceil

    # Cantidad de bloques por barra
    num_barras_act = (lista_act + paso - 1) // paso if lista_act > 0 else 0
    num_barras_in = (lista_in + paso - 1) // paso if lista_in > 0 else 0

    # Aseguramos que al menos haya 1 bloque si hay usuarios
    if lista_act > 0 and num_barras_act == 0:
        num_barras_act = 1
    if lista_in > 0 and num_barras_in == 0:
        num_barras_in = 1

    # Llamar a la función que crea el gráfico
    crear_Grafico(num_barras_act, num_barras_in, activo, inactivo, paso)


def crear_Grafico(num, num2, act, inac, paso):
    # Crear las listas que representan las barras
    hola = []
    for c in range(num):
        hola.append("   _______" if c == 0 else "  |       |")

    hola2 = []
    for c2 in range(num2):
        hola2.append("   _______" if c2 == 0 else "  |       |")

    # Ajustar para que ambas tengan la misma altura
    alto = num if num >= num2 else num2
    while len(hola) < alto:
        hola.insert(0, "")
    while len(hola2) < alto:
        hola2.insert(0, "")

    # Encabezado
    print(f'    {"ACTIVO"}     {"INACTIVO"}')
    print(f"      {act}          {inac}")
    print()

    # Mostrar las barras desde arriba
    for i in range(alto):
        print(hola[i].ljust(12) + hola2[i])

    # Mostrar base y escala
    print("   _______     _______")
    #print(f"\nCada bloque ≈ {paso} usuario(s)")

def usuarios_con_mas_reservas():
    lista_reservas = cargar_datos_txt(datos_reserva_txt)
    reservas = {}

    # Contar cuántas reservas tiene cada usuario
    for fila in lista_reservas:
        usuario_id = fila[1]
        reservas[usuario_id] = reservas.get(usuario_id, 0) + 1

    # Ordenar los usuarios según cantidad de reservas (de mayor a menor)
    reservas = dict(sorted(reservas.items(), key=lambda item: item[1], reverse=True))
    maximo = len(reservas)

    # --- Función recursiva para pedir el inicio ---
    def pedir_principio():
        try:
            principio = int(input(f"Seleccioná desde qué usuario querés empezar a ver (1 - {maximo}): "))
            if principio <= 0 or principio > maximo:
                print("Número fuera de rango, intente nuevamente.")
                return pedir_principio()  # llamada recursiva
            return principio
        except (ValueError, KeyboardInterrupt):
            print("Entrada inválida, intente nuevamente.")
            return pedir_principio()  # llamada recursiva

    # --- Función recursiva para pedir el final ---
    def pedir_final(principio):
        try:
            final = int(input(f"Seleccioná hasta qué usuario querés ver ({principio + 1} - {maximo}): "))
            if final <= principio or final > maximo:
                print("Número fuera de rango, debe ser mayor que el inicio y menor o igual que", maximo)
                return pedir_final(principio)
            return final
        except (ValueError, KeyboardInterrupt):
            print("Entrada inválida, intente nuevamente.")
            return pedir_final(principio)

    # Llamadas recursivas controladas
    principio = pedir_principio()
    final = pedir_final(principio)

    # Mostrar resultados dentro del rango
    print(f"\n Mostrando usuarios con más reservas del puesto {principio} al {final}:\n")
    for i, (usuario, cant) in enumerate(reservas.items(), start=1):
        if principio <= i <= final:
            print(f"{i}. Usuario {usuario} - {cant} reservas")
