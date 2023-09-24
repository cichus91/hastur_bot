from hastur.dice_utils.model.RollResultMessage import RollResultMessage, RollResultEmbed
from abc import ABC, abstractmethod

"""Szablon do tworzenia nowych klas zasad dla kolejnych gier
todo zrobienie wersji obsługującej JSON
"""


class RollStrategy(ABC):

    def __init__(self):
        self.roll_result_message = RollResultMessage()
        self.roll_parameters = tuple()
        self.author = ''

    def add_roll_result_embed_to_roll_result_message(self, roll_result_embed: RollResultEmbed):
        self.roll_result_message.embed_list.append(roll_result_embed)

    def set_roll_parameters(self, roll_parameters: tuple):
        if len(roll_parameters) > 0 and roll_parameters is not None:
            self.roll_parameters = roll_parameters
            return self

    def set_author(self, author):
        if author is not None:
            self.author = author
            return self

    @abstractmethod
    def get_roll_message(self):
        pass

    @abstractmethod
    def build_roll_result_embed(self):
        pass

    @abstractmethod
    def get_roll_result(self):
        pass
