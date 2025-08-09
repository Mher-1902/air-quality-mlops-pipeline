from fastapi import FastAPI
from fastapi.responses import JSONResponse
import joblib
import pandas as pd
import json

app = FastAPI(title="Air Quality Prediction API")

model = joblib.load("air_quality_model.pkl")

@app.get("/")
def home():
    return {"message": "Air Quality Prediction API is running"}

@app.get("/predict")
def predict(days: int = 10, pretty: bool = False):
    future = model.make_future_dataframe(periods=days, freq="D")
    forecast = model.predict(future)
    simple_forecast = forecast[["ds", "yhat"]].copy()
    
    # Convert Timestamps to strings (ISO format)
    simple_forecast["ds"] = simple_forecast["ds"].dt.strftime("%Y-%m-%d %H:%M:%S")
    
    data = simple_forecast.to_dict(orient="records")
    
    if pretty:
        return JSONResponse(content=json.loads(json.dumps(data, indent=4)))
    else:
        return data
