from datetime import date, timedelta
x = date.today() - timedelta(5)
print(date.today(), "now")
print(x, "five days ago")