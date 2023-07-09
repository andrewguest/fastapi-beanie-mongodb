import secure
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import config
from app.database import MongoDB
from routers.anime_router import router as anime_router

app = FastAPI(
    title="FastAPI example with Beanie and MongoDB",
    description="FastAPI example with Beanie and MongoDB",
    version="0.0.1"
)
secure_headers = secure.Secure()

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
@app.middleware("http")
async def set_secure_headers(request, call_next):
    response = await call_next(request)
    secure_headers.framework.fastapi(response)
    return response


@app.on_event("startup")
async def on_startup():
    await MongoDB.init(config.MONGO_URI, config.MONGO_DB_NAME)

app.include_router(anime_router)
