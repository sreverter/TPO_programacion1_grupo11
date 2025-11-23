import json
from funciones.funciones_usuarios import cargar_datos_json, borrado_usuarios

def test_borrar_usuario(monkeypatch, tmp_path):

    usuarios_test = [
        {"id": 1, "nombre": "Alan", "estado": True},
        {"id": 2, "nombre": "Juan", "estado": True}
    ]

    reservas_test = [
        ["1", "1", "vip", "1000", "150000", "2"],   
        ["2", "2", "campo", "1001", "120000", "3"]  
    ]

    fake_users = tmp_path / "usuarios.json"
    fake_reservas = tmp_path / "reservas.txt"

    fake_users.write_text(json.dumps(usuarios_test, indent=4))

    fake_reservas.write_text(
        "\n".join([",".join(r) for r in reservas_test]))

    monkeypatch.setattr("funciones.funciones_usuarios.datos_usuarios_js", str(fake_users))
    monkeypatch.setattr("funciones.funciones_usuarios.datos_reserva_txt", str(fake_reservas))

    inputs = iter(["2", "1"])  #id, confirmacion
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    borrado_usuarios()

    usuarios_final = cargar_datos_json(str(fake_users))
    reservas_final = fake_reservas.read_text().splitlines()

    user2 = next(u for u in usuarios_final if u["id"] == 2)
    assert user2["estado"] is False

    assert all(",2," not in linea for linea in reservas_final)
