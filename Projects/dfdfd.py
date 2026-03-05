# import  libraries
#
import random

# vars

player_name = "None"
player_hp = 10
Player_class = "None"
player_armour = 0
player_initiative = 0
player_arrows = 0
Player_stamina = 0

enemy_health = 10
enemy_armour = 0
enemy_initiative = 0
enemy_attack = 0
enemy_arrows = 0

action = "None"
fight_action = 0
sickness = 0
slave_trainee = 0
warrior_number_dismounted = 0  # health 30
warrior_number_mounted = 0  # health 15
warrior_number_ranged = 0  # health 10
random_event = 0
area = 0
inventory = {""}
player_melee_weapon = ["fists"]
player_ranged_weapons = [""]

Player_stamina = 50
area = 1

while sickness > 5 and player_hp != 0:
    if sickness > 5:
        print("You have been sick for too long. You have died of sickness. Game over.")
        break

    if player_hp <= 0:
        print("You are dead. Game over.")
        break


# start_game

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

player_name = input("You there! What is your name? : \n")

print("Well you're in luck today! You've been drafted into the army. Now, snap to it!\n")
print("The warrior opens the cage and ties your hand together.\n")

action = input("What do you do? (1.fight out of the bonds,2.comply,3.don't move)(1/2/3) : \n")

if action == "1":
    print(
        "You try to fight out of the bonds, but they are too tight. You struggle for a bit, but eventually give up. \n" \
        "The warrior looks at you and says, 'You should have just stayed put. Now, you are going to have to work twice as hard to get out of this mess. \n The warrior lunges at you with a gold spear and strikes you in the thigh'\n")
    player_hp = player_hp - 1.5


elif action == "2":
    print(
        "You comply with the warrior and follow him. He looks at you and says, 'Good, now you're learning. You'll be a fine soldier in no time.'\n")

else:
    print(
        "You don't move. The warrior looks at you and says, 'What are you doing?  Get moving!' He then hits you with the back of his spear, causing you to fall to the ground. He then drags you to the camp.\n")
    player_hp = player_hp - 0.5

print(
    "\nThe heavily armed warrior leads you to the middle of the camp. \n In the middle of the camp there is a large fire pit. Around them, you see several other slaves, all of them are in various states of exhaustion and despair. \n )'Lets have a look at you, pair up and grab a staff)' the warrior hurls a stack of wooden sticks at you.\n")

random_event = random.randint(1, 6)
if Player_stamina > 35:
    random_event = random_event + 5

if random_event >= 5:
    action = input(
        "What do you do? 1. (catch the staff) 2. (move out of the way) 3. (act dumb and let the staff hit you)\n")
    if action == 1:
        inventory.append("staff")
        for i in player_melee_weapon:  # this is to replace the player's melee weapon with the staff, but if the player has fists, it will not remove it and just add the staff to the inventory
            if i != "fists":
                player_melee_weapon.remove(i)
                player_melee_weapon.append("staff")
    elif action == 2:
        print(
            "\nThe staff flies through the air and lands nearby you as you move out of the way. \n The warrior looks at you in rage and says, 'You should have just caught the staff!' He then walks over to you and hits you on the head with another staff as punishment for not catching the staff.\n")
        player_hp = player_hp - 1
    else:
        print(
            "\nYou act dumb and let the staff hit you. You take damage and the warrior looks at you and says, 'You should have caught the staff! As punishment, you will not get to use one'. He then walks over and takes the staff off of you.\n")
        print(" \nYour exhaustion got the better of you and the staff hits you in the head as you try to grab it.\n")
        player_hp = player_hp - 1

# Combatcode

print(f" An enemy approaches {player_name}!")

if area == 1:
    slave_trainee = random.randint(1, 3)  # spawn 1-3 slave trainees


def combat():
    arrow_damage = 0

    player_initiative = random.randint(1, 20)
    enemy_initiative = random.randint(1, 20)
    while warrior_number_dismounted >= 1 or warrior_number_mounted >= 1 or warrior_number_ranged >= 1:
        while enemy_health > 0:
            if player_initiative > enemy_initiative:
                print("You are faster. \n")
                action = input(
                    "What do you do? (Fight(1) Run(2) hide(3) surrender (4) ) : ")  # replace other stuff with other actions that the player can do in combat, such as defend, use an item, etc.

        while action == '1':
            fight_action = input(
                f"what do you do? 1. strike with {player_melee_weapon[1]} 2. block 3. shoot with {player_ranged_weapons[0]} (if you have one) 4. use an ability (if you have one) 5. surrender")
            if fight_action == 3 and player_ranged_weapons != "" and player_arrows != 0:
                player_hit_chance = random.randint(1, 20)
                if player_hit_chance > enemy_armour:
                    arrow_damage = random.randint(5, 7)
                    enemy_health = enemy_health - arrow_damage
                    player_arrows = player_arrows - 1
                    Player_stamina = Player_stamina - 15

                    fight_action = input(
                        "You have hit the enemy with your shot. what do you do? 1. close to close combat 2. remain at a distance and shoot again (chance for faliour) 3. retreat and return again (skip enemy turn) 4. use an ability (if you have one) 5. general retreat (get out of combat)")
                    if fight_action == 1:
                        fight_action = input(
                            "\n you close to close combat. \n what do you? 1. strike with melee weapon 2. block 3. use an ability (if you have one) 4. surrender")
                        if fight_action == 1:
                            continue
                        elif fight_action == 2:

                if fight_action == 1:
                    if player_melee_weapon == "fist":
                        player_hit_chance = random.randint(1, 20)
                        if Player_stamina > 25:
                            player_hit_chance = player_hit_chance + 5
                        else:
                            player_hit_chance = player_hit_chance - 5

                            if player_hit_chance >= 9:
                                enemy_health = enemy_health - 1
                                Player_stamina = Player_stamina - 5
                    if player_melee_weapon == "sword":
                        player_hit_chance = random.randint(1, 20)
                        if Player_stamina > 25:
                            player_hit_chance = player_hit_chance + 5
                        else:
                            player_hit_chance = player_hit_chance - 5

                        if player_hit_chance >= 7:
                            enemy_health = enemy_health - 5


    else:
        print("The enemy is faster.")


if area == 2:
    warrior_number_dismounted = random.randint(1, 5)  # spawn 1-3 dismounted warriors
    warrior_number_ranged = random.randint(1, 3)  # spawn 1-3 ranged warriors
    warrior_number_dismounted = random.randint(1, 5)  # spawn 1-3 mounted warriors

combat()

if area == 3:

# enemy actions















