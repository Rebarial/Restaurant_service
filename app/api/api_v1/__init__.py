from fastapi import APIRouter
from app.config import settings
from .table import router as table_router
from .reservation import router as reservation_router

router = APIRouter(
    prefix=settings.api.v1.prefix,
)
router.include_router(
    table_router,
    prefix=settings.api.v1.table,
)
router.include_router(
    reservation_router,
    prefix=settings.api.v1.reservation,
)