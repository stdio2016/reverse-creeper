import datetime

def cw1_year_to_days(year):
    return int(3652425 * year / 10000)

first_day = datetime.date(1, 1, 1)
for year in range(1900, 2100):
    realdate = datetime.date(year, 1, 1)
    real_days = (realdate - first_day).days + 366
    cw1_days = cw1_year_to_days(year)
    print('year', year, 'difference', real_days - cw1_days)
# bugs occur at December 31, 1999 and January 1, 2000
# go to a date that doesn't exist
# when click Next on December 31, 1999 -> get December 0, 2000
# when click Prev on January 1, 2000 -> get January 0, 2000

# bugs occur at December 31, 2000 and January 1, 2001
# skip some date
# when click Next on December 31, 1999 -> get January 2, 2001
# when click Prev on January 1, 2001 -> get December 30, 2000