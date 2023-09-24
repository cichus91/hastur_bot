import logging

import discord
from typing import List
from hastur.dice_utils.model.RollResultMessage import RollResultEmbedFactory
from hastur.dice_utils.roll_strategies.RollStrategy import RollStrategy
from hastur.dice_utils.model.RollResult import RollResult
from hastur.dice_utils.model.Dice import StandardDice
from hastur.dice_utils.rol_rules.RollRule import RollRule, RiskRoll


class TrophyDarkStrategy(RollStrategy):

    NAME = "Trophy Dark"
    CMD_NAME = "trophy"

    def __init__(self):
        super().__init__()
        self.dice = StandardDice(min_value=1, max_value=6)

    def get_roll_message(self):
        embeds = list()
        light_dice_embed = self.light_dice_embed().to_embed()
        dark_dice_embed = self.dark_dice_embed().to_embed()
        embeds.append(light_dice_embed)
        embeds.append(dark_dice_embed)
        return embeds


    def build_roll_result_embed(self, color:discord.Color, author:str, result_description:str, roll_result:List):
        return RollResultEmbedFactory().build_roll_embed(color=color,
                                                  author=author,
                                                  result_description=result_description,
                                                  roll_result=roll_result)

    def dark_dice_embed(self):
        try:
            dark_dice_results_list = [self.dice.roll() for i in range(self.roll_parameters[1])]
            dark_dice_result = RiskRoll(roll_result=max(dark_dice_results_list)).check()
            dark_dice_result_embed = self.build_roll_result_embed(color=discord.Colour.default(),
                                                                       author=self.author,
                                                                       roll_result=dark_dice_result,
                                                                  result_description=dark_dice_results_list)
            return dark_dice_result_embed
        except Exception as e:
            logging.warn(e)

    def light_dice_embed(self):
        light_dice_results_list = [self.dice.roll() for i in range(self.roll_parameters[0])]
        light_dice_result = RiskRoll(roll_result=max(light_dice_results_list)).check()
        light_dice_result_embed = self.build_roll_result_embed(color=discord.Colour.from_rgb(255, 255, 255),
                                                                   author=self.author,
                                                                   roll_result=light_dice_result,
                                                               result_description=light_dice_results_list)
        return light_dice_result_embed

    def get_roll_result(self, roll_rule:RollRule):
        #todo co to robi?
        roll_result = RollResult()
        roll_rule = roll_rule
        roll_result.set_result(roll_rule)

