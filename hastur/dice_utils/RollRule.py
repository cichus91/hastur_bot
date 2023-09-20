from abc import ABC, abstractmethod
from dataclasses import dataclass, field

from hastur.dice_utils.RollResult import RollResult

"""
Abstrakcyjna klasa umożliwiająca implementacje kolejnych zasad.
"""

@dataclass
class RollRule(ABC):

    roll_result:int
    field_value:int = field(default=0)
    bonus_value:int = field(default=0)

    @abstractmethod
    def check(self) -> RollResult:
        pass
