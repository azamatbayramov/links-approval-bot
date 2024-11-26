from beanie import init_beanie
from motor import motor_asyncio

from config import DB_HOST, DB_NAME
from database.models.chat_join_record import ChatJoinRecord

ALL_MODELS = [ChatJoinRecord]


async def init_db():
    client = motor_asyncio.AsyncIOMotorClient(DB_HOST)
    database = client[DB_NAME]
    await init_beanie(database=database, document_models=ALL_MODELS)
