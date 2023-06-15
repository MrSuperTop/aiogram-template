from aiogram import Router

from package.handlers.add import router as add_router
from package.handlers.edit import router as edit_router
from package.handlers.help import router as help_router
from package.handlers.list import router as list_router
from package.handlers.remove import router as remove_router
from package.handlers.start import router as start_router

router = Router()
router.include_routers(
    list_router,
    start_router,
    add_router,
    remove_router,
    edit_router,
    help_router
)
