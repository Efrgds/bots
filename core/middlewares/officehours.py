from datetime import datetime
from typing import Callable, Awaitable, Dict, Any

from aiogram import BaseMiddleware
from aiogram.types import Message


def office_hours() -> bool:
    return datetime.now().weekday() in (0, 1, 2, 3, 4, 5, 6) and datetime.now().hour in ([i for i in (range(8, 20))])


class OfficeHoursMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any],
    ) -> Any:
        if office_hours():
            return await handler(event, data)

        await event.answer('Время работы бота:\r\n c 8:00 до 20:00.')
