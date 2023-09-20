import discord
import logging
from hastur.dice_utils.RollResultMessage import RollResultEmbedFactory, RollResultMessage
from hastur.dice_utils.roll_strategies.RollStrategy import RollStrategy
from hastur.dice_utils.GameEnum import GamesEnum

"""
Klasa obsługująca strategię, pozwalająca na stworzenie wysyłanej przez bota wiadomości.
"""

class RollManager():

    def __init__(self, author:str, roll_parameters:tuple, roll_strategy:RollStrategy) -> None:
        self.roll_strategy = roll_strategy
        self.roll_strategy.set_roll_parameters(roll_parameters)
        self.roll_strategy.set_author(author)

    def get_roll_message(self) -> RollResultMessage:
        try:
            return self.roll_strategy.get_roll_message()
        except Exception as e:
            logging.warn(e)
            return [discord.Embed(title="EMPTY", description="Something went wrong")]
