import os

from database.models.chat_join_record import ChatJoinRecord
from export.export_filename_generator import ExportFilenameGenerator


class Exporter:
    def __init__(self, filename: str | None = None):
        self.filename = filename

        if self.filename is None:
            self.filename = ExportFilenameGenerator.generate()

    def get_filename(self):
        return self.filename

    async def export(self):
        chat_join_records = await ChatJoinRecord.find_all().to_list()

        with open(self.filename, "w") as file:
            file.write(
                "chat_id,chat_type,chat_title,chat_username,user_id,user_is_bot,user_first_name,user_last_name,user_username,chat_invite_link,chat_invite_link_name,joined_at\n"
            )
            for chat_join_record in chat_join_records:
                chat_id = chat_join_record.chat.id
                chat_type = chat_join_record.chat.type
                chat_title = chat_join_record.chat.title
                chat_username = chat_join_record.chat.username
                user_id = chat_join_record.user.id
                user_is_bot = chat_join_record.user.is_bot
                user_first_name = chat_join_record.user.first_name
                user_last_name = chat_join_record.user.last_name
                user_username = chat_join_record.user.username
                chat_invite_link = (
                    chat_join_record.chat_invite_link.invite_link
                    if chat_join_record.chat_invite_link
                    else None
                )
                chat_invite_link_name = (
                    chat_join_record.chat_invite_link.name
                    if chat_join_record.chat_invite_link
                    else None
                )
                joined_at = chat_join_record.joined_at

                file.write(
                    f"{chat_id},{chat_type},{chat_title},{chat_username},{user_id},{user_is_bot},{user_first_name},{user_last_name},{user_username},{chat_invite_link},{chat_invite_link_name},{joined_at}\n"
                )

    async def delete(self):
        os.remove(self.filename)
