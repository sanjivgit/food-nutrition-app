from transformers import pipeline
from functools import lru_cache
import os

@lru_cache
def get_model():
    model_name = os.getenv("HF_MODEL", "distilbert-base-uncased")
    return pipeline("fill-mask", model=model_name)

def predict(input_text: str):
    model = get_model()
    return model(input_text)