

class DiceException(BaseException):

    WRONG_VALUES_RANGE_GIVEN = "Wrong range values was given!"

    def rise_wrong_values_range_exception(self):
        return DiceException(self.WRONG_VALUES_RANGE_GIVEN)
