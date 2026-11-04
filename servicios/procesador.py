from modelos.sensor import Sensor
def limpiar_registro_sensor(registro_raw: dict) -> dict:
    """
    Punto A: Normaliza un diccionario crudo de un sensor.
    Retorna un nuevo diccionario estandarizado.
    """
    sensor_id_limpio = registro_raw.get("sensor_id", "").strip()
    temp_raw = str(registro_raw.get("temperatura", "0"))
    temp_limpia = temp_raw.upper().replace("C", "").strip()
    try:
        temperatura_float = float(temp_limpia)
    except ValueError:
        temperatura_float = 0.0  
    ubicacion_raw = registro_raw.get("ubicacion")
    if ubicacion_raw and ubicacion_raw.strip():
        ubicacion_limpia = ubicacion_raw.strip()
    else:
        ubicacion_limpia = "Planta Desconocida"  # Valor por defecto seguro
    sensor_obj = Sensor(sensor_id_limpio, temperatura_float, ubicacion_limpia)
    return sensor_obj.to_dict()
def generar_resumen_sensores(lista_sensores_limpios: list, umbral_temperatura: float) -> tuple:
    """
    Punto B: Procesa la lista de sensores limpios y un umbral.
    Retorna una tupla: (lista_sensores_alerta, promedio_temperatura)
    """
    lista_sensores_alerta = []
    suma_temperaturas = 0.0
    total_sensores = len(lista_sensores_limpios)
    if total_sensores == 0:
        return [], 0.0
    for sensor in lista_sensores_limpios:
        temp = sensor["temperatura"]
        suma_temperaturas += temp
        if temp > umbral_temperatura:
            lista_sensores_alerta.append(sensor["sensor_id"])
    promedio_temperatura = suma_temperaturas / total_sensores
    return lista_sensores_alerta, promedio_temperatura