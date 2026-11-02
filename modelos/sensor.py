class Sensor:
    """
    Clase que modela un registro de sensor sanitizado de EcoTech Solutions.
    """
    def __init__(self, sensor_id: str, temperatura: float, ubicacion: str):
        self.sensor_id = sensor_id
        self.temperatura = temperatura
        self.ubicacion = ubicacion

    def to_dict(self) -> dict:
        """Convierte el objeto sensor en un diccionario estándar."""
        return {
            "sensor_id": self.sensor_id,
            "temperatura": self.temperatura,
            "ubicacion": self.ubicacion
        }

    def __str__(self):
        return f"Sensor [{self.sensor_id}] - Temp: {self.temperatura}°C - Ubicación: {self.ubicacion}"