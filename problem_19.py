THIRTY_DAYS_MONTHS = 4
THIRTY_ONE_DAYS_MONTHS = 7
DAY_INDEX = 1
START_YEAR = 1901
END_YEAR = 2000
EXAMPLE_YEAR = 1900
WEEK = 7
MONTHS = 12


def is_leap_year(year: int) -> bool:
    return year % 4 == 0 and (not year % 100 == 0 or year % 400 == 0)


def days_between_years(start: int, end: int) -> int:
    total_days = 0
    for year in range(start, end):
        total_days += (30 * THIRTY_DAYS_MONTHS) + (31 * THIRTY_ONE_DAYS_MONTHS)
        if is_leap_year(year):
            total_days += 29
            continue
        total_days += 28
    return total_days


def total_month_day(month: int, year: int) -> int:
    if month in (4, 6, 9, 11):
        return 30
    if month == 2:
        if is_leap_year(year):
            return 29
        return 28
    return 31


day = DAY_INDEX + (days_between_years(EXAMPLE_YEAR, START_YEAR) % 7) % 7
total_sundays = 0
for year in range(START_YEAR, END_YEAR + 1):
    if day == 0:
        total_sundays += 1
    for month in range(1, MONTHS):
        month_days = total_month_day(month, year)
        day = (day + (month_days % 7)) % 7
        if day == 0:
            total_sundays += 1
    month_days = total_month_day(MONTHS, year)
    day = (day + (month_days % 7)) % 7

print(total_sundays)
