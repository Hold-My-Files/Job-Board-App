from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.db import get_db
from app.auth.oauth2 import create_access_token
from app.auth.hashing import verify_password

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

@router.post("/token", response_model=dict)
def login_for_access_token(db: Session = Depends(get_db), form_data: schemas.UserCreate = Depends()):
    user = crud.get_user_by_email(db, email=form_data.email)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}