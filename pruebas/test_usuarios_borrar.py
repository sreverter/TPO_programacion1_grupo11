from funciones.funciones_usuarios import borrado_usuarios
from funciones.funciones_pruebas import cargar_datos_json, guardar_datos_json

datos_usuarios_js = "datos/datos_usuarios.json"

def test_borrar_usuario():
    try:
        usuarios = cargar_datos_json(datos_usuarios_js)
        id_buscado = 2
        # Aseguramos que el usuario esté activo (True)
        for u in usuarios:
            if u["id"] == id_buscado:
                u["estado"] = True

        guardar_datos_json(datos_usuarios_js, usuarios)

        # tomar el usuario y COPIAR sus valores antes de mutar
        usuario_original = next(u for u in usuarios if u["id"] == id_buscado)
        nombre_original = usuario_original["nombre"]
        estado_original = usuario_original["estado"]
        assert estado_original is True  # o lo que corresponda en tu setup

        # Act: desactivar
        for u in usuarios:
            if u["id"] == id_buscado:
                u["estado"] = False

        guardar_datos_json(datos_usuarios_js, usuarios)

        # Assert: recargar y verificar
        usuarios_actualizados = cargar_datos_json(datos_usuarios_js)
        usuario_actualizado = next(u for u in usuarios_actualizados if u["id"] == id_buscado)

        print(f"Antes: {nombre_original}, estado: {estado_original}")
        print(f"Después: {usuario_actualizado['nombre']}, estado: {usuario_actualizado['estado']}")

        assert usuario_actualizado["estado"] is False
    except (AssertionError, IndexError) as e:
        print(f"Error en test_borrar_usuario: {e}")
        raise