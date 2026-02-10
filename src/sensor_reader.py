import os
import random
from typing import Optional

class SensorError(Exception):
    pass

def read_industrial_sensor(sensor_id: str) -> Optional[float]:
    """Reads temperature from a specific sensor ID.
    Args:
        sensor_id (str): The unique ID (e.g., "SENS-01").
    Returns:
        float | None: Temperature or None if offline.
    """
    if not sensor_id.startswith("SENS"):
        raise ValueError("Invalid Sensor ID Format")
    
    if random.random() < 0.1:
        return None
        
    return round(random.uniform(20.0, 80.0), 2)
