#Pruebas vista usuarios

def buscar_usuario_por_id(datos, id_buscado):
    """
    Recibe una lista de usuarios (cada usuario es una lista o tupla)
    y devuelve el usuario cuyo ID coincide con 'id_buscado'.
    Si no existe, devuelve None.
    """
    for usuario in datos:
        if usuario['id'] == id_buscado:
            return usuario
    return None


#Pruebas Editar usuarios

import json

def guardar_datos_json(ruta, datos):
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=2)

def cargar_datos_json(ruta):
    with open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)

def editar_nombre_json(ruta, id_buscado, nombre_nuevo):
    usuarios = cargar_datos_json(ruta)
    for usuario in usuarios:
        if usuario.get("id") == id_buscado or usuario.get("id_usuario") == id_buscado:
            print(f"Antes: {usuario['nombre']}")
            usuario["nombre"] = nombre_nuevo
            print(f"Después: {usuario['nombre']}")   # 👈 <--- agregá esta línea
            guardar_datos_json(ruta, usuarios)
            return True
    return False

