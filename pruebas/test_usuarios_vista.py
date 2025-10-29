# pruebas/test_usuarios_vista.py
from funciones.funciones_pruebas import buscar_usuario_por_id

def test_buscar_usuario_existente():
    datos = [
        [1, "Mario", "mario@mail.com"],
        [2, "Ana", "ana@mail.com"],
    ]
    resultado = buscar_usuario_por_id(datos, 2)
    assert resultado == [2, "Ana", "ana@mail.com"]

def test_buscar_usuario_inexistente():
    datos = [
        [1, "Mario", "mario@mail.com"],
        [2, "Ana", "ana@mail.com"],
    ]
    resultado = buscar_usuario_por_id(datos, 99)
    assert resultado is None
