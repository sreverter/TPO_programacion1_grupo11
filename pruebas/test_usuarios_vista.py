from funciones.funciones_pruebas import buscar_usuario_por_id

USUARIOS_DE_PRUEBA = [
    {'id': 1, 'nombre': 'Ana'},
    {'id': 2, 'nombre': 'Beto'},
    {'id': 3, 'nombre': 'Cami'},
]

def test_buscar_usuario_existente():

    resultado = buscar_usuario_por_id(USUARIOS_DE_PRUEBA, 2)
    
    assert resultado is not None
    assert resultado['nombre'] == 'Beto' 

def test_buscar_usuario_inexistente():

    resultado = buscar_usuario_por_id(USUARIOS_DE_PRUEBA, 99)
    
    assert resultado is None    
