import random

def read_industrial_sensor(sensor_id: str):
    """
    Reads data from an industrial sensor with built-in validation and error handling.
    
    Args:
        sensor_id (str): The unique identifier for the sensor. Must start with 'SENS-'.
        
    Returns:
        float | None: The sensor reading value or None if a hardware failure occurs.
        
    Raises:
        ValueError: If the sensor_id format is invalid.
        ConnectionError: If a simulated hardware connection failure occurs.
    """
    
    # VALIDATION: If the ID does not start with SENS-, raise a ValueError
    if not sensor_id.startswith("SENS-"):
        raise ValueError(f"Invalid ID format: {sensor_id}")

    # CONNECTION SIMULATION: If the ID matches the error trigger, simulate a gateway failure
    if sensor_id == "SENS-ERROR":
        raise ConnectionError("Lost connection to industrial gateway")

    # BUSINESS LOGIC: Return a random value or None (simulating hardware failure)
    try:
        # Simulate a 10% chance of sensor failure (returning None)
        if random.random() < 0.1: 
            return None
        
        # Return a value between 0 and 120 (to test the 100.0 safety threshold)
        return round(random.uniform(20.0, 110.0), 2)
        
    except Exception:
        # Fail-safe: return None if any unexpected error occurs during reading
        return None