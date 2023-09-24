import discord
from typing import List

from hastur.dice_utils.model.Dice import StandardDice
from hastur.dice_utils.model.RollResultMessage import RollResultEmbedFactory
from hastur.dice_utils.roll_strategies.RollStrategy import RollStrategy
from hastur.dice_utils.model.RollResult import RollResult


class StandardRollStrategy(RollStrategy):

    NAME = "Standard"
    CMD_NAME = "standard"

    def get_roll_message(self):
        embeds = list()
        dice_embed = self.dice_embed().to_embed()
        embeds.append(dice_embed)
        return embeds

    def build_roll_result_embed(self, color:discord.Color, author:str, result_description:str, roll_result:List):
        return RollResultEmbedFactory().build_roll_embed(color=color,
                                                  author=author,
                                                  result_description=result_description,
                                                  roll_result=roll_result)

    def dice_embed(self):
        dice = StandardDice(min_value=1, max_value=self.roll_parameters[1])
        dice_results_list = [dice.roll() for x in range(self.roll_parameters[0])]
        dice_embed = self.build_roll_result_embed(color=discord.Color.default(),
                                                                   author=self.author,
                                                                   roll_result=RollResult.Result.STANDARD_ROLL.value,
                                                              result_description=dice_results_list)
        return dice_embed

    def get_roll_result(self):
        pass



