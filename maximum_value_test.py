import pytest

from maximum_value import maximum_value


@pytest.mark.parametrize(
    "orders,maximum_weight,value",
    [
        ([], 100, 0),
        ([{"weight": 100, "value": 1}], 10, 0),
        (
            [
                {"weight": 2, "value": 5},
                {"weight": 2, "value": 5},
                {"weight": 2, "value": 5},
                {"weight": 2, "value": 5},
                {"weight": 10, "value": 21},
            ],
            10,
            21,
        ),
        (
            [
                {"weight": 2, "value": 20},
                {"weight": 2, "value": 20},
                {"weight": 2, "value": 20},
                {"weight": 2, "value": 20},
                {"weight": 10, "value": 50},
            ],
            10,
            80,
        ),
        (
            [
                {"weight": 5, "value": 10},
                {"weight": 4, "value": 40},
                {"weight": 6, "value": 30},
                {"weight": 4, "value": 50},
            ],
            10,
            90,
        ),
        (
            [
                {"weight": 25, "value": 350},
                {"weight": 35, "value": 400},
                {"weight": 45, "value": 450},
                {"weight": 5, "value": 20},
                {"weight": 25, "value": 70},
                {"weight": 3, "value": 8},
                {"weight": 2, "value": 5},
                {"weight": 2, "value": 5},
            ],
            104,
            900,
        ),
        (
            [
                {"weight": 70, "value": 135},
                {"weight": 73, "value": 139},
                {"weight": 77, "value": 149},
                {"weight": 80, "value": 150},
                {"weight": 82, "value": 156},
                {"weight": 87, "value": 163},
                {"weight": 90, "value": 173},
                {"weight": 94, "value": 184},
                {"weight": 98, "value": 192},
                {"weight": 106, "value": 201},
                {"weight": 110, "value": 210},
                {"weight": 113, "value": 214},
                {"weight": 115, "value": 221},
                {"weight": 118, "value": 229},
                {"weight": 120, "value": 240},
            ],
            750,
            1458,
        ),
    ],
)
def test_maximum_value(orders, maximum_weight, value):
    assert maximum_value(orders, maximum_weight) == value
