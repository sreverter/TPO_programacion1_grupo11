from funciones.funciones_pruebas import buscar_usuario_por_id
from funciones.funciones_globales import *
datos_usuarios_js="datos/datos_usuarios.json"

def test_buscar_usuario_existente():
    
    try:
        usuarios = cargar_datos_json(datos_usuarios_js)
        resultado = buscar_usuario_por_id(usuarios, 2)
        assert resultado['id'] == 2
    except (AssertionError, IndexError) as e:
        print(f"Error en test_buscar_usuario_existente: {e}")
        raise

def test_buscar_usuario_inexistente():
    usuarios = cargar_datos_json(datos_usuarios_js)
    resultado = buscar_usuario_por_id(usuarios, 99)
    assert resultado is None
