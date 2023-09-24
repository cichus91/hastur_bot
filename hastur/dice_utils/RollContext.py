from collections import defaultdict
from typing import Optional, Union

from discord import Guild, Member, User

from hastur.dice_utils.roll_strategies import STRATEGIES_CLS_BY_CMD_NAME
from hastur.dice_utils.roll_strategies.RollStrategy import RollStrategy
from hastur.dice_utils.roll_strategies.StandardRollStrategy import StandardRollStrategy

"""Klasa zarządzająca kontekstem roll. Umożliwia wybranie odpowiedniego trybu, zgodnie z wyborem gry
z dużą dozą prawdopodobieństa do zamiany/rozbudowy w zależności od wyglądu innych serwisów"""


class RollContext(object):

    GAME_NAMES_BY_CMD = {cmd_name: strategy_cls.NAME for cmd_name, strategy_cls in STRATEGIES_CLS_BY_CMD_NAME.items()}

    def __init__(self) -> None:
        self._game_by_user = defaultdict(lambda: STRATEGIES_CLS_BY_CMD_NAME[StandardRollStrategy.CMD_NAME]())

    def get_strategy(self, user: Union[Member, User], guild: Optional[Guild]) -> RollStrategy:
        # defaultdict will set standard roll by default if no game set
        return self._game_by_user[self._game_key_from_msg(user, guild)]

    def set_strategy(self, user: Union[Member, User], guild: Optional[Guild], game: str) -> (bool, RollStrategy):
        if game not in STRATEGIES_CLS_BY_CMD_NAME:
            return False, self._game_by_user[self._game_key_from_msg(user, guild)]
        strategy = STRATEGIES_CLS_BY_CMD_NAME[game]()
        self._game_by_user[self._game_key_from_msg(user, guild)] = strategy
        return True, strategy

    @staticmethod
    def _game_key_from_msg(user: Union[Member, User], guild: Optional[Guild]) -> (int, int):
        guild_id = None
        if guild is not None:
            guild_id = guild.id
        return (guild_id, user.id)
