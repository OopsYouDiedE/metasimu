import os

import disnake
from disnake.ext import commands

from bot_creater import bot
from setting import load, save


@bot.event
async def on_message(message: disnake.Message):
    current_pid = load("pid")
    if current_pid != os.getpid():
        print("检测到更新标志，停止处理新消息")
        return  # 如果PID不匹配，不处理消息

    if message.author.bot:
        return

    ctx = await bot.get_context(message)
    if ctx.valid:
        await bot.process_commands(message)
        return

    if message.channel.id not in load("enabled_channels"):
        return

    if ((message.reference is not None and message.reference.resolved.author == bot.user) or
            bot.user.mentioned_in(message)):
        async with message.channel.typing():
            sent_message = await message.reply("Hello" + "⬤")
            await asyncio.sleep(3)
            await sent_message.edit(content="Hello i am" + "⬤")

        embed = disnake.Embed(color=0xE6D47B)
        embed.add_field(name="Input Tokens", value=50)
        embed.add_field(name="Output Tokens", value=200)
        await message.reply("Hello i am Tom", embed=embed)