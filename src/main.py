import asyncio
import logging
from datetime import datetime

from aiogram import Dispatcher, Bot
from aiogram.filters import Command
from aiogram.types import ChatJoinRequest, Message, FSInputFile

from config import LOG_LEVEL, LOG_FORMAT, BOT_TOKEN, BOT_ADMIN_USERNAMES
from database.db import init_db
from database.models.chat_join_record import (
    ChatJoinRecord,
    ChatModel,
    UserModel,
    ChatInviteLinkModel,
)
from export.exporter import Exporter

logging.basicConfig(level=LOG_LEVEL, format=LOG_FORMAT)

logger = logging.getLogger(__name__)

dp = Dispatcher()


@dp.chat_join_request()
async def chat_join_request_handler(request: ChatJoinRequest) -> None:
    chat = ChatModel.model_validate(request.chat, from_attributes=True)
    user = UserModel.model_validate(request.from_user, from_attributes=True)

    chat_invite_link = None
    if request.invite_link:
        chat_invite_link = ChatInviteLinkModel.model_validate(request.invite_link, from_attributes=True)

    logger.info(f"Handling chat join request from user {user.id} to chat {chat.id} with invite link {chat_invite_link.invite_link if chat_invite_link else None}")

    await request.approve()

    new_record = ChatJoinRecord(
        chat=chat,
        user=user,
        chat_invite_link=chat_invite_link,
        joined_at=datetime.now(),
    )

    await new_record.insert()


@dp.message(Command("export"))
async def start_handler(message: Message):
    if message.from_user.username not in BOT_ADMIN_USERNAMES:
        return

    exporter = Exporter()

    await exporter.export()

    await message.answer_document(FSInputFile(exporter.get_filename()))

    await exporter.delete()


async def main():
    logger.info("Starting bot")

    logger.info("Initializing database")
    await init_db()

    bot = Bot(token=BOT_TOKEN)

    logger.info("Starting bot polling")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
