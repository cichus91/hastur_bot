from hastur.dice_utils.RollManager import RollManager
from hastur.dice_utils.RollContext import RollContext, GamesEnum
from hastur.dice_utils.model.RollResultMessage import RollResultMessage


class RollController:

    #todo dodac obsluge jsona, zeby mozna było otrzymywac zapytania z innych serwisow
    def __init__(self):
        self.roll_context = RollContext()

    def get_roll_message(self, dice_amount: int, dice_type: int, game: str, author: str) -> RollResultMessage:
        #todo zmienić metodę przypisywania parametrów, w zależności od gry, w tym momencie jest to nieczytelne
        roll_parameters = (dice_amount, dice_type)
        roll_manager = RollManager(roll_strategy=self.roll_context.match_roll_strategy(game))
        return roll_manager.get_roll_message(author=author, roll_parameters=roll_parameters)


    def set_game(self, game: str):
        response = {"game": GamesEnum.STANDARD.value, "message": f"Nie znaleziono gry!!! Gra zmienona na {GamesEnum.STANDARD.value}"}
        if game in self.avaliabe_games():
            response["game"] = game
            response["message"] = f"Gra zmieniona na {game}"
        return response

    @staticmethod
    def avaliabe_games():
        avaliable_games = list()
        for game in list(GamesEnum):
            avaliable_games.append(game.value)
        return avaliable_games
