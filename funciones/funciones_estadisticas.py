from funciones.funciones_globales import *
datos_usuarios_js = "datos/datos_usuarios.json"
datos_reserva_txt = "datos/datos_reservas.txt"
datos_show_js = "datos/datos_shows.json"

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
    print(f"\033[36mShow con más espectadores:\033[0m {mayor['nombre-show']}")
    print(f"\033[36mEspectadores:\033[0m {mayor['espectadores']}")
    print(f"\033[36mFecha:\033[0m {mayor['fecha']}")

def shows_con_mayor_recaudacion():
    listas_reservas = cargar_datos_txt(datos_reserva_txt)
    id_precios = map(lambda fila: (fila[3], float(fila[4])), listas_reservas)
    recaudacion = {}
    for id_show, precio in id_precios:
        recaudacion[id_show] = recaudacion.get(id_show, 0) + precio
    recaudacion = dict(sorted(recaudacion.items(), key=lambda item: item[1], reverse=True))
    print("\n\033[92m=== RECAUDACIÓN POR SHOW ===\033[0m")
    for show, total in recaudacion.items():
        print(f"Show {show} → $ {total:.2f}")

def usuarios_mas_activos():
    listas_usuarios = cargar_datos_json(datos_usuarios_js)
    lista_act = sum(1 for i in listas_usuarios if i["estado"] is True)
    lista_in = sum(1 for i in listas_usuarios if i["estado"] is False)
    activo = lista_act
    inactivo = lista_in
    altura_max = 10
    maximo = lista_act if lista_act >= lista_in else lista_in
    paso = (maximo + altura_max - 1) // altura_max if maximo > 0 else 1
    num_barras_act = (lista_act + paso - 1) // paso if lista_act > 0 else 0
    num_barras_in = (lista_in + paso - 1) // paso if lista_in > 0 else 0
    if lista_act > 0 and num_barras_act == 0:
        num_barras_act = 1
    if lista_in > 0 and num_barras_in == 0:
        num_barras_in = 1
    crear_Grafico(num_barras_act, num_barras_in, activo, inactivo, paso)

def crear_Grafico(num, num2, act, inac, paso):
    columna_activos = []
    for c in range(num):
        columna_activos.append("   _______" if c == 0 else "  |       |")
    columna_inactivos = []
    for c2 in range(num2):
        columna_inactivos.append("   _______" if c2 == 0 else "  |       |")
    alto = num if num >= num2 else num2
    while len(columna_activos) < alto:
        columna_activos.insert(0, "")
    while len(columna_inactivos) < alto:
        columna_inactivos.insert(0, "")
    print(f'\033[36m    {"ACTIVO"}     {"INACTIVO"}\033[0m')
    print(f"      {act}          {inac}")
    print()
    def imprimir_barras_rec(columna_activos, columna_inactivos, alto, i=0):
        if i >= alto:
            return
        print(columna_activos[i].ljust(12) + columna_inactivos[i])
        imprimir_barras_rec(columna_activos, columna_inactivos, alto, i + 1)
    imprimir_barras_rec(columna_activos, columna_inactivos, alto)
    print("   _______     _______")

def pedir_principio(maximo):
    try:
        principio = int(input(f"\033[36mSeleccioná desde qué usuario querés empezar a ver (1 - {maximo-1}):\033[0m "))
        if principio <= 0 or principio >= maximo:
            print("\033[91mNúmero fuera de rango, intente nuevamente.\033[0m")
            return pedir_principio(maximo)
        return principio
    except (ValueError, KeyboardInterrupt):
        print("\033[91mEntrada inválida, intente nuevamente.\033[0m")
        return pedir_principio(maximo)

def pedir_final(principio, maximo):
    try:
        final = int(input(f"\033[36mSeleccioná hasta qué usuario querés ver ({principio + 1} - {maximo}):\033[0m "))
        if final <= principio or final > maximo:
            print("\033[91mNúmero fuera de rango, debe ser mayor que el inicio y menor o igual que", maximo, "\033[0m")
            return pedir_final(principio, maximo)
        return final
    except (ValueError, KeyboardInterrupt):
        print("\033[91mEntrada inválida, intente nuevamente.\033[0m")
        return pedir_final(principio, maximo)

def usuarios_con_mas_reservas():
    lista_reservas = cargar_datos_txt(datos_reserva_txt)
    reservas = {}
    for fila in lista_reservas:
        usuario_id = fila[1]
        cantidad_entradas = int(fila[5])
        reservas[usuario_id] = reservas.get(usuario_id, 0) + cantidad_entradas
    
    reservas = dict(sorted(reservas.items(), key=lambda item: item[1], reverse=True))
    maximo = len(reservas)


    principio = pedir_principio(maximo)
    final = pedir_final(principio, maximo)
    print(f"\n\033[36mMostrando usuarios con más reservas del puesto {principio} al {final}:\033[0m\n")
    for i, (usuario, cant) in enumerate(reservas.items(), start=1):
        if principio <= i <= final:
            print(f"{i}. Usuario {usuario} - {cant} reservas")
