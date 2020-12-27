#Shiv Subedi
#This code is developed to perform following tasks:
#1. find the number of days in a month
#2. to check whether a given date is a valid date
#3. find number of days between two dates
#4. find the age in days 

"""
Developing a code to find no of days in a given month
"""
import datetime

def days_in_month(year, month):
    """
	Inputs:
	  year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
			  representing the year
	  month - an integer between 1 and 12 representing the month

	Returns:
	  The number of days in the input month.
	"""
    date1 = datetime.date (year,month,1)
    if (month<12):
        date2= datetime.date (year, month+1,1)
    else:
        date2 = datetime.date (year+1,1,1)
    diff = date2-date1
	#print(diff.days)
    return diff.days

days_in_month(1,1)


#User provides a particular date and this function checks if the given date is a valid date or not
def is_valid_date(year, month, day):
    """
	Inputs:
	  year  - an integer representing the year
	  month - an integer representing the month
	  day   - an integer representing the day

	Returns:
	  True if year-month-day is a valid date and
	  False otherwise
	"""
    if ((year < datetime.MINYEAR) or (year > datetime.MAXYEAR)):
        return False
    elif ((month<1) or (month>12)):
        return False
    elif ((day < 1) or (day > days_in_month(year, month))):
        return False
    elif (((year % 400 != 0) or (year % 4 != 0)) and (month == 2 ) and (day == 29)):
        return False
    else:
        return True

is_valid_date(2000,1,1)


#The code fids the number of days between two  provided dates
def days_between(year1, month1, day1, year2, month2, day2):
    """
	Inputs:
	  year1  - an integer representing the year of the first date
	  month1 - an integer representing the month of the first date
	  day1   - an integer representing the day of the first date
	  year2  - an integer representing the year of the second date
	  month2 - an integer representing the month of the second date
	  day2   - an integer representing the day of the second date

	Returns:
	  The number of days from the first date to the second date.
	  Returns 0 if either date is invalid or the second date is
	  before the first date.
	"""
    if is_valid_date(year1, month1, day1) is False:
        return 0
    elif is_valid_date(year2, month2, day2) is False:
        return 0
    elif (datetime.date(year1,month1,day1) > datetime.date(year2,month2, day2)):
        return 0
    else:
        return (datetime.date(year2,month2, day2)-datetime.date(year1,month1,day1)).days

days_between(2000,1,1,2047,8,2)


#This code finds the age in days
def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid of if the input
      date is in the future.
    """



    if is_valid_date(year,month,day) is False:
        return 0
    elif (datetime.date(year, month,day) > datetime.date.today()):
        return 0
    else:
        return (datetime.date.today() - datetime.date(year, month,day)).days

age_in_days(2017,1,1)
