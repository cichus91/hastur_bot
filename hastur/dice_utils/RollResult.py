import discord
from dataclasses import dataclass, field
from enum import Enum
from abc import ABC, abstractmethod

from hastur.dice_utils.Dice import StandardDice, Dice


class RollResult():
#todo rozwazyc usuniecie i przeniesienie enuma do RollRule
    class Result(Enum):
        SUCCESS = "Pełny sukces"
        WEAK_SUCCESS = "Sukces z konsekwencją"
        CRITICAL_SUCCESS = "Krytyczny sukces"
        FAILURE = "Porażka"
        CRITICAL_FAILURE = "KRYTYCZNA PORAŻKA!!!"
        STANDARD_ROLL = "Rzut kością"

    def __init__(self) -> None:
        self.result = None


class RollResultBuilder():
#todo rozwazyc usuniecie
    def __init__(self) -> None:
        self.roll_result = RollResult()
        self.roll_results_list = list[RollResult]
