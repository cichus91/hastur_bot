from enum import Enum

from hastur.dice_utils.roll_strategies.RollStrategy import RollStrategy
from hastur.dice_utils.roll_strategies.TrophyDarkStrategy import TrophyDarkStrategy
from hastur.dice_utils.roll_strategies.StandardRollStrategy import StandardRollStrategy

"""Klasa zarządzająca kontekstem roll. Umożliwia wybranie odpowiedniego trybu, zgodnie z wyborem gry
z dużą dozą prawdopodobieństa do zamiany/rozbudowy w zależności od wyglądu innych serwisów"""


class RollContext:

    def match_roll_strategy(self, game) -> RollStrategy:
        match game:
            case GamesEnum.TROPHY_DARK.value:
                return TrophyDarkStrategy()
            case GamesEnum.STANDARD.value:
                return StandardRollStrategy()
            case _:
                return StandardRollStrategy()

class GamesEnum(Enum):
    TROPHY_DARK = "Trophy Dark"
    BLADES_IN_THE_DARK = "Blades in the Dark"
    BRINDLEWOOD_BAY = "Brindlewood Bay"
    STANDARD = "Standard"
