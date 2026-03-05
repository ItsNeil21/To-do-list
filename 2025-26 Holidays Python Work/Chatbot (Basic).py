import random
import pyttsx3
import datetime
import scikit-learn

from datetime import datetime

from datetime import date
now = datetime.now()


import datetime


current_time_formatted = now.strftime("%H:%M:%S")

def speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()

print("This is a chatbot! type bye to exit the program")

while True:
    user = input("You: ").lower()

    if "how are you" in user:
        speak("I'm fine")

    elif "hi" in user:
        speak(random.choice(["hello how are you!", "what's up!", "Hey Bro!"]))

    elif "what's the time" in user:
        speak(current_time_formatted)

    elif "tell me a joke" in user:
        speak(random.choice(["why was 6 afraid of 7? because 7 8 9", "I'm fine"]))

    elif "what's the date" in user:
        today = date.today()
        speak("Today is " + str(today))

    '''elif "lets play rock paper scissors" in user:
        while True
            options = ["rock", "paper", "scissors"]
            userinput = input("Your Choice: ").lower()
            myinput = random.choice(options)

            if myinput == userinput:
            speak("It's a draw")
            elif userinput == "rock" and myinput == "scissors" or userinput == "paper" and myinput == "rock" or userinput == "scissors" and myinput == "paper":
            speak("You Win!")
            else :
                speak("I win!! haha")
        playagain = input("Would you like to play again?(y/n)").lower()
        if playagain == "y":
                speak("Okay, let's play again")
        if playagain == "n":
                speak("Okay, that was fun!")
                break'''
    elif "let's play rock paper scissors" in user
    speak("Okay! Let's play rock paper scissors!")

    while True:
        options = ["rock", "paper", "scissors"]
        userinput = input("Your choice (rock, paper, scissors): ").lower()
        myinput = random.choice(options)

        if userinput not in options:
            speak("That's not a valid choice. Try again!")
            continue

        speak(f"I chose {myinput}!")

        if myinput == userinput:
            speak("It's a draw!")
        elif (userinput == "rock" and myinput == "scissors") or \
                (userinput == "paper" and myinput == "rock") or \
                (userinput == "scissors" and myinput == "paper"):
            speak("You win!")
        else:
            speak("I win! Haha!")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            speak("Okay, that was fun!")
            break














