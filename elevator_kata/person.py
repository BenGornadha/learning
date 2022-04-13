from __future__ import annotations

from elevator_kata.Elevator_exceptions import NoMovementDetectedException
from elevator_kata.direction import Direction


class LevelWrongTypeException(Exception):
    pass


class Person:

    def __init__(self, level: int, level_target: int) -> None:

        self._level: int = self._extract_level(level=level)
        self._level_target: int = self._extract_level(level=level_target)
        self._direction: str = self._extract_direction()

    def __str__(self):
        return f"Person(level={self._level},going={self._level_target})"

    def get_level(self) -> int:
        return self._level

    def get_level_target(self) -> int:
        return self._level_target

    def get_direction(self) -> str:
        return self._direction

    def _extract_level(self, level: int) -> int:
        if isinstance(level, int):
            return level
        raise LevelWrongTypeException

    def _extract_direction(self) -> str:
        self._require_movement()
        if self._level < self._level_target:
            return Direction.UP
        return Direction.DOWN

    def _require_movement(self) -> None:
        if self._level == self._level_target:
            raise NoMovementDetectedException
