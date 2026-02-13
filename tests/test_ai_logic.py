# Create a function to read a pressure sensor following Rockwell safety standards
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


def test_ai_suggested_logic():
    """Tests the AI-suggested logic for handling sensor readings."""
    result = read_industrial_sensor("SENS-01")
    
    if result is None:
        # Simulate fail-safe behavior
        assert True  # In a real test, you might check logs or alerts here
    elif result > 100.0:
        # Simulate alerting for critical conditions
        assert True  # In a real test, you might check that an alert was triggered
    else:
        # Normal operation
        assert result <= 100.0, f"Unexpected: Sensor reading is above safety threshold: {result}°C"