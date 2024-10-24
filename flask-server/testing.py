import joblib

# Test loading the model locally
try:
    model_path = 'flask-server/volkswagen_models/xgboost_model_20240912_134028.joblib'  # Provide the correct model path
    model_object = joblib.load(model_path)
    print(model_object.keys())  # This will show what keys are available in the saved file
except Exception as e:
    print(f"Error loading model locally: {str(e)}")
