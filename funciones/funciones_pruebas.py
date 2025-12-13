from funciones.funciones_globales import cargar_datos_json, inicializar_datos_json

def editar_nombre_json(ruta, id_buscado, nombre_nuevo):
    usuarios = cargar_datos_json(ruta)
    for usuario in usuarios:
        if usuario.get("id") == id_buscado or usuario.get("id_usuario") == id_buscado:
            print(f"Antes: {usuario['nombre']}")
            usuario["nombre"] = nombre_nuevo
            print(f"Después: {usuario['nombre']}")
            inicializar_datos_json(ruta, usuarios)
            return True
    return False

def borrar_usuario_por_id(usuarios, reservas, id_eliminar):
    for u in usuarios:
        if u["id"] == id_eliminar:
            u["estado"] = False

    reservas_filtradas = []
    for r in reservas:
        try:
            id_res = int(r[1])
        except:
            continue
        if id_res != id_eliminar:
            reservas_filtradas.append(r)

    return usuarios, reservas_filtradas

def buscar_usuario_por_id(datos, id_buscado):
    for usuario in datos:
        if usuario['id'] == id_buscado:
            return usuario
    return None

def validar_edad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
    return True

def dividir_numeros(a, b):
    return a / b

