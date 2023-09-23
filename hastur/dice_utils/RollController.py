from hastur.dice_utils.RollEndpoint import RollEndpoint
from hastur.dice_utils.RollManager import RollManager
from hastur.dice_utils.RollContext import RollContext

class RollController:

    #todo dodac obsluge jsona, zeby mozna było otrzymywac zapytania z innych serwisow
    def __init__(self):
        self.roll_context = RollContext()

    def get_roll_message(self, dice_amount: int, dice_type: int, game: str, author: str):
        #todo zmienić metodę przypisywania parametrów, w zależności od gry, w tym momencie jest to nieczytelne
        roll_parameters = (dice_amount, dice_type)
        #todo zmienic na wstrzykiwanie managera
        roll_manager = RollManager(roll_strategy=self.roll_context.match_roll_strategy(game))
        roll_endpoint = RollEndpoint(roll_manager=roll_manager)
        return roll_endpoint.get_roll_message(roll_parameters=roll_parameters, author=author)