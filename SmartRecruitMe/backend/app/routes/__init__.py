from .auth import router as auth_router
from .candidates import router as candidates_router
from .recruiters import router as recruiters_router

__all__ = ["auth_router", "candidates_router", "recruiters_router"]
