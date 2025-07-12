from fastapi import APIRouter, HTTPException
from src.app.models.schemas import PredictionRequest, PredictionResponse
from src.app.services.hf_model import predict

router = APIRouter()

@router.post("/predict", response_model=PredictionResponse)
async def predict(data: PredictionRequest):
    if "[MASK]" not in data.text:
        raise HTTPException(status_code=400, detail="Missing [MASK]")
    return {"results": predict(data.text)}