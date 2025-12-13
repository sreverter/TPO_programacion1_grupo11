from funciones.funciones_pruebas import validar_edad, dividir_numeros
import pytest
def test_validar_edad_levanta_excepcion():
    with pytest.raises(ValueError):
        validar_edad(-5)
        
def test_division_por_cero():
    with pytest.raises(ZeroDivisionError):
        dividir_numeros(10, 0)