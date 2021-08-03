import datetime

today = datetime.date.today()
print(today.month)
print(datetime.datetime.now())

print(today - datetime.timedelta(days=1))