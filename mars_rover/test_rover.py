from __future__ import annotations
import unittest
from enum import Enum, auto
from typing import Any


class Direction(Enum):
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()


class Command(Enum):
    FORWARD = auto()
    BACKWARD = auto()
    RIGHT = auto()
    LEFT = auto()


class Point:

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def translate(self, deltaX=0, deltaY=0) -> Point:
        return Point(self.x + deltaX, self.y + deltaY)

    def __eq__(self, other: Any):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    def __str__(self):
        return f"x={self.x},y={self.y}"

    def __repr__(self):
        return str(self)


class MarsRover:

    def __init__(self, starting_point: Point, direction: Direction) -> None:
        self.starting_point = starting_point
        self.direction = direction

    def get_current_position(self) -> Point:
        return self.starting_point

    def get_current_direction(self):
        return self.direction

    def __eq__(self, other):
        if isinstance(other, MarsRover):
            return self.get_current_position() == other.get_current_position() and self.get_current_direction() == other.get_current_direction()
        return False

    def __repr__(self):
        return f"starting_point={str(self.starting_point)} direction={self.direction}"


class Computer:

    def compute(self, a_command: Command, a_rover: MarsRover) -> MarsRover:
        position = a_rover.get_current_position()
        new_position = position
        new_direction = a_rover.get_current_direction()
        if a_command in [Command.RIGHT, Command.LEFT]:
            direction = a_rover.get_current_direction()
            if direction is Direction.NORTH:
                new_direction = Direction.EAST

        if a_rover.get_current_direction() is Direction.EAST and a_command is Command.BACKWARD:
            new_position = position.translate(deltaX=-1)
        if a_rover.get_current_direction() is Direction.EAST and a_command is Command.FORWARD:
            new_position = position.translate(deltaX=1)
        if a_rover.get_current_direction() is Direction.NORTH and a_command is Command.FORWARD:
            new_position = position.translate(deltaY=1)
        elif a_rover.get_current_direction() is Direction.NORTH and a_command is Command.BACKWARD:
            new_position = position.translate(deltaY=-1)

        elif a_rover.get_current_direction() is Direction.SOUTH and a_command is Command.FORWARD:
            new_position = position.translate(deltaY=-1)
        elif a_rover.get_current_direction() is Direction.SOUTH and a_command is Command.BACKWARD:
            new_position = position.translate(deltaY=1)

        return MarsRover(starting_point=new_position, direction=new_direction)


class TestComputer(unittest.TestCase):

    def test__move_forward_mars_rover_from_x_0_y_1_with_north(self):
        my_computer = Computer()
        new_rover = my_computer.compute(a_command=Command.FORWARD,
                                        a_rover=MarsRover(starting_point=Point(x=0, y=1), direction=Direction.NORTH))

        self.assertEqual(MarsRover(starting_point=Point(x=0, y=2), direction=Direction.NORTH), new_rover)

    def test__move_forward_mars_rover_from_x_0_y_2_with_north(self):
        my_computer = Computer()
        new_rover = my_computer.compute(a_command=Command.FORWARD,
                                        a_rover=MarsRover(starting_point=Point(x=0, y=2), direction=Direction.NORTH))

        self.assertEqual(MarsRover(starting_point=Point(x=0, y=3), direction=Direction.NORTH), new_rover)

    def test__move_forward_mars_rover_from_x_0_y_2_with_south(self):
        my_computer = Computer()
        new_rover = my_computer.compute(a_command=Command.FORWARD,
                                        a_rover=MarsRover(starting_point=Point(x=0, y=2), direction=Direction.SOUTH))

        self.assertEqual(MarsRover(starting_point=Point(x=0, y=1), direction=Direction.SOUTH), new_rover)

    def test__move_backward_mars_rover_from_x_0_y_2_with_north(self):
        my_computer = Computer()
        new_rover = my_computer.compute(a_command=Command.BACKWARD,
                                        a_rover=MarsRover(starting_point=Point(x=0, y=2), direction=Direction.NORTH))

        self.assertEqual(MarsRover(starting_point=Point(x=0, y=1), direction=Direction.NORTH), new_rover)

    def test__move_backward_mars_rover_from_x_0_y_2_with_south(self):
        my_computer = Computer()
        new_rover = my_computer.compute(a_command=Command.BACKWARD,
                                        a_rover=MarsRover(starting_point=Point(x=0, y=2), direction=Direction.SOUTH))

        self.assertEqual(MarsRover(starting_point=Point(x=0, y=3), direction=Direction.SOUTH), new_rover)

    def test__move_forward_mars_rover_from_x_0_y_2_with_east(self):
        my_computer = Computer()
        new_rover = my_computer.compute(a_command=Command.FORWARD,
                                        a_rover=MarsRover(starting_point=Point(x=0, y=2), direction=Direction.EAST))

        self.assertEqual(MarsRover(starting_point=Point(x=1, y=2), direction=Direction.EAST), new_rover)

    def test__move_backward_mars_rover_from_x_1_y_2_with_east(self):
        my_computer = Computer()
        new_rover = my_computer.compute(a_command=Command.BACKWARD,
                                        a_rover=MarsRover(starting_point=Point(x=1, y=2), direction=Direction.EAST))

        self.assertEqual(MarsRover(starting_point=Point(x=0, y=2), direction=Direction.EAST), new_rover)

    def test_x(self):
        my_computer = Computer()
        new_rover = my_computer.compute(a_command=Command.RIGHT,
                                        a_rover=MarsRover(starting_point=Point(x=1, y=2), direction=Direction.NORTH))

        self.assertEqual(MarsRover(starting_point=Point(x=1, y=2), direction=Direction.EAST), new_rover)


class TestRover(unittest.TestCase):

    def test__get_current_position_x_0_y_1_return_starting_Point_when_rover_didnt_receive_any_command(self):
        my_rover = MarsRover(starting_point=Point(x=0, y=1), direction=Direction.NORTH)

        self.assertEqual(Point(x=0, y=1), my_rover.get_current_position())

    def test__get_current_position_return_starting_Point_when_rover_didnt_receive_any_command(self):
        my_rover = MarsRover(starting_point=Point(x=0, y=2), direction=Direction.NORTH)

        self.assertEqual(Point(x=0, y=2), my_rover.get_current_position())

    def test__get_current_direction_return_initial_direction_when_rover_didnt_receive_any_command(self):
        my_rover = MarsRover(starting_point=Point(x=0, y=2), direction=Direction.NORTH)

        self.assertEqual(Direction.NORTH, my_rover.get_current_direction())

    def test__get_current_direction_return_initial_direction_east_when_rover_didnt_receive_any_command(self):
        my_rover = MarsRover(starting_point=Point(x=0, y=2), direction=Direction.EAST)

        self.assertEqual(Direction.EAST, my_rover.get_current_direction())

    def test_two_identicals_rovers_are_equals(self):
        r1 = MarsRover(Point(x=0, y=0), Direction.NORTH)
        r2 = MarsRover(Point(x=0, y=0), Direction.NORTH)
        self.assertEqual(r1, r2)


class TestPoint(unittest.TestCase):

    def test_two_points_with_same_x_and_y_are_equal(self):
        p1 = Point(x=0, y=1)
        p2 = Point(x=0, y=1)
        self.assertEqual(p1, p2)

    def test_comparing_a_Point_and_another_object_return_False(self):
        p1 = Point(x=0, y=0)
        self.assertFalse(p1 == "hello")

    def test__string_reprensentation_of_Point_display_x_and_y_value_separated_comma(self):
        p1 = Point(x=0, y=1)

        self.assertEqual("x=0,y=1", str(p1))
