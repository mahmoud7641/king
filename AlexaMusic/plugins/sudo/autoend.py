# Copyright (C) 2024 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

""""
TheTeamAlexa is a project of Telegram bots with variety of purposes.
Copyright (c) 2024 -present Team=Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""


from pyrogram import filters

import config
from strings import get_command
from AlexaMusic import app
from AlexaMusic.misc import SUDOERS
from AlexaMusic.utils.database import autoend_off, autoend_on
from AlexaMusic.utils.decorators.language import language

# Commands
AUTOEND_COMMAND = get_command("AUTOEND_COMMAND")


@app.on_message(filters.command(AUTOEND_COMMAND) & SUDOERS)
async def auto_end_stream(client, message):
    usage = "**طريقة الاستخدام:**\n\n/انهاء تلقائي [enable|disable]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "enable":
        await autoend_on()
        await message.reply_text(
            "تم تفعيل وضع الايقاف التلقائي.\n\nسيغادر المساعد محادثة الفيديو تلقائيًا بعد بضع دقائق عندما لا يكون احد يستمع  مع رسالة تحذيرية."
        )
    elif state == "disable":
        await autoend_off()
        await message.reply_text("تم تعطيل وضع انهاء التشغيل التلقائي.")
    else:
        await message.reply_text(usage)
