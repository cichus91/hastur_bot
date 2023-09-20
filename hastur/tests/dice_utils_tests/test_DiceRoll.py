import random
import pytest

from hastur.dice_utils.Dice import StandardDice
from hastur.dice_utils.DiceException import DiceException
"""
Standard Dice tests
"""
def test_max_value_setter_value_random_int():
    random_max_value = int(random.random()*10)
    dice = StandardDice(1, random_max_value)

    assert dice.roll() in range(dice.min_value, dice.max_value+1)


def test_min_value_setter_value_random_int():
    random_min_value = int(random.random() * 10)
    dice = StandardDice(random_min_value, 10)

    assert dice.min_value == random_min_value or dice.min_value > 0


def test_min_value_setter_negative_or_zero_value():
    dice_negative = StandardDice(-1, 10)
    dice_zero = StandardDice(0, 10)

    assert dice_negative.min_value == 1 and dice_zero.min_value == 1

def test_max_value_setter_negative_or_zero_value():
    dice_negative = StandardDice(1, -10)
    dice_zero = StandardDice(1, 0)

    assert dice_negative.min_value == 1 and dice_zero.min_value == 1


def test_standard_dice_roll_with_proper_values():
    dice = StandardDice(1, 10)

    assert dice.roll() in range(1, 11)

def test_standard_roll_rise_wrong_value_exception():

    with pytest.raises(DiceException, match = "Wrong range values was given!"):
        dice = StandardDice(4, 2)
"""
Special Dice tests
"""


