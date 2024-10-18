from datetime import date

import pytest

from work_calendar import NoDataForYearError, is_workday


def test_is_workday_holiday():
    """Check that a known holiday is recognized as a day off.

    We take 8th of March, 2024 as a known holiday.
    """
    holiday = date(day=8, month=3, year=2024)
    assert is_workday(holiday) is False


def test_is_workday_day_off():
    """Test that a non-holiday, which is a weekend, is recognized as a day off.

    The 7th of September, 2024 is assumed to be a Saturday.
    """
    day_off = date(day=7, month=9, year=2024)
    assert is_workday(day_off) is False


def test_is_workday_workday():
    """Test that a known workday is recognized as such.

    The 13th of June, 2018 is assumed to be a workday.
    """
    workday = date(day=13, month=6, year=2018)
    assert is_workday(workday) is True


def test_is_workday_out_of_bounds():
    """Test that the function raises NoDataForYearError when given a date that is out of bounds.

    This test uses a date in 2003, which is before the start of the range of available
    data. The function should raise NoDataForYearError in this case.
    """
    date_out_of_bounds = date(day=1, month=1, year=2003)
    with pytest.raises(NoDataForYearError):
        is_workday(date_out_of_bounds)


def test_is_workday_invalid_type():
    """Test that is_workday raises a TypeError when given an invalid type.

    This test uses a string, which is not a datetime.date object, as an argument to
    is_workday. The function should raise a TypeError in this case.
    """
    with pytest.raises(TypeError):
        is_workday("2010-01-01")  # type: ignore
