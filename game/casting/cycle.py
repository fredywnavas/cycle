import constants
from game.casting.actor import Actor
from game.shared.point import Point
from game.shared.color import Color

class Cycle(Actor):
    """
    A fast motorcycle.
    
    The responsibiliy of Cycle is move itself.

    Attributes:
        _segments (list)        : A list of actors that make up each cycle.
        _color (tuple)          : A tuple containing the values that make up a color.
        _prepare_cycle (method) : A method that will create the cycle for each instance of Cycle.
        _name (str)             : An empty string that will hold each players name.
    """
    def __init__(self, position):
        """
        Constructs a new cycle.

        Args:
            position (Point): The position and direction that each cycle will travel in at game start.
        """
        super().__init__()
        self._segments = []
        self._color = Color(255, 255, 255)
        self._prepare_cycle(position)
        self._name = ""

    def get_segments(self):
        """
        Gets the segments for each cycle.

        Returns:
            List: The list of actors for each cycle.
        """
        return self._segments

    def get_name(self):
        """
        Gets the player name.
        
        Returns:
            string: The players name as text.
        """
        return self._name

    def move_next(self):
        """
        Moves the actor to its next position according to its velocity.
        Will move each actor in _segments beginning from the last segment and ending with the first segment
        and stepping by -1 to iterate through the last backwards.
        """

        #move all segnments
        for segment in self._segments:
            segment.move_next()
        
        #update velocities
        for i in range(len(self._segments) -1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_cycle(self):
        """
        Gets the first actor from _segments.

        Returns:
            Actor: The first actor from the list of actors in _segments.
        """
        return self._segments[0]

    def wall(self, game_over):
        """
        Builds the wall for each cycle.

        Args:
            Boolean: Sets the color for each cycle if game is not over.
            Changes each cycle to white if game is over.
        """
        wall = self._segments[-1]
        velocity = wall.get_velocity()
        offset = velocity.reverse()
        position = wall.get_position().add(offset)

        segment = Actor()
        segment.set_position(position)
        segment.set_velocity(velocity)
        segment.set_text("#")
        if not game_over:
            segment.set_color(self._color)
        else:
            segment.set_color(constants.WHITE)
        self._segments.append(segment)

    def turn_cycle(self, velocity):
        """
        Changes direction for a cycle by changing the velocity.
        
        Args:
            Point: A given velocity to change direction.
        """
        self._segments[0].set_velocity(velocity)

    def _prepare_cycle(self, position):
        """
        Constructs a new cycle.

        Args:
            Point: A position to set the cycle position and direction which it will travel in.
        """
        x = position.get_x()
        y = position.get_y()

        for i in range(constants.CYCLE_LENGTH):
            position = Point(x, y + i * constants.CELL_SIZE)
            velocity = Point(0, 1 * -constants.CELL_SIZE)
            text = "O" if i == 0 else "#"

            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(self._color)
            self._segments.append(segment)

    def set_cycle_color(self, color):
        """
        Sets the color for each segment of a cycle.
        
        Args:
            color (Color): The given color.
        """
        self._color = color

        for segment in self._segments:
            segment.set_color(self._color)

    def set_name(self, name):
        """
        Sets the name for each player.
        Args:
            String: The players given name as text.
        """
        self._name = name