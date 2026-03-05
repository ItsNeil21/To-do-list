import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
all_data = []
data = []
cont = "y"

subjects = ["math", "science", "english", "humanities"]

while cont == "y":

    while True :

        subject_studied = input("What subject did you study : ").lower()
        if subject_studied not in subjects:
            print("Sorry that subject is not supported")
            subject_studied = input("What subject did you study : ").lower()

        time_studied = int(input("How long did you study in minutes : "))
        difficulty = float(input("How difficulty was your study (1-5): "))


        data_of_session = [subject_studied,time_studied,difficulty]
        data.append(data_of_session)
        with open ("Study Data.csv" , "a" ) as f :
            f.write(f"{subject_studied},{time_studied},{difficulty}\n")
            print("Saved to data")
            view = input("Would you like to view the data? (y/n): ")
            if view == "y" :
                print("Here is the data")
                with open ("Study Data.csv" , "r" ) as file :
                    content = file.read()
                    print(content)
                    analyse = input("Analyse data? (y/n) : ")
                    if analyse == "y" :
                        with open("Study Data.csv", "r") as f:
                            next(f)  # skip header if you have one
                            for line in f:
                                line = line.strip()
                                if line:
                                    parts = line.split(",")

                                    subject = parts[0]
                                    time = int(parts[1].strip())
                                    difficulty = float(parts[2].strip().replace("]", "").replace("[", ""))

                                    all_data.append([subject, time, difficulty])

                        times = [row[1] for row in all_data]
                        difficulty = [row[2] for row in all_data]
                        print("\n" "------Analysis-----")
                        nplise_time_sum = np.sum(times)
                        nplist_time_avg = np.mean(times)
                        nplist_difficulty_avg = np.mean(difficulty)
                        print("Total Time studied in minutes: " + str(nplise_time_sum))
                        print("Average time studied : " + str(nplist_time_avg))
                        print("Average difficulty : " + str(nplist_difficulty_avg))
                        df = pd.read_csv("Study Data.csv", names = ["subject", "time", "difficulty"])
                        grouped = df.groupby("subject")["time"].sum().reset_index()

                        plt.bar(grouped["subject"], grouped["time"])
                        plt.ylabel("Time")
                        plt.xlabel("Subject")
                        plt.title("Study time by subject")
                        plt.show()


        cont = input("Would you like to log another session? (y/n) : ")