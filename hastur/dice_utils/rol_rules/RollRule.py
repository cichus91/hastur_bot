from abc import ABC, abstractmethod
from dataclasses import dataclass, field

from hastur.dice_utils.model.RollResult import RollResult

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

class RiskRoll(RollRule):

    #todo wydzielic do osobnego pliku
    def check(self) -> RollResult.Result:
        if self.roll_result == 6:
            return RollResult.Result.SUCCESS.value
        elif self.roll_result in (4, 5):
            return RollResult.Result.WEAK_SUCCESS.value
        else:
            return RollResult.Result.FAILURE.value
