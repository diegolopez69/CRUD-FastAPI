from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.user_model import User
from app.schemas.user_schema import UserCreate

def get_all_users(db: Session):
    return db.query(User).all()

def get_user_by_id(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def create_user(db: Session, user: UserCreate):
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=409, detail="User already exists")

    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def update_user(db: Session, user_id: int, data: UserCreate):
    user = get_user_by_id(db, user_id)
    for key, value in data.dict().items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return user

def delete_user(db: Session, user_id: int):
    user = get_user_by_id(db, user_id)
    db.delete(user)
    db.commit()
    return {"Message": f"User {user_id} deleted"}