from sqlalchemy.orm import Session
from app import models, schemas
from app.auth.hashing import get_password_hash

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password, name=user.name, contact_details=user.contact_details, resume=user.resume)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_jobs(db: Session, skip: int = 0, limit: int = 10, title: str = None, location: str = None, job_type: str = None):
    query = db.query(models.Job)
    if title:
        query = query.filter(models.Job.title.contains(title))
    if location:
        query = query.filter(models.Job.location.contains(location))
    if job_type:
        query = query.filter(models.Job.job_type.contains(job_type))
    return query.offset(skip).limit(limit).all()

def create_job(db: Session, job: schemas.JobCreate, user_id: int):
    db_job = models.Job(**job.dict(), owner_id=user_id)
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

def create_application(db: Session, application: schemas.ApplicationCreate, user_id: int):
    db_application = models.Application(**application.dict(), user_id=user_id)
    db.add(db_application)
    db.commit()
    db.refresh(db_application)
    return db_application