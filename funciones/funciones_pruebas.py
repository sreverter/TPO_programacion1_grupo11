def buscar_usuario_por_id(datos, id_buscado):
    """
    Recibe una lista de usuarios (cada usuario es una lista o tupla)
    y devuelve el usuario cuyo ID coincide con 'id_buscado'.
    Si no existe, devuelve None.
    """
    for usuario in datos:
        if usuario[0] == id_buscado:
            return usuario
    return None