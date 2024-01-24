# Copyright (C) 2024 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

""""
TheTeamAlexa is a project of Telegram bots with variety of purposes.
Copyright (c) 2024 -present Team=Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""


import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from AlexaMusic import LOGGER, app, userbot
from AlexaMusic.core.call import Alexa
from AlexaMusic.plugins import ALL_MODULES
from AlexaMusic.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop_policy().get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("AlexaMusic").error("Add Pyrogram string session and then try...")
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("AlexaMusic.plugins" + all_module)
    LOGGER("AlexaMusic.plugins").info("Necessary Modules Imported Successfully.")
    await userbot.start()
    await Alexa.start()
    try:
        await Alexa.stream_call("https://telegra.ph/file/d5bfeb3063904eb6b4aba.jpg")
    except NoActiveGroupCall:
        LOGGER("AlexaMusic").error(
            "[ERROR] - \n\nشغّل الدردشة المرئية ولا تتركها وإلا سأتوقف عن العمل شكراً."
        )
        sys.exit()
    except:
        pass
    await Alexa.decorators()
    LOGGER("AlexaMusic").info("Music Bot Started Successfully")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("AlexaMusic").info("Stopping Music Bot")
