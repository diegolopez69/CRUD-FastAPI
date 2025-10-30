from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app.schemas import UserCreate, UserResponse
from app.controllers import (
    create_user,
    get_all_users,
    get_user_by_id,
    update_user,
    delete_user,
)

router = APIRouter()

@router.post("/users", response_model=UserResponse)
def create(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.get("/users", response_model=list[UserResponse])
def get_all(db: Session = Depends(get_db)):
    return get_all_users(db)

@router.get("/users/{user_id}", response_model=UserResponse)
def get_one(user_id: int, db: Session = Depends(get_db)):
    return get_user_by_id(db, user_id)

@router.put("/users/{user_id}", response_model=UserResponse)
def update(user_id: int, data: UserCreate, db: Session = Depends(get_db)):
    return update_user(db, user_id, data)

@router.delete("/users/{user_id}")
def delete(user_id: int, db: Session = Depends(get_db)):
    return delete_user(db, user_id)