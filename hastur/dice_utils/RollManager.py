import discord
import logging

from hastur.dice_utils.model.RollResultMessage import RollResultMessage
from hastur.dice_utils.roll_strategies.RollStrategy import RollStrategy

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
