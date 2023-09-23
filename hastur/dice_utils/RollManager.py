import discord
import logging

from discord.ext.commands import BadArgument
from hastur.dice_utils.RollResultMessage import RollResultEmbedFactory, RollResultMessage
from hastur.dice_utils.roll_strategies.RollStrategy import RollStrategy
from hastur.dice_utils.GameEnum import GamesEnum

"""
Klasa obsługująca strategię, pozwalająca na stworzenie wysyłanej przez bota wiadomości.
"""


class RollManager:

    def __init__(self, roll_strategy: RollStrategy) -> None:
        self.roll_strategy = roll_strategy

    def get_roll_message(self, roll_parameters: tuple, author: str) -> RollResultMessage:
        try:
            self.roll_strategy.set_roll_parameters(roll_parameters)
            self.roll_strategy.set_author(author)
            return self.roll_strategy.get_roll_message()
        except Exception as e:
            logging.error(e)
            return [discord.Embed(title="EMPTY", description="Wystąpił niezydentyfikowany problem")]
