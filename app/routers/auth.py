from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas.user import UserCreate, UserOut, UserLogin
from ..crud.user import get_user_by_email, create_user
from ..utils.security import verify_password, create_access_token

router = APIRouter(tags=["Authentication"])

@router.post("/register", response_model=UserOut, status_code=201)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email já registrado")
    return create_user(db, user=user)

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = get_user_by_email(db, email=form_data.username)
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=403, detail="Credenciais inválidas")
    access_token = create_access_token(data={"user_id": user.id})
    return {"access_token": access_token, "token_type": "bearer"}