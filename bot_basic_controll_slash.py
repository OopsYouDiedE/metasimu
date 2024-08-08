import disnake
from disnake.ext import commands

from bot_creater import bot
from setting import load, save


@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')


@bot.slash_command(name="enable", description="Enable a channel for bot interaction")
@commands.default_member_permissions(administrator=True)
async def enable_channel(inter: disnake.ApplicationCommandInteraction, channel: disnake.TextChannel):
    enabled_channels = load("enabled_channels", [])
    if channel.id not in enabled_channels:
        enabled_channels.add(channel.id)
        save("enabled_channels", enabled_channels)
        await inter.send(f"Channel {channel.mention} has been enabled for bot interaction.")
    else:
        await inter.send(f"Channel {channel.mention} is already enabled.")


@bot.slash_command(name="disable", description="Disable a channel for bot interaction")
@commands.default_member_permissions(administrator=True)
async def disable_channel(inter: disnake.ApplicationCommandInteraction, channel: disnake.TextChannel):
    enabled_channels = load("enabled_channels", [])
    if channel.id in enabled_channels:
        enabled_channels.remove(channel.id)
        save("enabled_channels", enabled_channels)
        await inter.send(f"Channel {channel.mention} has been disabled for bot interaction.")
    else:
        await inter.send(f"Channel {channel.mention} is not enabled.")
