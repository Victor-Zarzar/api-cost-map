from fastapi import APIRouter, Depends
from app.models.user import User
from app.core.dependencies import AdminOnly

router = APIRouter()


@router.get("/whoami")
def whoami_admin(current_user: User = Depends(AdminOnly)):
    return {
        "username": current_user.username,
        "role": current_user.role,
        "disabled": current_user.disabled,
    }
