import random
from abc import ABC, abstractmethod
from enum import Enum
from dataclasses import dataclass, field

from hastur.dice_utils.DiceException import DiceException

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
        try:
            roll_result = int(random.randint(self.min_value, self.max_value))
            return roll_result
        except Exception:
            raise DiceException().rise_wrong_values_range_exception()

@dataclass
class SpecialityDice(Dice):

    values_range:list = field(default_factory=list)

    def roll(self):
        try:
            roll_result = random.choice(self.values_range)
        except Exception as e:
            print(f"Something gone wrong! Raise {e}")


class DiceType(Enum):
    D4 = "K4"
    D6 = "K6"
    D8 = "K8"
    D10 = "K10"
    D12 = "K12"
    D20 = "K20"
    D100 = "K100"
