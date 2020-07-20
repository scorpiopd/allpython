# program will calculate the total number of days in between date
from datetime import datetime
from datetime import date

yr=int(input("enter year "))
mn=int(input("enter month "))
day=int(input("enter day "))

pastdate=date(year=yr,month=mn,day=day)
print(pastdate)




todaydate=date.today()
print(todaydate)

fdate=pastdate-todaydate
print(fdate)