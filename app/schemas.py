from pydantic import BaseModel, EmailStr
from typing import List, Optional

class UserBase(BaseModel):
    email: str
    name: Optional[str] = None
    contact_details: Optional[str] = None
    resume: Optional[str] = None

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    name: str
    contact_details: str
    resume: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    name: str
    contact_details: str
    resume: str

class User(UserBase):
    id: int
    jobs: List["Job"] = []
    applications: List["Application"] = []

    class Config:
        orm_mode = True

class JobBase(BaseModel):
    title: str
    description: str
    location: Optional[str] = None
    job_type: Optional[str] = None

class JobCreate(JobBase):
    pass

class Job(JobBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class ApplicationBase(BaseModel):
    job_id: int

class ApplicationCreate(ApplicationBase):
    pass

class Application(ApplicationBase):
    id: int
    user_id: int
    status: str

    class Config:
        orm_mode = True