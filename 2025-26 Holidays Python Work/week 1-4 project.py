import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sleep_data = []

cont = "y"

print("Welcome to sleep tracker, Neil.")

while cont == "y":
    while True :
        hours = float(input("How long did you sleep for in hours : "))
        quality = float(input("What was the quality of your sleep (1-5) : "))
        time_Taken = float(input("How long did it take for you to fall asleep for in hours : "))
        session_Data = [hours, quality, time_Taken]
        sleep_data.append(session_Data)
        with open("Data.csv", "a") as f:
            f.write(f"{hours},{quality},{time_Taken}\n")
            print("Saved Successfully")
            analyse = input("Analyse data ? (y/n) :  ")
            if analyse == "y":
                df = pd.read_csv(
                    "Study Data.csv",
                    names=["Hours_Slept", "Quality", "Time_Taken"],
                    encoding="cp1252"  # or "latin1"
                )

                # Extract columns for NumPy analysis if needed
                col1 = df["Hours_Slept"].to_numpy()
                col2 = df["Quality"].to_numpy()
                col3 = df["Time_Taken"].to_numpy()
                print("\n------Analysis------")
                print("Average time slept in hours" + str(round(np.mean(col1), 2)))
                print("Average quality of sleep" + str(round(np.mean(col2)), 2))
                print("Average time taken to sleep in hours" + str(round(np.mean(col3), 2)))


