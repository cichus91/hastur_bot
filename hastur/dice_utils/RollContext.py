from hastur.dice_utils.roll_strategies.RollStrategy import RollStrategy
from hastur.dice_utils.roll_strategies.TrophyDarkStrategy import TrophyDarkStrategy
from hastur.dice_utils.GameEnum import GamesEnum
from hastur.dice_utils.roll_strategies.StandardRollStrategy import StandardRollStrategy

"""Klasa zarządzająca kontekstem roll. Umożliwia wybranie odpowiedniego trybu, zgodnie z wyborem gry"""


class RollContext:

    def match_roll_strategy(self, game) -> RollStrategy:
        match game:
            case GamesEnum.TROPHY_DARK.value:
                return TrophyDarkStrategy()
            case GamesEnum.STANDARD.value:
                return StandardRollStrategy()
