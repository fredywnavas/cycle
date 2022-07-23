import constants
from game.scripting.action import Action
from game.shared.point import Point

class ControlActorsAction(Action):
    """
    An input action that controls the cycle.
    The responsibility of ControlActorsAction is to get a direction and turn
    a cycle to move in that direction depending on the key a player presses.

    Attributes:
        _keyboard_service (KeyboarService): An instance of KeyboardService.
        _cycle_one_direction (Point): The direction assigned to cycle_one.
        _cycle_two_direction (Point): The direction assigned to cycle_two.
    """
    def __init__(self, keyboard_service):
        """
        Constructs a new ControlActorsAction using the specified KeyboardService.

        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._cycle_one_direction = Point(0, -constants.CELL_SIZE)
        self._cycle_two_direction = Point(0, -constants.CELL_SIZE)

    def execute(self, cast, script):
        """
        Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """

        # Cycle one keyboard inputs

        # left
        if self._keyboard_service.is_key_down('a'):
            self._cycle_one_direction = Point(-constants.CELL_SIZE, 0)
        
        # right
        if self._keyboard_service.is_key_down('d'):
            self._cycle_one_direction = Point(constants.CELL_SIZE, 0)

        # up
        if self._keyboard_service.is_key_down('w'):
            self._cycle_one_direction = Point(0, -constants.CELL_SIZE)

        # down
        if self._keyboard_service.is_key_down('s'):
            self._cycle_one_direction = Point(0, constants.CELL_SIZE)

        cycle_one = cast.get_first_actor("cycle_one")
        cycle_one.turn_cycle(self._cycle_one_direction)

        # Cycle two keyboard inputs

        # left
        if self._keyboard_service.is_key_down('j'):
            self._cycle_two_direction = Point(-constants.CELL_SIZE, 0)

        # right
        if self._keyboard_service.is_key_down('l'):
            self._cycle_two_direction = Point(constants.CELL_SIZE, 0)

        # up
        if self._keyboard_service.is_key_down('i'):
            self._cycle_two_direction = Point(0, -constants.CELL_SIZE)
        
        # down
        if self._keyboard_service.is_key_down('k'):
            self._cycle_two_direction = Point(0, constants.CELL_SIZE)

        cycle_two = cast.get_first_actor("cycle_two")
        cycle_two.turn_cycle(self._cycle_two_direction)