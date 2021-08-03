import datetime
import pandas as pd

today = datetime.date.today()
print(today.month)
print(datetime.datetime.now())

print(today - datetime.timedelta(days=1))
print(today.strftime("%Y年%m月%d日"))

df = pd.DataFrame([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
            ])

print(df)

df = pd.read_csv("housing.csv")
print(df.head)
print(df.iloc[: ,2:])

print(df[df["housing_median_age"] > 30])