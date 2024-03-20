import random
import time
import os
import sys

random.seed(os.urandom(1024))


def wait_for_input():
    controls_read = input()
    while controls_read == "":
        break


print("")
print("Welcome to Dark Pythons: Echoes of the Fallen Code.")
print('')
print('Controls: W,A,S,D to move directions, E to interact and Q for misc actions.')
print("After every line of dialogue, the video game will wait for the enter key's input to continue:")
wait_for_input()
print("In a world where reality is intertwined with the digital, an ancient curse has fallen over the land of "
      "Pythorean; \ncorrupting its code and trapping its inhabitants in an endless loop of death and despair. Legends "
      "tell of an emboldened hero who will traverse the treacherous \ndepths of the Cursed Library, the perilous "
      "fields of NullPointer, and the dreaded Castle of SegFault, to find and reset the Core of Creation, "
      "thus lifting the \ncurse and restoring balance to Pythoria:")
wait_for_input()

print('================================================================')

player = {  # Player will have a name and class given by the user, player class will affect base damage and health
    # Health will be increased through player leveling system and damage will be increased through damage on players
    # weapon (builds upon base damage)
    'name': '',
    'class': '',
    'hp': 0,
    'damage': 0,
    'stamina': 0,
}

enemy = [
    {
        'basic enemy': [
            {'name': 'Corrupted Code Fragment'},
            {'hp': 50},
            {"damage": 2},
        ],
        'advanced enemy': [
            {'name': 'Unsolvable Bug'},
            {'hp': 50},
            {"damage": 2},
        ]
    }]

items = [
    {
        'Weapon': [
            {'Name': 'Iron Sword', 'Damage': 20},  # Starting weapon for Knight class
            {'Name': 'Katana', 'Damage': 15},  # Starting weapon for Samurai class
            {'Name': 'Cerulean Staff', 'Damage': 18},  # Starting weapon for Mage class
            {'Name': 'Dagger', 'Damage': 12},  # Starting weapon for Bandit class
        ],
        'Weapon tier two': [
            {'Name': 'Coins', 'Amount': 500},
            {'Name': 'Health Potion', 'Health_Given': 30, 'Amount': 1},
            {'Name': 'Mana Potion', 'Health_Given': 50, 'Amount': 1},
            {'Name': 'Stamina Potion', 'Health_Given': 70}
        ]
    }
]

locations = ["Locked Room", "Cursed Library", "Fields of NullPointer", "Castle of SegFault"]


def player_character():
    player['class'] = input()
    if player['class'] == 'Knight':
        player['damage'] = 20
        player['hp'] = 100
        print('You are a warrior')
    elif player['class'] == 'Samurai':
        player['damage'] = 10
        player['hp'] = 100
        print('You are a warrior')
    elif player['class'] == 'Mage':
        player['damage'] = 10
        player['hp'] = 100
        print('You are a warrior')
    elif player['class'] == 'Bandit':
        player['damage'] = 10
        player['hp'] = 100
        print('You are a warrior')


def Locked_room():
    print('You wake up in a dimly lit room, disorientated. Looking above you, you see a hole in the ceiling, '
          'the sun is shinning brightly through it')
    wait_for_input()
    print('"Is that, a person?"')
    wait_for_input()
    print("You see what looks to be a man, dressed in a set of steel medieval armour")
    wait_for_input()
    print('The man reaches out his hand and drops something through the hole. You watch the object fall until its '
          'right in front of you')
    wait_for_input()
    print('"A Key!"')
    print("You grab the key. The man leaves. And you stand up.")
    wait_for_input()
    user_input = input("Press W to walk towards the door or Q to explore the room ").upper()
    if user_input == 'W':
        print("You walk towards the door.")
        print("The keyhole looks rusty")
        user_input = input("Press E to use key").upper()
        if user_input == 'E':
            print("You used the key on the door. As you open the door, a wall encoded with ")


        else:
            print("You failed to use the key")
            user_input = input("Use E to try the key again or Q to explore the room ").upper()
            if user_input == 'E':
                print("You used the key on the door")
            elif user_input == 'Q':
                print("You investigate the room, determined to find out how you got yourself into this situation ")
                print("But you find nothing")
    elif user_input == 'Q':
        print("You investigate the room, determined to find out how you got yourself into this situation ")
        print("But you find nothing")


Locked_room()
