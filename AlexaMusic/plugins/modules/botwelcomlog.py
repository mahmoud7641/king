# This code is written by (C) TheTeamAlexa bot will send message to log group when someone add
# this bot to new group make sure to star all projects
# Copyright (C) 2021-2024 by Alexa_Help@ Github, < TheTeamAlexa >.
# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group
# All rights reserved. © Alisha © Alexa © Yukki

from pyrogram import Client, filters
from pyrogram.types import Message
from AlexaMusic import app
from AlexaMusic.utils.database import get_served_chats
from config import LOG_GROUP_ID


async def lul_message(chat_id: int, message: str):
    await app.send_message(chat_id=chat_id, text=message)


@app.on_message(filters.new_chat_members)
async def on_new_chat_members(client: Client, message: Message):
    if (await client.get_me()).id in [user.id for user in message.new_chat_members]:
        added_by = message.from_user.first_name if message.from_user else "ᴜɴᴋɴᴏᴡɴ ᴜsᴇʀ"
        matlabi_jhanto = message.chat.title
        served_chats = len(await get_served_chats())
        chat_id = message.chat.id
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "جروب خاص"
        lemda_text = f" تم اضافة البوت لجروب جديد..\n\n┏━━━━━━━━━━━━━━━━━┓\n┣★ **الجروب** › : {matlabi_jhanto}\n┣★ **ايدي الجروب** › : {chat_id}\n┣★ **اسم الجروب** › : {chatusername}\n┣★ **عدد الجروبات** › : {served_chats}\n┣★ **تمت الاضافة بواسطة** › :\n┗━━━ {added_by}"
        await lul_message(LOG_GROUP_ID, lemda_text)
