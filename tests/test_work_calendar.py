import unittest
from datetime import date

import pytest

from work_calendar import WorkCalendar, exceptions


class TestWorkCalendar(unittest.TestCase):
    def test_is_workday(self):
        actual_holiday = date(day=8, month=3, year=2024)
        workday = date(day=13, month=6, year=2018)
        invalid_date = date(day=1, month=1, year=2003)
        result_holiday = WorkCalendar.is_workday(actual_holiday)
        result_workday = WorkCalendar.is_workday(workday)

        assert result_holiday is False
        assert result_workday is True

        with pytest.raises(exceptions.NoDataForYearError):
            WorkCalendar.is_workday(invalid_date)

        with pytest.raises(TypeError):
            WorkCalendar.is_workday("2010-01-01")  # type: ignore
