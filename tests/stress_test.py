import pytest
import random

def read_sensor_fast(sensor_id: str):
    if not sensor_id.startswith("SENS-"):
        raise ValueError("Invalid ID")
    return random.uniform(20.0, 50.0)

def test_stress_logic_adherence():
    with pytest.raises(ValueError):
        read_sensor_fast("INVALID-123")

def test_stress_performance():
    import time
    start_time = time.time()
    for _ in range(100): 
        read_sensor_fast("SENS-01")
    assert time.time() - start_time < 1.0 