import asyncio
import logging
import os

import discord
import dotenv

from dice_utils.Dice import StandardDice
from discord.ext import commands
from enum import Enum

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)
token = dotenv.dotenv_values(dotenv_path="./environ/.env")['TOKEN']

console_handler = logging.StreamHandler()
file_handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")

logger = logging.getLogger("discord_bot")
logger.addHandler(console_handler)
logger.addHandler(file_handler)
bot.logger = logger


@bot.event
async def on_ready():
    bot.logger.info(f'Bot {bot.user.name} ready to work!')
    await bot.change_presence(activity=discord.Game("No game loaded!"))


# @bot.event
# async def on_command_error(ctx, error):
#     if isinstance(error, commands.CommandNotFound):
#         await ctx.send("Podano błędną komendę")
#     elif isinstance(error, commands.MissingRequiredArgument):
#         await ctx.send("Podano błędną wartość")


async def load_cogs() -> None:
    for file in os.listdir(f"{os.path.relpath(os.path.dirname(__file__))}/cogs"):
        if file.endswith(".py") and file != "__init__.py":
            extention = file[:-3]
            try:
                await bot.load_extension(f"cogs.{extention}")
                bot.logger.info(f"Loaded extension {extention}")
            except Exception as e:
                exception = f"{type(e).__name__}"
                bot.logger.error(f"Failed to load extention {extention} \n {exception}")
    # await bot.load_extension("cogs.basic_rpg_commands")

asyncio.run(load_cogs())
bot.run(token)
