import asyncio
import logging
import os

import discord
import discord.ext.commands
import dotenv

from dice_utils.Dice import StandardDice
from discord.ext import commands
from enum import Enum


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)
token = dotenv.dotenv_values(dotenv_path="./environ/.env")['TOKEN']

discord.utils.setup_logging()

@bot.event
async def on_ready():
    logging.info(f'Bot {bot.user.name} ready to work!')
    await bot.change_presence(activity=discord.Game("No game loaded!"))

@bot.event
async def on_command_error(ctx, error):
    logging.error(error)
    logging.error(type(error))
    if isinstance(error, discord.ext.commands.UserInputError):
        await ctx.send(embed=discord.Embed(title="ERORR", description="Podano błędną wartość"))
    else:
        await ctx.send("Something went wrong")


async def load_cogs() -> None:
    for file in os.listdir(f"{os.path.relpath(os.path.dirname(__file__))}/cogs"):
        if file.endswith(".py") and file != "__init__.py":
            extention = file[:-3]
            try:
                await bot.load_extension(f"cogs.{extention}")
                logging.info(f"Loaded extension {extention}")
            except Exception as e:
                exception = f"{type(e).__name__}"
                logging.error(f"Failed to load extention {extention} \n {exception}")
    # await bot.load_extension("cogs.basic_rpg_commands")

asyncio.run(load_cogs())
bot.run(token)
