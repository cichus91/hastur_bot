import random
from abc import ABC, abstractmethod
from enum import Enum
from dataclasses import dataclass, field

"""
Klasy odpowiedzialne za tworzenie obiektów kości.
"""


class Dice(ABC):

    @abstractmethod
    def roll(self):
        pass

@dataclass
class StandardDice(Dice):

    min_value:int = field(default=1)
    max_value:int = field(default=6)

    @property
    def min_value(self) ->int:
        return self._min_value

    @min_value.setter
    def min_value(self, value) -> None:
        self._min_value =max(1, value)

    @property
    def max_value(self) ->int:
        return self._max_value

    @max_value.setter
    def max_value(self, value) -> None:
        self._max_value = max(1, value)

    def roll(self) -> int:
        roll_result = int(random.randint(self.min_value, self.max_value))
        return roll_result


@dataclass
class SpecialityDice(Dice):

    values_range: list = field(default_factory=list)

    def roll(self):
        roll_result = random.choice(self.values_range)
        return roll_result


class DiceType(Enum):
    D4 = "K4"
    D6 = "K6"
    D8 = "K8"
    D10 = "K10"
    D12 = "K12"
    D20 = "K20"
    D100 = "K100"
