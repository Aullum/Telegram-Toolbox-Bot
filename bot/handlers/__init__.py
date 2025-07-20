from aiogram import Router

from bot.handlers.base64_handler import router as base64_router
from bot.handlers.fake_profile_handler import router as fake_profile_router
from bot.handlers.json_to_csv_handler import router as json_to_csv_router
from bot.handlers.lorem_handler import router as lorem_router
from bot.handlers.password_handler import router as password_router
from bot.handlers.start_handler import router as start_router

handler_router = Router()
handler_router.include_routers(
    start_router,
    password_router,
    json_to_csv_router,
    base64_router,
    lorem_router,
    fake_profile_router,
)

__all__ = [
    "handler_router",
]
