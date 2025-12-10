import pytest

from main import calculate_fare
from historical import num_lin_file
from prices import get_price, read_prices

# Tests para funciones del fichero main
@pytest.mark.parametrize(
    "seconds_stopped, seconds_moving, expected",
    [
        (2, 10, 0.54),
        (1, 25, 1.27),
        (10, 112, 5.800000000000001)
    ]
)
def test_calculate_fare_operation(seconds_stopped, seconds_moving, expected):
    assert calculate_fare(seconds_stopped, seconds_moving) == expected


# Tests para funciones del fichero historical
def test_file_count_lins():
    assert num_lin_file("./historical/historical.txt") == 2

def test_file_empty_count_lins():
    assert num_lin_file("./historical/historical_vacio.txt") == 0


# Tests para funciones del fichero prices
def test_get_price():
    assert get_price("price_moving = 0.05") == ("price_moving", 0.05)

def test_get_price_not_spaces():
    assert get_price("price_moving=0.05") == ("price_moving", 0.05)

def test_get_price_not_none():
    assert get_price("price_moving=0.05") != None

def test_get_price_has_two_elements():
    price_tuple = get_price("price_moving=0.05")
    assert len(price_tuple) == 2


@pytest.mark.parametrize(
    "input_lin, expected",
    [
        ("price_moving = 0.05", ("price_moving", 0.05)),
        ("price_stopped = 0.02", ("price_stopped", 0.02))
    ]
)
def test_get_price_param(input_lin, expected):
    assert get_price(input_lin) == expected


def test_read_prices_is_a_tuple():
    assert read_prices() == (0.05, 0.02)