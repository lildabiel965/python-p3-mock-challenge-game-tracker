class Game:
    def __init__(self, title):
        if not isinstance(title, str) or len(title) == 0:
            raise ValueError("Title must be a non-empty string.")
        self._title = title

    @property
    def title(self):
        return self._title

    def results(self):
        return [result for result in Result.instances if result.game == self]

    def players(self):
        return list(set(result.player for result in Result.instances if result.game == self))

    def average_score(self, player):
        player_results = [result.score for result in Result.instances if result.game == self and result.player == player]
        if not player_results:
            return 0
        return sum(player_results) / len(player_results)

class Player:
    def __init__(self, username):
        if not isinstance(username, str) or not (2 <= len(username) <= 16):
            raise ValueError("Username must be a string between 2 and 16 characters.")
        self._username = username

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError("Username must be a string between 2 and 16 characters.")
        self._username = value

    def results(self):
        return [result for result in Result.instances if result.player == self]

    def games_played(self):
        return list(set(result.game for result in Result.instances if result.player == self))

    def played_game(self, game):
        return any(result.game == game for result in Result.instances if result.player == self)

    def num_times_played(self, game):
        return sum(1 for result in Result.instances if result.player == self and result.game == game)

class Result:
    instances = []  # Class variable to keep track of all instances
    all = []  # Class variable to keep track of all results

    def __init__(self, player, game, score):
        if not isinstance(score, int) or not (1 <= score <= 5000):
            raise ValueError("Score must be an integer between 1 and 5000.")
        self._player = player
        self._game = game
        self._score = score
        Result.instances.append(self)  # Add the instance to the class variable
        Result.all.append(self)  # Add the instance to the all variable

    @property
    def player(self):
        return self._player

    @property
    def game(self):
        return self._game

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int) or not (1 <= value <= 5000):
            raise ValueError("Score must be an integer between 1 and 5000.")
        self._score = value
