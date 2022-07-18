import constants
from game.casting.actor import Actor

class GameOver(Actor):
    """
    Displays a Game Over Message.

    Attributes:
        _color (constant): The color value the game over message is displayed in.
    """
    def __init__(self):
        """
        Constructs a game over message.
        """
        super().__init__()
        self._color = constants.GREEN

    def get_color(self):
        """
        Gets the actor's color as a tuple of three ints (r, g, b).
        
        Returns:
            Color: The actor's text color.
        """
        return super().get_color()

    def set_color(self, color):
        """
        Updates the color to the given one.

        Args:
            color (Color): The given color.
        """
        return super().set_color(color)