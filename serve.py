from fastapi import FastAPI
import joblib
import os

app = FastAPI(title="ML Model API")

model = None

def load_model():
    global model
    model_path = "models/model.pkl"
    if os.path.exists(model_path):
        model = joblib.load(model_path)

load_model()

@app.get("/")
def root():
    return {"status": "ML Model API is running"}

@app.get("/health")
def health():
    return {"status": "healthy", "model_loaded": model is not None}

@app.get("/predict")
def predict(x: float, y: float, z: float, w: float):
    if model is None:
        return {"error": "Model not loaded. Run train.py first."}
    prediction = model.predict([[x, y, z, w]])
    return {"prediction": int(prediction[0])}
