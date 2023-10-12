import os
import json
import datetime
from work_calendar import exceptions


class WorkCalendar:

    data_path = os.path.join(os.getcwd(), 'data', 'total.json')

    @classmethod
    def is_day_off(cls, date_to_check: datetime.date) -> bool:
        return cls._is_in_days_off(date_to_check)

    @classmethod
    def _is_in_days_off(cls, day: datetime.date) -> bool:
        data = cls._load_data(cls.data_path)
        year = datetime.date.strftime(day, '%Y')
        date_ = datetime.date.strftime(day, '%Y-%m-%d')
        for stored_year, days_off in data.items():
            if stored_year == year:
                return date_ in days_off
        raise exceptions.NoDataForYearError(year)

    @classmethod
    def _load_data(cls, path_to_data: str) -> dict[str, str]:
        with open(path_to_data, 'r') as f:
            data = json.loads(f.read())
            return data

