import pytest
from src.sensor_reader import read_industrial_sensor

def test_sensor_invalid_id():
    with pytest.raises(ValueError):
        read_industrial_sensor("INVALID-999")

def test_sensor_valid_reading():
    result = read_industrial_sensor("SENS-01")
    assert result is None or isinstance(result, float)


def test_sensor_safety_boundary():
    """Valida que el sensor no devuelva valores físicamente imposibles."""
    result = read_industrial_sensor("SENS-01")
    if result is not None:
        # En una planta real, una temperatura de 500°C activaría una alarma
        assert result <= 100.0, "La temperatura excede el límite de seguridad del sensor"