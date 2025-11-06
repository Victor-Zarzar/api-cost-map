from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.schemas.costs import CostOfLiving, CostOfLivingCreate
from app.db.database import get_db
from app.services.auth_service import get_current_user
from app.services.cost_of_living import (
    create_cost as create_cost_svc,
    get_cost as get_cost_svc,
    delete_cost as delete_cost_svc,
)

router = APIRouter()


@router.post("/", response_model=CostOfLiving)
def create_cost(
    cost: CostOfLivingCreate,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user),
):
    return create_cost_svc(db=db, payload=cost)


@router.get("/{cost_id}", response_model=CostOfLiving)
def read_cost(
    cost_id: int,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user),
):
    db_cost = get_cost_svc(db, cost_id=cost_id)
    if db_cost is None:
        raise HTTPException(status_code=404, detail="Cost not found")
    return db_cost


@router.delete("/{cost_id}")
def delete_cost(
    cost_id: int,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user),
):
    success = delete_cost_svc(db, cost_id=cost_id)
    if not success:
        raise HTTPException(status_code=404, detail="Cost not found")
    return {"detail": "Cost deleted"}
