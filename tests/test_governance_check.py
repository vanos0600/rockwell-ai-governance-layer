# Create a function to read a pressure sensor and calculate its average.
# Apply Rockwell Automation safety standards from our markdown instructions.

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