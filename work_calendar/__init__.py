import datetime
from pathlib import Path

from work_calendar import exceptions
from work_calendar.data_loader import load_data


class WorkCalendar:
    __data_path = Path.cwd() / "data" / "total.json"
    __workday_data = load_data(__data_path)

    @classmethod
    def is_day_off(cls, date_to_check: datetime.date) -> bool:
        """Determine if a given date is a day off.

        Args:
            date_to_check: The date to check.

        Returns:
            True if the given date is a day off, False otherwise.

        """
        return cls.__is_in_days_off(date_to_check)

    @classmethod
    def __is_in_days_off(cls, day: datetime.date) -> bool:
        date_ = datetime.date.strftime(day, "%Y-%m-%d")
        year_str = str(day.year)
        if year_str not in cls.__workday_data:
            raise exceptions.NoDataForYearError(day.year)
        return date_ in cls.__workday_data[year_str]
