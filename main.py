import uvicorn
import models
from database import engine
from fastapi import FastAPI, APIRouter
from routers import user, book, borrowed_book

# Create all the tables
models.Base.metadata.create_all(bind=engine)

#  Initialize FastAPI
app = FastAPI()
router = APIRouter(prefix="/api", tags=["Root"])
router.include_router(user.router)
router.include_router(book.router)
router.include_router(borrowed_book.router)


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
