from fastapi import APIRouter
from src.app.api.v1.endpoints import predict, summarize, image_infer

router = APIRouter()
router.include_router(predict.router, tags=["predict"])
router.include_router(summarize.router, tags=["summarize"])
router.include_router(image_infer.router, tags=["image"])