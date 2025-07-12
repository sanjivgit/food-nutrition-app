from fastapi import FastAPI
import uvicorn
from src.app.api.v1 import router as v1_router

app = FastAPI(title="AI API")

app.include_router(v1_router.router, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run("src.app.main:app", host="0.0.0.0", port=8000, reload=True)
