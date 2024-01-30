import uvicorn
import models
from database import engine
from fastapi import FastAPI, APIRouter
from routers import borrow_book, user, book, return_book, auth, admin

# Create all the tables
models.Base.metadata.create_all(bind=engine)

#  Initialize FastAPI
app = FastAPI()

router = APIRouter(prefix="/api", tags=["Root"])

router.include_router(user.router)
router.include_router(book.router)
router.include_router(borrow_book.router)
router.include_router(return_book.router)
router.include_router(auth.router)
router.include_router(admin.router)


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
