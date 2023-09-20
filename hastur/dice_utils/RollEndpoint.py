import discord
from hastur.dice_utils.RollContext import RollContext
from hastur.dice_utils.RollManager import RollManager

"""
Klasa przyjmująca dane od bota i wywołująca kontekst rzutu i RollManager w celu pozyskania ostetecznej wiadomości rzutu.
"""


class RollEndpoint:

    def get_roll_message(self, dice_amount:int, dice_type:int, game:str, author:str) ->list[discord.Embed]:
        roll_parameters = (dice_amount, dice_type)
        roll_strategy = RollContext().match_roll_strategy(game=game)
        roll_manager = RollManager(roll_parameters=roll_parameters, author=author, roll_strategy=roll_strategy)
        return roll_manager.get_roll_message()
