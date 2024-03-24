import random
import time
import os
import sys

random.seed(os.urandom(1024))


def setup_player():
    player = {
        'name': introduction(),
        'hp': 0,
        'stamina': 0,
        'level': 1,
        'location': None,
        'class': None,  # This will be set by the player_class function
        'Attacks knight': [{'Name': '', 'MinDamage': 0, 'MaxDamage': 0},
                           {'Name': '', 'MinDamage': 0, 'MaxDamage': 0}],
        'Attacks samurai': [{'Name': '', 'MinDamage': 0, 'MaxDamage': 0},
                            {'Name': '', 'MinDamage': 0, 'MaxDamage': 0}],
        'Attacks mage': [{'Name': '', 'MinDamage': 0, 'MaxDamage': 0},
                         {'Name': '', 'MinDamage': 0, 'MaxDamage': 0}],
        'Attacks bandit': [{'Name': '', 'MinDamage': 0, 'MaxDamage': 0},
                           {'Name': '', 'MinDamage': 0, 'MaxDamage': 0}],
    }
    player = player_class(player)  # Now, we're properly passing the player dictionary
    return player



def wait_for_input():
    controls_read = input()
    while controls_read == "":
        break
    return controls_read


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
        'Weapon tier1': [
            {'Type': 'Sword', 'Name': 'SharpArray', 'Damage': 20},  # Starting weapon for Knight class
            {'Type': 'Katana', 'Name': 'CyberSlicer', 'Damage': 15},  # Starting weapon for Samurai class
            {'Type': 'Staff', 'Name': 'CodeCaster', 'Damage': 18},  # Starting weapon for Mage class
            {'Type': 'Dagger', 'Name': 'AsyncEdge', 'Damage': 12},  # Starting weapon for Bandit class
        ],
        'Weapon tier2': [
            {'Type': 'Sword', 'Name': 'RecurseRipper', 'Damage': 500},
            {'Type': 'Katana', 'Name': 'SliceIndexer', 'Health_Given': 30, 'Amount': 1},
            {'Type': 'Staff', 'Name': 'GambitGenerator', 'Health_Given': 50, 'Amount': 1},
            {'Type': 'Dagger', 'Name': 'FatalFloat', 'Health_Given': 70}
        ],
        'Weapon tier3': [
            {'Type': 'Sword', 'Name': 'DefBlade', 'Amount': 500},
            # Combining the Python function definition keyword def with "Blade", suggesting a sword that can define or alter reality itself, following the rules of its wielder, much like a function follows its defined parameters and actions.
            {'Type': 'Katana', 'Name': 'CyberShinobi', 'Health_Given': 30, 'Amount': 1},
            {'Type': 'Staff', 'Name': 'YieldScepter', 'Health_Given': 50, 'Amount': 1},
            {'Type': 'Dagger', 'Name': 'ByteBlade', 'Health_Given': 70}
        ]
    }
]


#random_encounter = random.randint(0, 2)
#wild_enemy = enemy[random_encounter]
#enemy_attack_randomizer = random.randint(0, len(wild_enemy['Attack']) - 1)

inventory = []
locations = ["Cursed Library", "Fields of NullPointer", "Castle of SegFault"]


def introduction():
    name = input("Enter the name of your hero: ")
    print("")
    print(f'Welcome {name}, to Dark Pythons: Echoes of the Fallen Code.')
    print('Controls: W,A,S,D to move directions, type in your preferred action when provided.')
    print("After every line of dialogue, the video game will wait for the enter key's input to continue:")
    print("Remember, this is a story game, so make sure you do everything you can for the full experience!")
    wait_for_input()
    print("In a world where reality is intertwined with the digital, an ancient curse has fallen over the land of "
          "Pythorean; \ncorrupting its code and trapping its inhabitants in an endless loop of death and despair. Legends "
          "tell of an emboldened hero who will traverse the treacherous \ndepths of the Cursed Library, the perilous "
          "fields of NullPointer, and the dreaded Castle of SegFault, to find and reset the Core of Creation, "
          "thus lifting the \ncurse and restoring balance to Pythoria:")
    wait_for_input()

    print('================================================================')


