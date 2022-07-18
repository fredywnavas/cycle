import constants

from game.casting.cast import Cast
from game.casting.score import Score
from game.casting.cycle import Cycle
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.point import Point

def main():

    # Creates two cycles, gets their position and color
    cycle_one = Cycle(Point(int(constants.MAX_X - 600), int(constants.MAX_Y / 2)))
    cycle_two = Cycle(Point(int(constants.MAX_X - 300), int(constants.MAX_Y / 2)))
    cycle_one.set_cycle_color(constants.GREEN)
    cycle_two.set_cycle_color(constants.RED)
    cycle_one_name = input("\nPlease enter player 1 name: \n")
    cycle_two_name = input("\nPlease enter player 2 name: \n")
    cycle_one.set_name(cycle_one_name)
    cycle_two.set_name(cycle_two_name)

    