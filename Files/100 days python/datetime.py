from datetime import datetime

from datetime import date

today = print(datetime.today())
todaydate = print(date.today())
christmas = date(2020, 12, 25)
fdate = christmas - date.today()
print(fdate)

if christmas is not todaydate:
    print(f"there are more {fdate}")
else:
    print("yay today is christmas")