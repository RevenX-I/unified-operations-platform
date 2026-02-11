from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Unified Operations Platform",
    description="API for the Unified Operations Platform",
    version="0.1.0",
)

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from .routers import auth

app.include_router(auth.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Unified Operations Platform API"}

@app.get("/health")
async def health_check():
    return {"status": "ok"}
