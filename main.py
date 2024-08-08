import os

import disnake
from disnake.ext import commands

from bot_creater import bot
from setting import load, save
import bot_basic_controll_slash
import bot_on_reply
import asyncio

save("pid", os.getpid())









bot.run(os.environ['DISCORD_BOT_TOKEN'])
