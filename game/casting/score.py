import constants

from game.casting.actor import Actor
from game.shared.point import Point

class Score(Actor):
    """
    A record of points made or lost.
    The responsibility of Score is to keep track of the points the player has earned.
    It contains methods for adding and getting points.
    Client should use get_text() to get string representation of the points earned.

    Attributes:
        _points (int)           : The points earned in the game.
        position (Point)        : A point value to place each players score on the screen. 
        _player_name (string)   : A string that will hold each players name.
        set_position (method)   : A method that sets the scores position on the screen.
        set_text (method)       : A method that displays each players name.
    """
    def __init__(self):
        """
        Sets starting points and position of points display
        """
        super().__init__()
        self._points = 0
        position = Point(0, 0)
        self._player_name = ""
        self.set_text(f"{self._player_name}: {self._points}")
        self.set_position(position)

    def add_points(self, points):
        """
        Adds the given points to the running total and updates the next.

        Args:
            self(Score)     : An instance of Score.
            points (integer): The points to add.
        """
        self._points += points
        self.set_text(f"{self._player_name}: {self._points}")

    def get_position(self):
        """
        
        """