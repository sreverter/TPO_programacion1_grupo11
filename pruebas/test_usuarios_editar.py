import json
from funciones.funciones_globales import *
datos_usuarios_js="datos/datos_usuarios.json"
from funciones.funciones_pruebas import (
    editar_nombre_json, cargar_datos_json,
)
usuarios_iniciales = cargar_datos_json(datos_usuarios_js)

def test_editar_nombre(tmp_path, capsys):
    # ----- Arrange -----
    # Creamos un JSON temporal con 2 usuarios
    try:
        usuarios_iniciales
        ruta = tmp_path / "datos_usuarios.json"
        ruta.write_text(json.dumps(usuarios_iniciales, ensure_ascii=False, indent=2), encoding="utf-8")

        usuarios_leidos = cargar_datos_json(str(ruta))
        u2 = next(u for u in usuarios_leidos if u.get("id") == 2)
        print("Antes:", u2["nombre"])
    # ----- Act -----
        ok = editar_nombre_json(str(ruta), id_buscado=2, nombre_nuevo="Marta Gimenez")

    # ----- Assert -----
        assert ok is True

        captured = capsys.readouterr()
        print(captured.out)
        assert "Antes: María López" in captured.out
        assert "Después: Marta Gimenez" in captured.out

        usuarios_recargados = cargar_datos_json(str(ruta))
        # buscamos el usuario 2 y revisamos el nombre en el archivo ya guardado
        u2 = next(u for u in usuarios_recargados if u.get("id", u.get("id_usuario")) == 2)
        assert u2["nombre"] == "Marta Gimenez"
    except (AssertionError, IndexError) as e:
        print(f"Error en test_editar_nombre: {e}")
        raise