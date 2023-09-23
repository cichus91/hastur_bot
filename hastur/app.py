import asyncio
import discord
import logging
from discord.ext import commands

from hastur.cogs.dice_commands import RpgCommands


class HasturBot(commands.Bot):

    COG_CLS = [RpgCommands]

    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super(HasturBot, self).__init__(command_prefix="!", intents=intents)
        self._logger = logging.getLogger("discord")

    async def setup_hook(self):
        # Add cogs concurrently
        await asyncio.gather(*[self._load_cog(cog_cls(self)) for cog_cls in self.COG_CLS])

    async def _load_cog(self, cog: commands.Cog):
        try:
            await self.add_cog(cog)
            self._logger.info(f"Loaded {cog.qualified_name}")
        except Exception as e:
            self._logger.error(f"Failed to load {cog.qualified_name}:\n {e}")

    async def on_ready(self):
        self._logger.info(f'Bot {self.user.name} ready to work!')
        await self.change_presence(activity=discord.Game("No game loaded!"))

    #async def on_command_error(
    #    self, ctx: commands.context.Context[commands.bot.BotT], err: commands.errors.CommandError
    #) -> None:
    #    if isinstance(err, commands.CommandNotFound):
    #        await ctx.send("Podano błędną komendę")
    #    elif isinstance(err, commands.MissingRequiredArgument):
    #        await ctx.send("Podano błędną wartość")
