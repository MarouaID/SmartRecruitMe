from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models import Notification
from app.auth import get_current_candidate, get_current_recruiter

router = APIRouter(prefix="/api/notifications", tags=["Notifications"])

def _serialize_notification(n: Notification):
    return {
        "id": n.id,
        "message": n.message,
        "is_read": bool(n.is_read),
        "created_at": n.created_at.isoformat(),
    }

@router.get("/candidate", response_model=List[dict])
def get_candidate_notifications(
    current_user=Depends(get_current_candidate),
    db: Session = Depends(get_db),
):
    notifications = (
        db.query(Notification)
        .filter(Notification.user_id == current_user.id)
        .order_by(Notification.created_at.desc())
        .all()
    )
    return [_serialize_notification(n) for n in notifications]

@router.get("/recruiter", response_model=List[dict])
def get_recruiter_notifications(
    current_user=Depends(get_current_recruiter),
    db: Session = Depends(get_db),
):
    notifications = (
        db.query(Notification)
        .filter(Notification.user_id == current_user.id)
        .order_by(Notification.created_at.desc())
        .all()
    )
    return [_serialize_notification(n) for n in notifications]

@router.post("/mark-read")
def mark_read(
    ids: List[int],
    current_user=Depends(get_current_candidate),
    db: Session = Depends(get_db),
):
    """Mark notifications as read for a candidate."""
    updated = (
        db.query(Notification)
        .filter(Notification.user_id == current_user.id, Notification.id.in_(ids))
        .all()
    )
    for n in updated:
        n.is_read = 1
    db.commit()
    return {"updated": len(updated)}
