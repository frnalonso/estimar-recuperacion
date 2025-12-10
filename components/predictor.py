# components/predictor.py

import os
import joblib
import pandas as pd

# Carpeta raíz del proyecto (una arriba de /components)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Ruta al modelo dentro de /models
MODEL_PATH = os.path.join(BASE_DIR, "models", "mejor_modelo.joblib")

_modelo = None  # cache en memoria


def get_model():
    """
    Carga el modelo sólo una vez y lo reutiliza.
    """
    global _modelo
    if _modelo is None:
        _modelo = joblib.load(MODEL_PATH)
    return _modelo


def predecir_dias_baja(edad_en_lesion, zona, gravedad_clinica, lesion, lesiones_previas_totales, edad):
    """
    Arma el DataFrame con las columnas que usaste al entrenar
    y devuelve la predicción como float.
    """
    modelo = get_model()

    nueva_fila = pd.DataFrame([{
        "edad_en_lesion": edad_en_lesion,
        "zona_lesion": zona,
        "gravedad_clinica": gravedad_clinica,
        "lesion": lesion,
        "lesiones_previas_totales": lesiones_previas_totales,
        "edad": edad
    }])

    pred = modelo.predict(nueva_fila)[0]
    return float(pred)
