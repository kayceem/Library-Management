import uvicorn
import models
from database import engine
from fastapi import FastAPI, APIRouter

# Create all the tables
models.Base.metadata.create_all(bind=engine)

#  Initialize FastAPI
app = FastAPI()
router = APIRouter(prefix="/api", tags=["Root"])


@router.get("/")
async def home():
    return {"message": "OK"}


app.include_router(router)
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
