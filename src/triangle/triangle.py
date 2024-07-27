from collections.abc import Callable
from functools import wraps

CheckFunction = Callable[[list[float]], bool]


def is_valid(func: CheckFunction) -> CheckFunction:
    """Sides are not 0 and the longest one is less than the sum of others."""

    @wraps(func)
    def wrapper(triangle: list[float]) -> bool:
        valid = set(triangle) != {0} and sum(triangle) > max(triangle) * 2
        return valid and func(triangle)

    return wrapper


@is_valid
def equilateral(triangle: list[float]) -> bool:
    """All sides of an equal length."""
    return len(set(triangle)) == 1


@is_valid
def isosceles(triangle: list[float]) -> bool:
    """At least two sides of the equal length."""
    return len(set(triangle)) <= 2


@is_valid
def scalene(triangle: list[float]) -> bool:
    """All sides of a different length."""
    return len(set(triangle)) == 3


def degenerate(triangle: list[float]) -> bool:
    """Has zero area."""
    return sum(triangle) == 2 * max(triangle)
