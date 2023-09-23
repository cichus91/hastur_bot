import discord
from hastur.dice_utils.RollManager import RollManager

"""
Klasa przyjmująca dane od bota i wywołująca kontekst rzutu i RollManager w celu pozyskania ostetecznej wiadomości rzutu.
"""


class RollEndpoint:

    def __init__(self, roll_manager: RollManager):
        self.roll_manager = roll_manager

    def get_roll_message(self, roll_parameters: tuple, author: str) -> list[discord.Embed]:
        return self.roll_manager.get_roll_message(roll_parameters, author)

