import pytest
from datetime import date, time
from class_shift import Shift


"""смены, которые нужно проверить на факт пересечения по времени"""

tests_true = [
    (
        dict(
            time_from=time(22, 00, 00),
            time_to=time(10, 00, 00),
            date_from=date(2020, 9, 1),
            date_to=date(2020, 9, 30),
            week_days=[2, 4],
        ),
        dict(
            time_from=time(8, 00, 00),
            time_to=time(17, 00, 00),
            date_from=date(2020, 9, 1),
            date_to=date(2020, 9, 30),
            week_days=[1, 3],
        ),
    ),
    (
        dict(
            time_from=time(8, 00, 00),
            time_to=time(5, 00, 00),
            date_from=date(2020, 1, 1),
            date_to=date(2020, 1, 10),
            week_days=[1, 2, 3],
        ),
        dict(
            time_from=time(10, 00, 00),
            time_to=time(13, 00, 00),
            date_from=date(2020, 1, 1),
            date_to=date(2020, 1, 10),
            week_days=[1, 2, 3],
        ),
    ),
    (
        dict(
            time_from=time(8, 00, 00),
            time_to=time(15, 00, 00),
            date_from=date(2020, 1, 1),
            date_to=date(2020, 1, 10),
            week_days=[1, 2, 3],
        ),
        dict(
            time_from=time(8, 00, 00),
            time_to=time(15, 00, 00),
            date_from=date(2020, 1, 1),
            date_to=date(2020, 1, 10),
            week_days=[1, 2, 3],
        ),
    ),
    (
        dict(
            time_from=time(8, 00, 00),
            time_to=time(17, 00, 00),
            date_from=date(2020, 1, 1),
            date_to=date(2020, 1, 10),
            week_days=[1, 2, 3],
        ),
        dict(
            time_from=time(10, 00, 00),
            time_to=time(13, 00, 00),
            date_from=date(2020, 1, 1),
            date_to=date(2020, 1, 10),
            week_days=[1, 2, 3],
        ),
    ),
    (
        dict(
            time_from=time(8, 00, 00),
            time_to=time(17, 00, 00),
            date_from=date(2020, 1, 1),
            date_to=date(2020, 1, 10),
            week_days=[1, 2, 3],
        ),
        dict(
            time_from=time(10, 00, 00),
            time_to=time(20, 00, 00),
            date_from=date(2020, 1, 1),
            date_to=date(2020, 1, 10),
            week_days=[1, 2, 3],
        ),
    ),
    (
        dict(
            time_from=time(22, 00, 00),
            time_to=time(11, 00, 00),
            date_from=date(2020, 1, 1),
            date_to=date(2020, 1, 10),
            week_days=[3, 4, 5],
        ),
        dict(
            time_from=time(10, 00, 00),
            time_to=time(20, 00, 00),
            date_from=date(2020, 1, 11),
            date_to=date(2020, 1, 20),
            week_days=[6, 7, 1],
        ),
    ),
]

"""смены которые нужно проверить на факт НЕпересечения по времени"""

tests_false = [
        (
            dict(
                time_from=time(8, 00, 00),
                time_to=time(17, 00, 00),
                date_from=date(2020, 1, 1),
                date_to=date(2020, 1, 10),
                week_days=[1, 2, 3],
            ),
            dict(
                time_from=time(17, 00, 00),
                time_to=time(4, 00, 00),
                date_from=date(2020, 1, 1),
                date_to=date(2020, 1, 10),
                week_days=[1, 2, 3],
            ),
        ),
        (
            dict(
                time_from=time(22, 00, 00),
                time_to=time(5, 00, 00),
                date_from=date(2020, 9, 1),
                date_to=date(2020, 9, 30),
                week_days=[2, 4],
            ),
            dict(
                time_from=time(8, 00, 00),
                time_to=time(17, 00, 00),
                date_from=date(2020, 9, 1),
                date_to=date(2020, 9, 30),
                week_days=[1, 3],
            ),
        ),
    ]


@pytest.mark.parametrize(
    'first_value, second_value, result',
    [
        (Shift(**tests_true[0][0]), Shift(**tests_true[0][1]), True),
        (Shift(**tests_true[1][0]), Shift(**tests_true[1][1]), True),
        (Shift(**tests_true[2][0]), Shift(**tests_true[2][1]), True),
        (Shift(**tests_true[3][0]), Shift(**tests_true[3][1]), True),
        (Shift(**tests_true[4][0]), Shift(**tests_true[4][1]), True),
        (Shift(**tests_true[5][0]), Shift(**tests_true[5][1]), True),
        (Shift(**tests_false[0][0]), Shift(**tests_false[0][1]), False),
        (Shift(**tests_false[1][0]), Shift(**tests_false[1][1]), False)
    ],
)
def test_shift(first_value, second_value, result):
    assert Shift.__cmp__(first_value, second_value) == result


# ~/pytest start_pytest.py
