import pytest 
from montacarga import Montacarga


@pytest.fixture
def montacarga():
    cantidad_pasillos = 10
    carga_maxima = 100
    return Montacarga(cantidad_pasillos, carga_maxima) # Instanciamos el montacarga


# Desarrollo del test de encendido y apagado del montacarga
def test_encender_apagar(montacarga):
    montacarga.encender()
    assert montacarga.encendido is True
    montacarga.apagar()
    assert montacarga.encendido is False


# Desarrollo del test de movimiendo del montacarga.
@pytest.mark.parametrize("destino, resultado_esperado,", [
    (7, 7),
    (-1, 0),    # Movimiento fuera de rango
    (20, 0),    # Movimiento fuera de rango
    (5, 5),
    (5, 5)      # Movimiento en el mismo pasillo
])
def test_mover_montacarga(montacarga,destino, resultado_esperado):
    montacarga.__str__()
    montacarga.encender()
    montacarga.mover(destino)
    montacarga.__str__()
    montacarga.apagar()
    assert montacarga.pasillo_actual == resultado_esperado


# Desarrollo del test de carga del montacarga
@pytest.mark.parametrize("carga, resultado_esperado", [
    (50, 50),
    (30, 30),
    (110, 0),       # Aca pasamos el limite de peso del montacarga
    (-10, 0)        # Intentamos hacer una carga negativa de peso
])
def test_cargar_montacarga (montacarga, carga, resultado_esperado):
    montacarga.encender()
    montacarga.cargar_montacarga(carga)
    montacarga.__str__()
    assert montacarga.carga_actual == resultado_esperado


# Desarrollo del test para descarga del montacarga
@pytest.mark.parametrize("descarga, resultado_esperado", [
    (30, 20),
    (40, 10),    
    (60, 50),    # Intenta descargar más de la carga disponible
    (-10, 50)    # Intenta descargar un peso negativo
])
def test_descargar_montacarga(montacarga, descarga, resultado_esperado):
    montacarga.encender()
    montacarga.cargar_montacarga(50)    # Establecemos el peso inicial del montacarga al momento del test
    montacarga.descargar_montacarga(descarga)
    montacarga.__str__()
    assert montacarga.carga_actual == resultado_esperado


