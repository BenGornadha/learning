from __future__ import annotations


class IncorrectLevelException(Exception):
    pass


class IncorrectDirectionException(Exception):
    pass

class CannotGoUpper(Exception):
    pass

class CannotGoDowner(Exception):
    pass


class NoMovementDetectedException(Exception):
    pass