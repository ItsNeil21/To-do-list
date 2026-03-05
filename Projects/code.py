# import libraries

import random
import time

# defined variables

player_name = "None"
player_hp = 10
Player_class = "None"
player_armour = 0
player_initiative = 0
player_arrows = 0
Player_stamina = 0
player_attacks = 1
player_atk = 1

enemy_health = 10
enemy_armour = 0
enemy_initiative = 0
enemy_attack = 0
enemy_arrows = 0

action = "None"
fight_action = 0

warrior_number_dismounted = 0
warrior_number_mounted = 0
warrior_number_ranged = 0
siege_unit = 0
random_event = 0
area = 0
inventory = {}
player_melee_weapon = ["fists"]
player_ranged_weapons = [""]
campaign_progress = 0
campaign = False
money = 0

Player_stamina = 50
area = 1


# start defs

def campaign_start():
    print(
        "\n After several weeks resting in camp, you are summoned to formation.\n The rest of your tuman (group of 1000 soldiors equivilent ot a modern company) stands at atention with their horses besides them. \n")
    print(
        "\n Your comanding general steps foward into the parade ground leading two idugan (shamens).\n The idugan steps fowards and lights two great bonfires.\n They roar to life, flame rising in the air.\n The idugan then takes a bowl of Kumis (fermented mares milk) and pours onto the ground. \n An offering to the gods to a successfull campaign. \n")
    print(
        "\n The commanding general steps foward.\n he draw his sword and slashes it through the flames, letting it clense the evil from this campaign.\n The rest of the tuman follows suit, drawing their swords and inundating them with fire. \n ")
    print(
        "\n The rest of the equiptment is clensed in the same way by the indugan. \n After this, the tuman-u-noyan (commanding general) draws his sword and adresses the gathered soldiors, 'We have survived many hardships and campaings together. \n There are some new units amung us, know this, we take care of our own and so, to a succesfull campaign. \n With the end of the comanders speach, there was a roar of affermaiton and they where dismissed to their barracks. \n They would leave tomorow morning. \n' ")


def start_game():
    print("\nWelcome to KhanBound!\n")
    print(
        "You are a slave that was captured on the earliest raids conducted by \n the Mongol Empire. Over the short time that you have been captured, you have seen the vibrant grasslands of the steeples, the rocky highlands of Central Asia and the vibrant lakes of the Blue Pearl.\n")
    print(
        "Inside your cage, drawn by a heavyset ox, you see the vastness of the mongolian grasslands. \n Between the bars of your cage, you see what seems to be a herd of horses drawing circular tents. Riding on them, there were heavily armed warriors in heavy brocade clothes. They had several bows slung across their saddle bow and carried multiple quivers of arrows.\n")
    print(
        "The sun rose high in the sky, warming your skin. Suddenly, the oxen stopped. You watch as the armed warriors step down from their horses start to make camp.\n")
    print("One of the warriors approach you.\n")


start_game()

player_name = input("\n You there! What is your name? : ")

# warrior asks

Player_class = input(
    "\n The warrior looks at you and says, 'You are going to be trained to fight for the Mongol Empire. You will be trained in one of two classes. Which class do you want to be trained in? \n 1. Bowman \n 2. Swordsman \n  Please enter the number of the class you want to be trained in : ")
if Player_class == "1":

    print(f"'Excellent choice, {player_name}. You will be trained as a bowman.\n")

else:
    print(f"'Excellent choice, {player_name}. You will be trained as a swordsman.\n")

print(
    "\n The warrior takes you to a training area where there are several other slaves that are being trained. You see a group of slaves that are being trained in archery \n and another group that is being trained in sword fighting.\n You are taken to the group that is being trained in your chosen class.\n")

# start combat training

wins = 0

while wins < 3:

    if Player_class == "1":
        enemy_points = 0
        player_points = 0

        print("'I will go first, show me what you got! \n'")

        while enemy_points < 3 and player_points < 3:
            enemy_hit = random.randint(1, 6)
            if enemy_hit <= 3:
                print(
                    "The warrior takes out a target and shoots an arrow at it. The arrow hits the target dead center. \n")
                enemy_points += 1

            else:
                print("The warrior takes out a target and shoots an arrow at it. The arrow misses the target. \n")

            print(f"The score is now you {player_points} to {enemy_points} the trainer \n")
            print("Now it's your turn! \n")
            print("You take out your bow and shoot an arrow at the target.\n")
            num = int(input("Pick a number from 1 to 5 : "))
            random_num = random.randint(1, 5)
            if num >= random_num:
                print(f"Your arrow hits the target dead centre! \n")
                player_points += 1
                print(f"The score is now you {player_points} to {enemy_points} the trainer \n")

            else:
                print(f"Your arrow misses the target. \n")
                print(f"The score is now you {player_points} to {enemy_points} the trainer \n")

        if player_points == 3:
            print("Congratulations! You have won the training session. \n")
            wins += 1
        else:
            print("You have lost the training session. Try again. \n")

    else:
        enemy_points = 0
        player_points = 0

        print("'I will go first, show me what you got! \n'")

        while enemy_points < 3 and player_points < 3:
            enemy_hit = random.randint(1, 6)
            if enemy_hit <= 3:
                print(
                    "The warrior takes out a target and swings his sword at it. The sword hits the target dead center. \n")
                enemy_points += 1

            else:
                print("The warrior takes out a target and swings his sword at it. The sword misses the target. \n")

            print(f"The score is now you {player_points} to {enemy_points} the trainer \n")
            print("Now it's your turn! \n")
            print("You take out your sword and swing it at the target.\n")
            num = int(input("Pick a number from 1 to 5 : "))
            random_num = random.randint(1, 5)
            if num >= random_num:
                print(f"Your sword hits the target dead centre! \n")
                player_points += 1
                print(f"The score is now you {player_points} to {enemy_points} the trainer \n")

            else:
                print(f"Your sword misses the target. \n")
                print(f"The score is now you {player_points} to {enemy_points} the trainer \n")

        if player_points == 3:
            print("Congratulations! You have won the training session. \n")
            wins += 1
        else:
            print("You have lost the training session. Try again. \n")