def print_player_info(player):
    print(f"\nPlayer Information:")
    print(f"Name: {player['name']}")
    print(f"Class: {player['class']}")
    print(f"HP: {player['hp']}")
    print(f"Stamina: {player['stamina']}")
    print(f"Level: {player['level']}")
    # Add more details as needed.


def player_class(player):
    while True:
        print("Welcome, fragmented one. You have been chosen by the order in hopes you have what it takes to find and "
              "reset the core of creation!")
        player['class'] = input("The first step in your journey is picking your players class. Do you wish to be a "
                                "fierce knight, a humble samurai, a keen mage, or a sneaky bandit. ("
                                "knight/samurai/mage/bandit): ")
        if player['class'] == 'knight':
            player['damage'] = 20
            player['hp'] = 100
            player["Attack knight"].append({'Name': 'Slash', 'MinDamage': 5, 'MaxDamage': 10})
            inventory.append(items[0]['Weapon tier1'][0])
            break
        elif player['class'] == 'samurai':
            player['damage'] = 10
            player['hp'] = 100
            player["Attack samurai"].append({'Name': 'bleed', 'MinDamage': 5, 'MaxDamage': 10})
            inventory.append(items[0]['Weapon tier1'][1])
            break
        elif player['class'] == 'mage':
            player['damage'] = 10
            player['hp'] = 100
            player["Attack mage"].append({'Name': 'rock sling', 'MinDamage': 5, 'MaxDamage': 10})
            inventory.append(items[0]['Weapon tier1'][2])
            break
        elif player['class'] == 'bandit':
            player['damage'] = 10
            player['hp'] = 100
            player["Attack bandit"].append({'Name': 'Stab', 'MinDamage': 5, 'MaxDamage': 10})
            inventory.append(items[0]['Weapon tier1'][3])
            break
    return player


def locked_room():
    print('You wake up in a dimly lit room. The air is thick with dust and the scent of ancient parchment. You '
          'remember nothing of how you came to be here, only that the darkness outside this room calls to you, '
          'whispering of a curse and a core...:')
    wait_for_input()
    while True:
        action = input("\nWhat do you do? (inspect/call/sit): ").lower().strip()
        if action == 'inspect':
            print("\nYour hands brush against the cold stone wall, feeling for a seam. Your fingers catch on a loose "
                  "stone and press it instinctively. A section of the wall grinds open, revealing a sliver of freedom.")
            break
        elif action == 'call':
            print("\nYour voice echoes through unseen halls, met only by silence. It seems you are alone in this "
                  "predicament.")
            wait_for_input()

        elif action == 'sit':
            print("\nAs despair threatens to take hold, you remind yourself that succumbing to it will not change "
                  "your fate. It's time to act.")
            wait_for_input()
        else:
            print("\nUnknown action. Your survival depends on making the right choices.")
            wait_for_input()
    print("\nStepping through the secret passage, you find yourself on a path winding through an ethereal landscape, "
          "torn between realms.")
    print("Suddenly, the ground beneath you gives way, and you are consumed by swirling darkness...")


def generate_damage(attack):
    return random.randint(attack['MinDamage'], attack['MaxDamage'])


