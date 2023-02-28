import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(now)
print(year)
print(month)
print(day_of_week)

date_of_birth = dt.datetime(year=1986, month=11, day=1, hour=16)
print(date_of_birth)
