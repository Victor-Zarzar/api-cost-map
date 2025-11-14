from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.schemas.auth import Token
from app.core.config import settings
from app.db.database import get_db
from app.core.security.jwt import create_access_token
from app.services.user_service import authenticate

router = APIRouter()


@router.post("/token", response_model=Token)
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    user = authenticate(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Incorrect username or password")
    access_token = create_access_token(
        {"sub": user.username, "role": user.role})
    return {"access_token": access_token, "token_type": "bearer"}
