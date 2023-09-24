from hastur.dice_utils.roll_strategies.RollStrategy import RollStrategy
from hastur.dice_utils.roll_strategies.TrophyDarkStrategy import TrophyDarkStrategy
from hastur.dice_utils.roll_strategies.StandardRollStrategy import StandardRollStrategy

# Map game cmd name -> strategy class (for roll context)
STRATEGIES_CLS_BY_CMD_NAME: dict[str, type] = {
    strategy_cls.CMD_NAME: strategy_cls
    for strategy_cls in (StandardRollStrategy, TrophyDarkStrategy)
}
