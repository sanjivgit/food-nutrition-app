from fastapi import APIRouter, UploadFile, File, HTTPException
from src.app.services.image_infer_service import classify_image
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/image-classify")
async def image_classify(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Only image files are allowed.")

    result = await classify_image(file)
    return JSONResponse(content={"result": result})