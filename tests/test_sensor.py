import pytest
from src.sensor_reader import read_industrial_sensor

def test_sensor_invalid_id():
    """Prueba que un ID sin prefijo SENS- dispare un ValueError."""
    with pytest.raises(ValueError):
        read_industrial_sensor("INVALID-999")

def test_sensor_valid_reading():
    """Prueba que el retorno sea un float o None."""
    result = read_industrial_sensor("SENS-01")
    assert result is None or isinstance(result, float)

def test_sensor_safety_boundary():
    """Valida límites físicos de seguridad."""
    # Nota: Como el valor es aleatorio, este test podría fallar si sale > 100.
    # En una entrevista, esto te sirve para explicar el manejo de alertas.
    result = read_industrial_sensor("SENS-01")
    if result is not None:
        assert result <= 100.0, f"Critical: High temperature detected: {result}°C"

def test_sensor_connection_failure():
    """Simula un fallo de conexión crítico."""
    with pytest.raises(ConnectionError):
        # Usamos el ID especial que creamos en el código para disparar el error
        read_industrial_sensor("SENS-ERROR")