def game_reload(player):
    if player['hp'] <= 0:
        player['hp'] = 100
        all_locations(player['Location'])


 # def battle():
     # print("You encountered a wild", wild_enemy['Name'])
    # print("It's a", wild_enemy['Type'], "Type!")
    # print("It has", wild_enemy['Health'], "Health")
    # print("It's a level", wild_enemy['Level'])

    #  while True:
    #     till_encounter = random.randint(1, 2)
    #     time.sleep(till_encounter)
    #   print('Begin Battle!')
    #  break

    # while player['Health'] > 0 and wild_enemy['Health'] > 0:
    #    user_input = input('Enter 1 to attack, 2 to throw a pokeball, 3 to flee the battle: ')

    #  if user_input == '1':
    #   attack_choice = random.choice(player['Attacks'])
    #   Damage_own = generate_damage(attack_choice)
    #    print(player['Name'], 'attacked the wild', wild_enemy['Name'], 'with', attack_choice['Name'])
    #  if player['Type'] == "Fire" and wild_enemy['Type'] == "Grass":
    #     wild_enemy['Health'] -= Damage_own * 1.5
    #   elif player['Type'] == "Fire" and wild_enemy['Type'] == "Water":
    #      wild_enemy['Health'] -= Damage_own * 0.5
    #  else:
    #       wild_enemy['Health'] -= Damage_own
    #  print("The attack did", Damage_own, 'damage')

    #  if wild_enemy['Health'] <= 0:
    #      break
    # else:
    #     print("The", wild_enemy['Name'], "has", wild_enemy['Health'], "health remaining")
    #  till_encounter = random.randint(1, 2)
    #  time.sleep(till_encounter)

    # print("The wild", wild_enemy['Name'], 'attacked you back!')
    # print(wild_enemy['Name'], 'used', wild_enemy['Attack'][enemy_attack_randomizer]['Name'])
    #   Damage_enemy = generate_damage(wild_enemy['Attack'][enemy_attack_randomizer])

    #  if player['Type'] == "Fire" and wild_enemy['Type'] == "Grass":
    #     player['Health'] -= Damage_enemy * 1.5
    #  elif player['Type'] == "Fire" and wild_enemy['Type'] == "Water":
    #    player['Health'] -= Damage_enemy * 0.5
    #  else:
    #      player['Health'] -= Damage_enemy
    #  print('The wild', wild_enemy['Name'], 'did', Damage_enemy, 'damage to', player['Name'])
    #  print(player['Name'], 'has', player['Health'], 'health left')

    # elif user_input == '2':
    #    print('You fled the battle!')
    #     break

    # else:
    # print("You can't do that")

    #  if player['Health'] <= 0:
    # print("All your health has been depleted!")
    # print("Game is reloading from beginning of current area")
    #   game_reload()
    # elif wild_enemy['Health'] <= 0:
    # print("The wild", wild_enemy['Name'], "fainted!")
    # if wild_enemy['Level'] == 3:
    #   player['Level'] += 0.25
    # elif wild_enemy['Level'] == 4:
    # player['Level'] += 0.5
    # elif wild_enemy['Level'] == 5:
    # player['Level'] += 0.75
    # elif wild_enemy['Level'] == 6:
    # player['Level'] += 1
    # print("The battle ended.")
    # if player['Level'] > 5:
    # print(f"Charmander leveled up to level {player['Level']}!")
    #enemy['hp'] -= player['attack']
    # return player, enemy, items


def all_locations(player):
    chosen_location = player['location']
    if chosen_location == "Fields of NullPointer":
        Fields_of_NullPointer()
    elif chosen_location == "Cursed Library":
        Cursed_Library()
    elif chosen_location == "Castle of SegFault":
        Castle_of_SegFault()


def Cursed_Library():
    locations.remove("Cursed Library")
    print(
        f"\nYou awaken. Looking into the sky, the name Cursed Libray appears in bold writing. It's time to uncover "
        f"your destiny and perhaps, the fate of Pythoria itself.")


def Fields_of_NullPointer():
    current_location = "Fields of NullPointer"
    print(
        f"\nYou awaken. Looking into the sky, the name Fields of NullPointer appears in bold writing. It's time "
        f"to uncover your destiny and perhaps, the fate of Pythoria itself.")

    locations.remove("Fields of NullPointer")


def Castle_of_SegFault():
    current_location = "Castle of SegFault"
    print(
        f"\nYou awaken. Looking into the sky, the name Castle of SegFault appears in bold writing. It's time to "
        f"uncover your destiny and perhaps, the fate of Pythoria itself.")
    locations.remove("Castle of SegFault")

def main():
    player = setup_player()  # Initialize the player dictionary
    print_player_info(player)  # Print the player's details

if __name__ == "__main__":
    main()

