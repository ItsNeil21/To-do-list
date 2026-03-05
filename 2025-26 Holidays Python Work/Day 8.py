    #Week 2 of python

#Task : Print numbers 1-100



'''range(1,101)

for i in range(1,101):
    print(i)'''

#sucessful and works

'''range(1,101)

for i in range(1,101):
    if i % 2 == 0:
        print(i)'''
#The task was to print only nums even between 1-100 - successful

'''import random
num = random.randint(1,10)
print(num)
chances = 5
userinput = int(input("Enter a number: "))

while chances > 0:

    while userinput != num:
        userinput = int(input("Enter a number: "))
        chances = chances - 1
        if userinput == num:
            print("You win")
            break'''

#half successful - 1/2 marks lol;


#def addtwonumbers() :
    #num1 = int(input("Enter a number: "))
    #num2 = int(input("Enter the second number: "))
    #more = input("Do you want to add any more numbers? (y/n): ")
    #if more == "y":

    #print(num1+num2)

#addtwonumbers()''''''


#half complete - couldnt be bothered lol :(



'''import random
num = random.randint(1,6)
roll = input("Roll? (y/n) : ")

while roll == 'y':

    print(num)
    roll = input("Roll? (y/n) : ")
    num = random.randint(1, 6)

    if roll == 'n':
        break'''

#successful

import random

print("Welcome to the number guessing game!")
mysterynumber = random.randint(1,100)
print(mysterynumber)
guess = int(input("Guess a number between 1 and 100: "))
chances = 5
while chances > 0:
    while guess != mysterynumber:
        userinput = int(input("Guess a number between 1 and 100: "))
        chances = chances - 1
    if chances <= 0:
     print("You lose, score of zero")
    elif guess == mysterynumber and chances > 0:
        if chances == 5:
            print("You win, score of 100!")
        elif chances == 4:
            print("You win, score of 80!")
        elif chances == 3:
            print("You win, score of 60!")
        elif chances == 2:
            print("You win, score of 40!")
        elif chances == 1:
            print("You win, score of 20!")
