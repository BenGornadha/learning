from __future__ import annotations


class Elevator:

    def __init__(self, current_level: int, target_level : int):
        self.current_level = current_level
        self.target_level = target_level
        self.next_target_level = 0

    def call(self, a_button: Button) -> bool:
        if self.current_level == a_button.level:
            return True
        if self.has_to_go_up():
            self.next_target_level = a_button.level
            return False

    def has_to_go_up(self):
        return self.current_level < self.target_level

    def move(self):
        if self.current_level > self.target_level:
            self.current_level = self.current_level - 1

        if self.has_to_go_up():
            self.current_level = self.current_level + 1

    def has_arrived(self):
        if self.current_level == self.target_level:
            self.target_level = self.next_target_level

class IncorrectLevelException(Exception):
    pass


class IncorrectDirectionException(Exception):
    pass


class Button:

    def __init__(self, level: int, direction: str):

        self.level = self._extract_level(level)

        self.direction = self._extract_direction(direction=direction)

    def _extract_level(self, level):
        if level > 5 or level < 0:
            raise IncorrectLevelException
        return level

    def _extract_direction(self, direction):
        if direction not in ["up", "down"]:
            raise IncorrectDirectionException
        return direction
