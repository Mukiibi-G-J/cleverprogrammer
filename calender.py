import calendar
import daytime
import time
print(calendar.weekheader(3))
#givea the index of the first day of the week
print(calendar.firstweekday())
 
#u can also use the month (2021)for year and 4 for the month 
print(calendar.month(2021,4))

#give you the calender in an array 
print(calendar.monthcalendar(2019,3))

#gives you the whole year
print(calendar.calendar(2021))

day_of_the_week=calendar.weekday(2021,5,1)
print(day_of_the_week)

#use to find out if a year is a  leap year
Is_leap=calendar.isleap(2020)
print(Is_leap) 

how_many_leap_days= calendar.leapdays(2000,2005)
print(how_many_leap_days)


# Data Type
    # intergers
    # floats
    # boolens
    # strings
# Casting
    # float(1)