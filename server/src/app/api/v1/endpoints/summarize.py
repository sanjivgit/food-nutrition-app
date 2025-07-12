from fastapi import APIRouter
from src.app.models.summarize import SummarizeRequest, SummarizeResponse
from src.app.services.summarize_service import summarize_text

router = APIRouter()

@router.post("/summarize", response_model=SummarizeResponse)
async def summarize(data: SummarizeRequest):
    summary = summarize_text(data.text)
    return {"summary": summary}