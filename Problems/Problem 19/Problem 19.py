# Problem 19: determine the number of Saturdays between 1 Jan 1901 and 31 Dec 2000
import datetime as dt
from dateutil.relativedelta import relativedelta

def problem19(start_date, end_date):
	result = 0

	delta_month = relativedelta(months=1)

	while start_date <= end_date:
		
		if start_date.weekday() == 6:
			result += 1

		start_date += delta_month

	return result

if __name__ == '__main__': 
    print(problem19(dt.datetime(year=1901, month=1, day=1), dt.datetime(year=2000, month=12, day=31)))