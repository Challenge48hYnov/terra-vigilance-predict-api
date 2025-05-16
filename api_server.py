import joblib
import uvicorn
import datetime
import pandas as pd
import xgboost as xgb
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

# 1. Définition du schéma d'entrée aligné sur les features utilisées (X)
class InputData(BaseModel):
    sismicite: float
    concentration_gaz: float
    pluie_totale: float
    timestamp: float
    quartier: int

# 2. Chargement du préprocesseur et du modèle XGBoost
try:
    preprocessor = joblib.load('preprocessor.pkl')
    xgb_model = xgb.XGBClassifier()
    xgb_model.load_model('xgb_model.json')
except Exception as e:
    raise RuntimeError(f"Erreur lors du chargement des artefacts: {e}")

# 3. Mapping du code vers le label
mapping = {
    0: 'aucun',
    1: "['innondation']",
    2: "['seisme']",
    3: "['innondation', 'seisme']"
}

app = FastAPI()

@app.post('/predict')
def predict(data: InputData):
    # Conversion en DataFrame avec uniquement les colonnes attendues
    df = pd.DataFrame([data.dict()])
    try:
        X_proc = preprocessor.transform(df)
    except Exception as e:
        # colonne manquante ou problème de format
        raise HTTPException(status_code=400, detail=f"Erreur de prétraitement: {e}")

    # Prédiction
    try:
        pred_code = int(xgb_model.predict(X_proc)[0])
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de la prédiction: {e}")

    pred_label = mapping.get(pred_code, 'inconnu')
    return {
        'prediction_code': pred_code,
        'prediction_label': pred_label
    }