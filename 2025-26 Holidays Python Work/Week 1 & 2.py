#Project 1 : Calculator

'''var_continue = "true"
while var_continue == "true":
    operator = input ("What would you like to do? : ")
    if operator == "add":
        num1 =  int(input("Enter first number : "))
        num2 = int(input("Enter second number : "))
        print(num1 + num2)

    elif operator == "subtract":
        num1 = int(input("Enter first number : "))
        num2 = int(input("Enter second number : "))
        print(num1-num2)

    elif operator == "multiply":
        num1 = int(input("Enter first number : "))
        num2 = int(input("Enter second number : "))
        print(num1*num2)

    elif operator == "square":
        num1 = int(input("Enter first number : "))
        num2 = int(input("Enter second number : "))
        print(num1**num2)

    else :
        num1 = int(input("Enter first number : "))
        num2 = int(input("Enter second number : "))
        print(num1/num2)

    cont = input("Would you like to continue? (y/n) : ")

    if cont == "n" :
        break

    else :
        continue'''

#The calculator works and is effective - tick.

#Project 2 : Username Generator

'''import random

samplenames = ["CyberNomad", "PolitePanda", "PixelWarrior","DataDreamer"]

username = random.choice(samplenames)

print(username) '''

#The generator works - tick.

#Project 3 : Guess the number
import random

'''import random

number = random.randint(1, 10)
guesses = 0

while True:
    guess = int(input("Guess a number between 1 and 10: "))
    guesses += 1

    if guess == number:
        print("Correct!")
        print("Guesses:", guesses)
        break
    elif guess < number:
        print("Too low")
    else:
        print("Too high")'''

'''import numpy as np
players = np.array(["Bob", "Neil" , "Derrek", "Jonathan", "J    ack"])
scores = np.random.randint(0,101,size=len(players))
print(players)
print(scores)
print("The mean of the scores is", np.mean(scores))
print("The highest score is", np.max(scores))
print("The lowest score is", np.min(scores))
print("The median score was", np.median(scores))
print("The standard deviation of the scores was", np.std(scores))
top_scores = scores[scores>=70]
top_players = players[scores>=70]
print("The top player/s are", top_players)
print("The top score/s are", top_scores)
sorted_scores = np.argsort(scores)[::-1]
top3_players = players[sorted_scores][:3]
print("The top 3 player/s are", top3_players)
print("The top score/s are", top_scores)
import matplotlib.pyplot as plt


plt.bar(players, scores)
plt.xlabel("Players")
plt.ylabel("Scores")
plt.title("Player Scores Dashboard")
plt.show()'''

import pandas as pd

df = pd.read_csv("CSV TEST.csv")


df["passed"] = df["Score"] >= 60
df["age"] = df["Score"] / 10
print(df.head())
a = df.groupby("age")["Score"].mean()
print(a)
x = df.describe()
print(x)