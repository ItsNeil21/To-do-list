import random

print("Welcome to Team Allocator")

players = []
response = input("Do you want to add another name (y/n)? : ")
while response.lower() != "y":
 names = input("Enter names here : ")
 players.append(names)
response = input("Do you want to add another name (y/n) : ?")