import pyray
import constants

class VideoService:
    """
    Outputs the game state. The responsibility of the class of objects is to draw the game state on the screen.
    """

    def __init__(self, debug = False):
        """
        Constructs a new VideoService using the specified debug mode.

        Args:
            debug (bool): whether or noto to draw in debug mode.
        """
        self._debug = debug