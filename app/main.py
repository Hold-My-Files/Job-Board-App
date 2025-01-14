from fastapi import FastAPI
from app.routers import users, jobs, applications
from app.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(jobs.router)
app.include_router(applications.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Job Board Application"}