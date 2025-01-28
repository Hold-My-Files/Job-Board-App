from fastapi import FastAPI
from routers import users, jobs, applications
from db import engine, Base, init_db
from dotenv import load_dotenv
import uvicorn
import os
from contextlib import asynccontextmanager

load_dotenv()

# Base.metadata.create_all(bind=engine)
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup event
    init_db()
    yield
    # Shutdown event (if needed)
    # await shutdown()

app = FastAPI(lifespan=lifespan)

app.include_router(users.router)
app.include_router(jobs.router)
app.include_router(applications.router)




@app.get("/")
def read_root():
    return {"message": "Welcome to the Job Board Application"}


if __name__ == "__main__":
    if not os.path.exists("db.sqlite"):
        init_db()
    uvicorn.run(app, host="127.0.0.1", port=8000)