import pytest

from src.lasangna.lasagna import bake_time_remaining
from src.lasangna.lasagna import elapsed_time_in_minutes
from src.lasangna.lasagna import EXPECTED_BAKE_TIME
from src.lasangna.lasagna import preparation_time_in_minutes


def test_expected_bake_time():
    assert EXPECTED_BAKE_TIME == 40


@pytest.mark.parametrize(
    "time,expected",
    (
        (1, 39),
        (2, 38),
        (5, 35),
        (10, 30),
        (15, 25),
        (23, 17),
        (33, 7),
        (39, 1),
    ),
)
def test_bake_time_remaining(time, expected):
    assert bake_time_remaining(time) == expected


@pytest.mark.parametrize(
    "layers,expected",
    (
        (1, 2),
        (2, 4),
        (5, 10),
        (8, 16),
        (11, 22),
        (15, 30),
    ),
)
def test_preparation_time_in_minutes(layers, expected):
    assert preparation_time_in_minutes(layers) == expected


@pytest.mark.parametrize(
    "layers,time,expected",
    (
        (1, 3, 5),
        (2, 7, 11),
        (5, 8, 18),
        (8, 4, 20),
        (11, 15, 37),
        (15, 20, 50),
    ),
)
def test_elapsed_time_in_minutes(layers, time, expected):
    assert elapsed_time_in_minutes(layers, time) == expected
