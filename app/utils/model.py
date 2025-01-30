from tensorflow.keras.models import load_model

def load_trained_model(model_path: str):
    # Load the trained model
    return load_model(model_path)
