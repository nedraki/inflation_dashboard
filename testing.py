import datetime as dt
from datetime import datetime, date

day_zero = dt.date(2021, 10, 3)
today = dt.date.today()

print(day_zero)
print(today)
delta = today - day_zero

print(delta)