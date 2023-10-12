class NoDataForYearError(Exception):

    def __init__(self, year):
        self.year = year
        self.message = f'No data found for holidays in year {self.year}' 
        super().__init__(self.message)

