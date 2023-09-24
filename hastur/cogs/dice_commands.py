import logging

import discord
from discord.ext import commands
from discord.ext.commands import BadArgument, Context

from hastur.dice_utils.RollContext import RollContext


class RpgCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self._roll_ctx = RollContext()

    @commands.command(name="roll")
    async def roll(self, ctx: Context, dice_amount: int=1, dice_type: int=6):
        try:
            roll_parameters = (dice_amount, dice_type)
            for result_embed in self._get_roll_result(ctx, roll_parameters):
                await ctx.send(embed=result_embed)
        except BadArgument as ba:
            await ctx.send(discord.Embed(title="EMPTY", description="Podano błędną wartość"))

    def _get_roll_result(self, ctx: Context, roll_parameters: tuple):
        author, guild = self._author_and_guild_from_ctx(ctx)
        strategy = self._roll_ctx.get_strategy(author, guild)
        try:
            strategy.set_roll_parameters(roll_parameters).set_author(author)
            return strategy.get_roll_message()
        except Exception as e:
            logging.error(e)
            return [discord.Embed(title="EMPTY", description="Wystąpił niezydentyfikowany problem")]

    @commands.command(name="set_game")
    async def dice_settings(self, ctx: Context, game: str):
        author, guild = self._author_and_guild_from_ctx(ctx)
        success, strategy = self._roll_ctx.set_strategy(author, guild, game)
        if not success:
            ctx.send(f"Nie znaleziono gry!!! Nie zmieniono z {strategy.NAME}")
        await ctx.send(f"Gra zmieniona na {strategy.NAME}")

    @commands.command(name="check")
    async def check_settings(self, ctx: Context):
        author, guild = self._author_and_guild_from_ctx(ctx)
        strategy = self._roll_ctx.get_strategy(author, guild)
        await ctx.send(f"{strategy.NAME}")

    @staticmethod
    def _author_and_guild_from_ctx(ctx: Context):
        msg = ctx.message
        return msg.author, msg.guild
