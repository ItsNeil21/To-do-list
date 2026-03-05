import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


df = pd.read_csv("icecream data.csv")
x = df["Temperature"].values.reshape(-1, 1)
y = df["Sold"].values


model = LinearRegression()
model.fit(x,y)


new_temp = float(input("What is the temperature? :"))
current = np.array([[new_temp]])
if current > 20  :
    prediction = model.predict(current)
    print("Predicted sales for", new_temp, "°C:", prediction[0])

else :
    print("Too cold for Icecream !!!")

