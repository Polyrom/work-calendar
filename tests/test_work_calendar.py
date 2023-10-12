from datetime import date
import unittest

from work_calendar import WorkCalendar, exceptions


class TestWorkCalendar(unittest.TestCase):

    def test_is_day_off(self):
        actual_holiday = date(day=8, month=3, year=2024)
        workday = date(day=13, month=6, year=2018)
        invalid_date = date(day=1, month=1, year=2003)
        result_holiday = WorkCalendar.is_day_off(actual_holiday)
        result_workday = WorkCalendar.is_day_off(workday)

        self.assertTrue(result_holiday)
        self.assertFalse(result_workday)

        with self.assertRaises(exceptions.NoDataForYearError):
            WorkCalendar.is_day_off(invalid_date)
        
