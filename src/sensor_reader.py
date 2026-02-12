import random

def read_industrial_sensor(sensor_id: str):
    # VALIDACIÓN: Si el ID no empieza con SENS-, lanzamos ValueError
    if not sensor_id.startswith("SENS-"):
        raise ValueError(f"Invalid ID format: {sensor_id}")

    # SIMULACIÓN DE CONEXIÓN: Si el ID es uno específico, simulamos caída
    if sensor_id == "SENS-ERROR":
        raise ConnectionError("Lost connection to industrial gateway")

    # LÓGICA DE NEGOCIO: Retornamos un valor aleatorio o None (simulando fallo hardware)
    try:
        # Simulamos que a veces el sensor falla (retorna None)
        if random.random() < 0.1: 
            return None
        
        # Retorna un valor entre 0 y 120 (para probar el límite de 100)
        return round(random.uniform(20.0, 110.0), 2)
    except Exception:
        return None