import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("adelaide_weather_sample.csv")

X = df[["MaxTemp_C","MinTemp_C","Humidity_3pm_%","WindSpeed_kmh"]].values
y = df["Rain_mm"].values

model = LinearRegression()
model.fit(X,y)

current_max = float(input("Enter Max Temperature in Celsius: "))
current_min = float(input("Enter Min Temperature in Celsius: "))
current_hum = float(input("Enter Current Humidity in %: "))
current_wind = float(input("Enter Current Wind Speed in km/h: "))

user_input = [[current_max, current_min, current_hum, current_wind]]
y_prediction = model.predict(user_input)[0]

if y_prediction < 0 :
    print("I dont think it will rain today.")

else :
    print(f'I think it will rain {y_prediction} mm today')



