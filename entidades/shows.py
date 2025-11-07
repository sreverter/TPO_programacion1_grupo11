def cambio_tipo_evento():
    try:
        tipo= input("\033[4;35mIngrese el nuevo tipo de evento: \033[0m")
        if len(tipo)>0:
            return tipo
        else:
            print("El tipo de evento no puede estar vacío.")
            return "Sin título"
    except (ValueError,KeyboardInterrupt):
        print("sus caracteres no son validos")

def cambio_duracion_evento(shows):
    suma = 0
    suma = int(shows['duracion-show'])
    while True:
        try:
            duracion = int(input("\033[35mIngresa la duración en minutos: \033[0m"))
            if duracion < 0:
                print("Debe ser un número positivo.")
                continue
            if (suma + duracion) > 720:
                print("\033[91mLa duración total supera las 12 horas del día. Consulte con un gerente.\033[0m")
                continue
            return duracion
        except (ValueError, KeyboardInterrupt):
            print("Ingrese caracteres válidos.")
            
def cambio_precio_evento():
    while True:
        try:
            precio=int(input("defina un precio para el show"))
            if precio <=0:
                eleccion=str(input("esta seleccionando una entrada gratuita esta seguro de su decision (s/n) ")).lower()
                
                if eleccion== "s":
                    return precio
                elif eleccion== "n":
                    continue

            elif precio >= 99999:
                eleccion=str(input("esta seleccionando una entrada extremadamente cara esta seguro de su decision (s/n) ")).lower()
                
                if eleccion== "s":
                    return precio
                elif eleccion== "n":
                    continue
            else:
                return precio
        except (ValueError, KeyboardInterrupt):
            print("\033[31mDebe ingresar un número válido.\033[0m")
            continue

        

def nuevo_id_show (datos_shows):
    if datos_shows==[]:
        return 1
    shows_ordenados = sorted(datos_shows, key=lambda x: x['id-show'])
    # for shows in shows_ordenados:
    #     ultimo=shows['id-show']
    def obtener_ultimo_id(lista, i=0):
        # si estamos en el último elemento devolvemos su id
        if i == len(lista) - 1:
            return lista[i]['id-show']
        return obtener_ultimo_id(lista, i + 1)

    ultimo = obtener_ultimo_id(shows_ordenados)
    agregado=ultimo+1
    return agregado