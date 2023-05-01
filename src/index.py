from fastapi import FastAPI
from libmain.routers.root import users_router

app = FastAPI(
    title="FastAPI Backend",
    description="Backend for the FastAPI project",
    version="0.1.0",
)

app.include_router(users_router)


@app.get("/")
def root():
    return {"message": "Hello FastApi"}


@app.get("/health")
def hello():
    return {"message": "Healthy!"}
