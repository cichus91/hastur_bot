import discord
from typing import List

class RollResultMessage():

    def __init__(self) -> None:
        self.embed_list = list()

class RollResultEmbed():

    def __init__(self):
        self.color
        self.author
        self.result_description
        self.roll_result

    def color(self, color:discord.Color):
        if color is not None:
            self.color = color
        else:
            self.color = discord.Color.default()
        return self

    def author(self, author:str):
        if author is not None:
            self.author = author
        else:
            self.author = "empty"
        return self

    def result_description(self, result_description:str):
        if result_description is not None:
            self.result_description = result_description
        else:
            self.result_description = "empty"
        return self

    def roll_result(self, roll_result:List):
        if roll_result is not None:
            self.roll_result = roll_result
        else:
            self.roll_result = list()
        return self

    def to_embed(self):
        embed = discord.Embed(color=self.color, title=self.roll_result, description=self.result_description)
        embed.set_author(name= self.author)
        return embed

class RollResultEmbedFactory():

    def build_roll_embed(self, color:discord.Color, author:str, result_description:str, roll_result:List) -> RollResultEmbed:
        return RollResultEmbed().color(color).author(author).result_description(result_description).roll_result(roll_result)

