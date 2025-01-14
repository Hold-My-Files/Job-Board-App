from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas
from app.database import get_db
from app.auth.oauth2 import get_current_user

router = APIRouter(
    prefix="/jobs",
    tags=["jobs"],
)

@router.get("/", response_model=List[schemas.Job])
def read_jobs(skip: int = 0, limit: int = 10, title: str = None, location: str = None, job_type: str = None, db: Session = Depends(get_db)):
    jobs = crud.get_jobs(db, skip=skip, limit=limit, title=title, location=location, job_type=job_type)
    return jobs

@router.post("/", response_model=schemas.Job)
def create_job(job: schemas.JobCreate, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return crud.create_job(db=db, job=job, user_id=current_user.id)