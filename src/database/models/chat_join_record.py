from datetime import datetime

from beanie import Document
from pydantic import BaseModel


class ChatModel(BaseModel):
    id: int
    type: str
    title: str | None = None
    username: str | None = None


class UserModel(BaseModel):
    id: int
    is_bot: bool
    first_name: str
    last_name: str | None = None
    username: str | None = None


class ChatInviteLinkModel(BaseModel):
    invite_link: str
    name: str | None = None


class ChatJoinRecord(Document):
    chat: ChatModel
    user: UserModel
    chat_invite_link: ChatInviteLinkModel
    joined_at: datetime
