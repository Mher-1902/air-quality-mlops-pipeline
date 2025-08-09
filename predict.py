import pandas as pd
import joblib

# Load the saved model
model = joblib.load("air_quality_model.pkl")

# Example: Make a future dataframe for 10 extra days
future = model.make_future_dataframe(periods=10, freq="D")

# Predict
forecast = model.predict(future)

# Save predictions
forecast.to_csv("air_quality_predictions.csv", index=False)
print("Predictions saved to air_quality_predictions.csv")
