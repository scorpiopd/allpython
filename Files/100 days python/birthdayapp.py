from datetime import datetime
from datetime import date


u=input("Enter your name ")
u=u.upper()


def print_header():
    print("-----------------------")
    print("BIRTHDAY APP")
    print("-----------------------")


def get_birthday_date():
    print("Tell us you were born ")
    year = int(input("YEAR[YYYY]"))
    month = int(input("MONTH[MM]"))
    day = int(input("DAY[DD]"))
    bday = date(year, month, day)

    return bday


def compute_days_between_days(bday, now):
    date1 = now
    date2 = date(now.year, bday.month, bday.day)

    dt = date1 - date2
    days = int(dt.total_seconds() / 60 / 60 / 24)
    return days


def print_birthday_info(days,u):
    if days < 0:
        print(f" {u}  birthday is in {days} days means {days / 30} months   ")
    elif days > 0:
        print(f" {u}  already celebrated your birthday")
    else:
        print(f"  HAPPY BIRTHDAY {u} WOHOOO")


def main():
    print_header()
    bday = get_birthday_date()

    now = date.today()

    no_of_days = compute_days_between_days(bday, now)

    print(print_birthday_info(no_of_days,u))


main()
