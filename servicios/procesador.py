from modelos.sensor import Sensor

def limpiar_registro_sensor(registro_raw: dict) -> dict:
    """
    Punto A: Normaliza un diccionario crudo de un sensor.
    Retorna un nuevo diccionario estandarizado.
    """
    # 1. Limpiar el ID (eliminando espacios sobrantes)
    sensor_id_limpio = registro_raw.get("sensor_id", "").strip()
    
    # 2. Limpiar la temperatura (remover 'C' y convertir a float)
    temp_raw = str(registro_raw.get("temperatura", "0"))
    temp_limpia = temp_raw.upper().replace("C", "").strip()
    try:
        temperatura_float = float(temp_limpia)
    except ValueError:
        temperatura_float = 0.0  # Valor por defecto seguro ante datos corruptos
        
    # 3. Asignar ubicación por defecto si no existe o está vacía
    ubicacion_raw = registro_raw.get("ubicacion")
    if ubicacion_raw and ubicacion_raw.strip():
        ubicacion_limpia = ubicacion_raw.strip()
    else:
        ubicacion_limpia = "Planta Desconocida"  # Valor por defecto seguro
        
    # Creamos una instancia de la clase Sensor y la convertimos a diccionario
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
        
        # Evaluar si supera el umbral de temperatura configurado
        if temp > umbral_temperatura:
            lista_sensores_alerta.append(sensor["sensor_id"])
            
    # Calcular el promedio térmico global de la planta
    promedio_temperatura = suma_temperaturas / total_sensores
    
    return lista_sensores_alerta, promedio_temperatura