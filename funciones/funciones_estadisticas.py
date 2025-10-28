from iniciacion_listas import datos_globales_reserva, datos_globales_usuarios, ids_shows, datos_globales


# 1. Shows más vendidos
def estadistica_shows_mas_vendidos():
    #se ordena datos globales por la contidad de espectadores 
    sorted_shows = sorted(datos_globales, key=lambda x: x[3], reverse=True)
    #se añade la funcion para que solo puedas ver un cantidad determinada menor a 5
    cantidad = int(input("Seleccione cuántos quiere ver (máximo 5): "))
    #validacion de que no sea mayor a 5
    while cantidad > 5:
        print("Cantidad inválida, el máximo es 5")
        cantidad = int(input("Seleccione cuántos quiere ver (máximo 5): "))
    
    #se aplica un corte a la matriz para que solo se muestre hasta ese punto     
    sorted_shows = sorted_shows[:cantidad]
    #se printea de una forma mas organizada usando anchos 
    print("\n\033[92m=== SHOWS MÁS VENDIDOS ===         \033[0m\n")

    columnas_t = ["ID's", "Tipo de evento", "Duración", "Cant. Espectadores", "Esp. Disponibles", "Fecha"]
    anchos = [12, 20, 10, 8, 14, 14]

    print("-" * 74)
    print("".join(columnas_t[i].ljust(anchos[i]) for i in range(len(columnas_t))))
    print("-" * 74)

    for fila in sorted_shows:
        fila_str = [str(fila[i]).ljust(anchos[i]) for i in range(len(fila))]
        print("".join(fila_str))


# 2. Usuarios activos vs inactivos
def estadistica_mas_user_activos():
    #se suman los usuarios para ver la cantidad de activos o inactivos
    lista_act = sum(1 for i in datos_globales_usuarios if i[5] is True)
    lista_in = sum(1 for i in datos_globales_usuarios if i[5] is False)

    #se crea otra variable que sea igual a las otras
    activo=lista_act
    inactivo=lista_in

    #se verifica que el grafico que vamos a ser sea dentro de limites razonables
    #en usuarios activos
    if lista_act <= 100:
        num_barras_act = lista_act // 10
    else:
        num_barras_act = lista_act // 10

    #en usuarios inactivos
    if lista_in <= 100:
        num_barras_in = lista_in // 10
    else:
        num_barras_in = lista_in // 10
    
    # Asegurar que haya al menos 1 barra si hay usuarios
    if lista_act > 0 and num_barras_act == 0:
        num_barras_act = 1
    if lista_in > 0 and num_barras_in == 0:
        num_barras_in = 1
    #se llama la funcion de creacion de graficos dandoles todos los datos
    crear_Grafico(num_barras_act, num_barras_in, activo, inactivo)


# 3. Shows más recaudados
def shows_mas_recaudados():
    #se crea un diccionario para las recaudaciones
        
        recaudacion = {}  
        #agarra el show y el precio 
        for fila in datos_globales_reserva:
            id_show, precio = fila[3], fila[4]
            recaudacion[id_show] = recaudacion.get(id_show, 0) + precio
        #ordena el diccionario por la recaudacion   
        recaudacion = dict(sorted(recaudacion.items(), key=lambda item: item[1], reverse=True)) 

        print("\n\033[92m=== RECAUDACIÓN POR SHOW ===\033[0m")
        for show, total in recaudacion.items():
            print("Show", show, "→", "$", total)
    


# 4. Usuarios con más reservas
def usuarios_con_mas_re():
    #crea un diccionario
    reservas = {}  

    #agarra el id de usuario por cada reserva que tengas
    for fila in datos_globales_reserva:
        usuario_id = fila[1]
        reservas[usuario_id] = reservas.get(usuario_id, 0) + 1
    reservas = dict(sorted(reservas.items(), key=lambda item: item[1], reverse=True))
    maximo=len(reservas)
        # Pedir posición inicial
    while True:
        try:
            
            principio = int(input(f"Seleccioná desde qué usuario querés empezar a ver (1 - {maximo}): "))
            if principio <=0  or principio > maximo:
                print("Número fuera de rango, intente nuevamente.")
                continue
            break
        except (ValueError,KeyboardInterrupt):
            print("Entrada inválida, intente nuevamente.")
            continue

    # Pedir cantidad a mostrar a partir de esa posición
    while True:
        try:
            subir = int(input(f"¿Cuántos usuarios querés ver a partir del número {principio}? "))
            if subir < 1 or (principio + subir -1) > maximo:
                print("Número inválido, intente nuevamente.")
                continue
            break
        except (ValueError,KeyboardInterrupt):
            print("Entrada inválida, intente nuevamente.")
            continue

    final = principio + subir 

    print("\n\033[92m=== RESERVAS POR USUARIO ===\033[0m")
    for usuario, total in list(reservas.items())[principio:final]:
        print("Usuario", usuario, "→", total)



# Gráfico simple 
def crear_Grafico(num, num2, act, inac):
    #se crea una lista
    hola = []
    #por la cantidad de activos que haya se añade un append para simular un grafico
    for c in range(num):
        hola.append("   _______" if c == 0 else "  |       |")
    #por la cantidad de inactivos que haya se añade un append para simular un grafico
    hola2 = []
    for c2 in range(num2):
        hola2.append("   _______" if c2 == 0 else "  |       |")
    
    #se define un alto con el maximo de largo de ambas listas
    alto = max(len(hola), len(hola2))
    #se hace que si uno es mas largo que el otro se insetan espacios en el mas chico para que no se rompa el grafico
    while len(hola) < alto:
        hola.insert(0, "")
    while len(hola2) < alto:
        hola2.insert(0, "")
    
    #se printean los datos
    print(f'    {"ACTIVO"}     {"INACTIVO"}   ')
    print(f"      {act}          {inac}")
    for i in range(alto):
        print(hola[i].ljust(12) + hola2[i])