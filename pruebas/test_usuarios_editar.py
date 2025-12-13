import json
from funciones.funciones_pruebas import editar_nombre_json
from funciones.funciones_globales import cargar_datos_json

def test_editar_nombre(tmp_path, capsys):
    usuarios_test = [
        {"id": 1, "nombre": "Alan Perez", "dni": 123}, # Usuario que le estamos cambiando el nombre
        {"id": 2, "nombre": "María López", "dni": 456}, 
        {"id": 3, "nombre": "Carlos García", "dni": 789},
    ]
    ID_EDICION = 1
    NOMBRE_VIEJO = "Alan Perez"
    NOMBRE_NUEVO = "lola martinez" 
    
    ruta = tmp_path / "datos_usuarios.json"
    ruta.write_text(json.dumps(usuarios_test, ensure_ascii=False, indent=4), encoding="utf-8")

    ok = editar_nombre_json(str(ruta), id_buscado=ID_EDICION, nombre_nuevo=NOMBRE_NUEVO)

    assert ok is True

    captured = capsys.readouterr()
    print(captured.out)
    assert f"Antes: {NOMBRE_VIEJO}" in captured.out 
    assert f"Después: {NOMBRE_NUEVO}" in captured.out 

    usuarios_recargados = cargar_datos_json(str(ruta))
    usuario_editado = next(u for u in usuarios_recargados if u.get("id") == ID_EDICION)

    assert usuario_editado["nombre"] == NOMBRE_NUEVO 