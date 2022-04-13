from enum import Enum


class Direction(str, Enum):
    UP: str = "up"
    DOWN: str = "down"
    STAY: str = "stay"


