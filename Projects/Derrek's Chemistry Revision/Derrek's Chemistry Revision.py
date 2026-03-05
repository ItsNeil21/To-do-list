
#import all libraries

import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image
import time

#PIL = pillow # from pillow import Image

df = pd.read_csv("Derrek's Data.csv")

#Create dictionary of questions and answers

questions = [
    {"question": "What is the chemical symbol for water?", "answer": "h2O"},
    {"question": "What is the chemical symbol for sodium?", "answer": "na"},
    {"question": "What do you call a substance made of only one type of atom?", "answer": "element"},
    {"question": "What is the chemical formula for carbon dioxide?", "answer": "co2"},
    {"question": "What gas do plants release during photosynthesis?", "answer": "oxygen"},
    {"question": "What is the chemical symbol for hydrogen?", "answer": "h"},
    {"question": "What is the pH of pure water?", "answer": "7"},
    {"question": "What is the most abundant gas in the Earth's atmosphere?", "answer": "nitrogen"},
    {"question": "What type of reaction combines two or more substances to make a new substance?", "answer": "synthesis"},
    {"question": "What is the chemical formula for table salt?", "answer": "nacl"},{"question" : "Identify the molecule shown.", "image" : "image/download.png", "answer" : "water"}
]

#Create counter / score variable

count = 0

attempt = input("What attempt is this : ")

#Loop through and ask questions

for q in questions :
    if "image" in q:
        img = Image.open(q["image"])
        img.show()
    user_ans = input(q["question"] + " ").strip()
    if user_ans.lower() == q["answer"].lower() :
        print("You got it correct!")
        count += 1
    else :
        print("Oops, you got it wrong. The answer is " + q["answer"])

print("You got a score of " + str(count) + "/11")

new_row = pd.DataFrame([{"attempts": attempt, "score": count}])


new_row.to_csv("Derrek's Data.csv", mode="a", index=False, header=False)

print("\nCurrent Data Analysis\n")
mean_score = df["Score"].mean()
mid_Score = df["Score"].median()
print("Mean Score: " + str(mean_score))
print("Median Score: " + str(mid_Score))

x = df["Attempts"].values
y = df["Score"].values

time.sleep(5)

plt.bar(x,y)
plt.ylabel("Score")
plt.xlabel("Attempts")
plt.show()













