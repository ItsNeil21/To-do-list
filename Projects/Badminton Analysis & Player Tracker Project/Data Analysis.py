#import libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Read csv
df = pd.read_csv("PLAYER DATA.csv")

# Convert W/L to numeric for easier calculation (1 = Win, 0 = Loss)
df["Win_numeric"] = (df["W/L (Singles)"] == "W").astype(int)

# Group by Player and calculate mean win rate
win_rates = df.groupby("Player")["Win_numeric"].mean()

# Print results
for player, rate in win_rates.items():

    print(f"{player}'s mean win rate is {rate:.2%}")
