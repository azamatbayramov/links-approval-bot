import logging
from datetime import datetime

from aiogram import Dispatcher
from aiogram.types import ChatJoinRequest

from database.models.chat_join_record import (
    ChatJoinRecord,
    ChatModel,
    UserModel,
    ChatInviteLinkModel,
)
from config import LOG_LEVEL, LOG_FORMAT

logging.basicConfig(level=LOG_LEVEL, format=LOG_FORMAT)

logger = logging.getLogger(__name__)

dp = Dispatcher()


@dp.chat_join_request()
async def chat_join_request_handler(request: ChatJoinRequest) -> None:
    logger.info(
        f"User {request.from_user.id} requested to join chat {request.chat.id} via link {request.invite_link.invite_link}. Approving request."
    )

    await request.approve()

    logger.info(
        f"User {request.from_user.id} joined chat {request.chat.id} via link {request.invite_link.invite_link}. Recording join."
    )

    new_record = ChatJoinRecord(
        chat=ChatModel.model_validate(request.chat, from_attributes=True),
        user=UserModel.model_validate(request.from_user, from_attributes=True),
        invite_link=ChatInviteLinkModel.model_validate(
            request.invite_link, from_attributes=True
        ),
        joined_at=datetime.now(),
    )

    await new_record.insert()

    logger.info(f"User {request.from_user.id} join recorded.")
