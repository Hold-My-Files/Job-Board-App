from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas
from app.db import get_db
from app.auth.oauth2 import get_current_user

router = APIRouter(
    prefix="/applications",
    tags=["applications"],
)

@router.post("/", response_model=schemas.Application)
def create_application(application: schemas.ApplicationCreate, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    try:
        return crud.create_application(db=db, application=application, user_id=current_user.id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))