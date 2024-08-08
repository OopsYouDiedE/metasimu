import disnake
from disnake.ext import commands
intents = disnake.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=commands.when_mentioned_or(".", "!"), intents=intents)
