import pandas as pd
df = pd.read_csv("weather_data.csv")
# df = pd.DataFrame(df)
rows , colomn = df.shape
# print(df)
# print(rows)
# print(colomn)
# print(df.head())
# print(df.head(2)) 
# print(type(df['day']))
x = df[["event" , "day" ]]


x = df["temperature"].max()
x = df.describe()
print(x)
print(df[df.temperature >= 32])