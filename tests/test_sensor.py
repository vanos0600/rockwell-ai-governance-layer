import pytest
from src.sensor_reader import read_industrial_sensor

def test_sensor_invalid_id():
    """Tests that an ID without the 'SENS-' prefix raises a ValueError."""
    with pytest.raises(ValueError):
        read_industrial_sensor("INVALID-999")

def test_sensor_valid_reading():
    """Tests that the return value is either a float or None."""
    result = read_industrial_sensor("SENS-01")
    assert result is None or isinstance(result, float)

def test_sensor_safety_boundary():
    """Validates physical security limits."""
    # Since the value is randomized, this test might fail if it exceeds 100.
    result = read_industrial_sensor("SENS-01")
    if result is not None:
        assert result <= 100.0, f"Critical: High temperature detected: {result}°C"

def test_sensor_connection_failure():
    """Simulates a critical hardware connection failure."""
    with pytest.raises(ConnectionError):
        # We use the special ID 'SENS-ERROR' to trigger the simulated exception
        read_industrial_sensor("SENS-ERROR")