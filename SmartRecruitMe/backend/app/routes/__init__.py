from .auth import router as auth_router
from .candidates import router as candidates_router
from .recruiters import router as recruiters_router
from .chat import router as chat_router
from .notifications import router as notifications_router

__all__ = [
    "auth_router",
    "candidates_router",
    "recruiters_router",
    "chat_router",
    "notifications_router",
]
