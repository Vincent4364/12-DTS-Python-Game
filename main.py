import random
import time
import os
import sys

random.seed(os.urandom(1024))


def wait_for_input():
    controls_read = input()
    while controls_read == "":
        break
    return controls_read


player = {  # Player will have a name and class given by the user, player class will affect base damage and health
    # Health will be increased through player leveling system and damage will be increased through damage on players
    # weapon (builds upon base damage)
    'name': '',
    'class': '',
    'hp': 0,
    'stamina': 0,
    'level': 1,
    'Attacks_knight': [{'Name': '', 'MinDamage': 0, 'MaxDamage': 0},
                        {'Name': '', 'MinDamage': 0, 'MaxDamage': 0}
                ],
    'Attacks_samurai': [{'Name': '', 'MinDamage': 0, 'MaxDamage': 0},
                        {'Name': '', 'MinDamage': 0, 'MaxDamage': 0}
                ],
    'Attacks_mage': [{'Name': '', 'MinDamage': 0, 'MaxDamage': 0},
                        {'Name': '', 'MinDamage': 0, 'MaxDamage': 0}
                ],
    'Attacks_bandit': [{'Name': '', 'MinDamage': 0, 'MaxDamage': 0},
                        {'Name': '', 'MinDamage': 0, 'MaxDamage': 0}
                ]


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
            {'Type': 'Sword', 'Name': 'DefBlade', 'Amount': 500},  # Combining the Python function definition keyword def with "Blade", suggesting a sword that can define or alter reality itself, following the rules of its wielder, much like a function follows its defined parameters and actions.
            {'Type': 'Katana', 'Name': 'CyberShinobi', 'Health_Given': 30, 'Amount': 1},
            {'Type': 'Staff', 'Name': 'YieldScepter', 'Health_Given': 50, 'Amount': 1},
            {'Type': 'Dagger', 'Name': 'ByteBlade', 'Health_Given': 70}
        ]
    }
]

random_encounter = random.randint(0, 2)
equipped_pokemon = personal_pokemon[0]
#  When asking user if they want to bring out new poke-mon after previous one fainted user equipped choice
#  = personal_pokemon[*which ever index number corresponds to wanted poke-mon*] this should work new Pokémon into battle
#  func also
pokemon_one = wild_pokemon[random_encounter]
enemy_attack_randomizer = random.randint(0, len(pokemon_one['Attack']) - 1)

inventory = [items[0]['Weapon tier1'][0]]
locations = ["Cursed Library", "Fields of NullPointer", "Castle of SegFault"]

if player['level'] == 1:
    player['Attacks'][0]['MinDamage'] = 17
    player['Attacks'][0]['MaxDamage'] = 22
    player['Attacks'][1]['MinDamage'] = 10
    player['Attacks'][1]['MaxDamage'] = 12
elif player['level'] == 2:
    player['Attacks'][0]['MinDamage'] = 19
    player['Attacks'][0]['MaxDamage'] = 24
    player['Attacks'][1]['MinDamage'] = 12
    player['Attacks'][1]['MaxDamage'] = 14
elif player['level'] == 3:
    player['Attacks'][0]['MinDamage'] = 21
    player['Attacks'][0]['MaxDamage'] = 26
    player['Attacks'][1]['MinDamage'] = 14
    player['Attacks'][1]['MaxDamage'] = 16
elif player['level'] == 4:
    player['Attacks'][0]['MinDamage'] = 23
    player['Attacks'][0]['MaxDamage'] = 28
    player['Attacks'][1]['MinDamage'] = 16
    player['Attacks'][1]['MaxDamage'] = 18
elif player['level'] == 5:
    player['Attacks'][0]['MinDamage'] = 25
    player['Attacks'][0]['MaxDamage'] = 30
    player['Attacks'][1]['MinDamage'] = 18
    player['Attacks'][1]['MaxDamage'] = 20


print("")
player['name'] = input("First, what is your name? ")
print('Welcome {}, to Dark Pythons: Echoes of the Fallen Code.', player['name'])
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


def player_class():
    while True:
        print("Welcome, fragmented one. You have been chosen by the order in hopes you have what it takes to find and "
              "reset the core of creation!")
        player['class'] = input("The first step in your journey is picking your players class. Do you wish to be a "
                                "fierce knight, a humble samurai, a keen mage, or a sneaky bandit. ("
                                "knight/samurai/mage/bandit): ")
        if player['class'] == 'knight':
            player['damage'] = 20
            player['hp'] = 100
            inventory.append(items[0]['Weapon tier1'][0])
            all_locations(locations)
            print('A new knight has stepped foot into the world of Pythorean!')
            break
        elif player['class'] == 'samurai':
            player['damage'] = 10
            player['hp'] = 100
            inventory.append(items[0]['Weapon tier1'][1])
            all_locations(locations)
            print('A new samurai has stepped foot into the world of Pythorean!')
            break
        elif player['class'] == 'mage':
            player['damage'] = 10
            player['hp'] = 100
            inventory.append(items[0]['Weapon tier1'][2])
            all_locations(locations)
            print('A new mage has stepped foot into the world of Pythorean!')
            break
        elif player['class'] == 'bandit':
            player['damage'] = 10
            player['hp'] = 100
            inventory.append(items[0]['Weapon tier1'][3])
            all_locations(locations)
            print('A new bandit has stepped foot into the world of Pythorean!')
            break

    all_locations(locations)


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
    player_class()


def all_locations(locations):
    def Cursed_Library():
        print(
            f"\nYou awaken. Looking into the sky, the name Cursed Libray appears in bold writing. It's time to uncover "
            f"your destiny and perhaps, the fate of Pythoria itself.")
        locations.remove("Cursed Library")

    def Fields_of_NullPointer():
        print(
            f"\nYou awaken. Looking into the sky, the name Fields of NullPointer appears in bold writing. It's time "
            f"to uncover your destiny and perhaps, the fate of Pythoria itself.")

        locations.remove("Fields of NullPointer")

    def Castle_of_SegFault():
        print(
            f"\nYou awaken. Looking into the sky, the name Castle of SegFault appears in bold writing. It's time to "
            f"uncover your destiny and perhaps, the fate of Pythoria itself.")
        locations.remove("Castle of SegFault")

    chosen_location = random.choice(locations)
    if chosen_location == locations[0]:
        Cursed_Library()

    elif chosen_location == locations[1]:
        Fields_of_NullPointer()

    elif chosen_location == locations[2]:
        Castle_of_SegFault()


def game_mechanics():
    def battle():
        print("You encountered a wild", pokemon_one['Name'])
        print("It's a", pokemon_one['Type'], "Type!")
        print("It has", pokemon_one['Health'], "Health")
        print("It's a level", pokemon_one['Level'])

        while True:
            till_encounter = random.randint(1, 2)
            time.sleep(till_encounter)
            print('Begin Battle!')
            break

        while equipped_pokemon['Health'] > 0 and pokemon_one['Health'] > 0:
            user_input = input('Enter 1 to attack, 2 to throw a pokeball, 3 to flee the battle: ')

            if user_input == '1':
                attack_choice = random.choice(equipped_pokemon['Attacks'])
                Damage_own = generate_damage(attack_choice)
                print(equipped_pokemon['Name'], 'attacked the wild', pokemon_one['Name'], 'with', attack_choice['Name'])
                if equipped_pokemon['Type'] == "Fire" and pokemon_one['Type'] == "Grass":
                    pokemon_one['Health'] -= Damage_own * 1.5
                elif equipped_pokemon['Type'] == "Fire" and pokemon_one['Type'] == "Water":
                    pokemon_one['Health'] -= Damage_own * 0.5
                else:
                    pokemon_one['Health'] -= Damage_own
                print("The attack did", Damage_own, 'damage')

                if pokemon_one['Health'] <= 0:
                    break
                else:
                    print("The", pokemon_one['Name'], "has", pokemon_one['Health'], "health remaining")
                    till_encounter = random.randint(1, 2)
                    time.sleep(till_encounter)

                print("The wild", pokemon_one['Name'], 'attacked you back!')
                print(pokemon_one['Name'], 'used', pokemon_one['Attack'][enemy_attack_randomizer]['Name'])
                Damage_enemy = generate_damage(pokemon_one['Attack'][enemy_attack_randomizer])

                if equipped_pokemon['Type'] == "Fire" and pokemon_one['Type'] == "Grass":
                    equipped_pokemon['Health'] -= Damage_enemy * 1.5
                elif equipped_pokemon['Type'] == "Fire" and pokemon_one['Type'] == "Water":
                    equipped_pokemon['Health'] -= Damage_enemy * 0.5
                else:
                    equipped_pokemon['Health'] -= Damage_enemy
                print('The wild', pokemon_one['Name'], 'did', Damage_enemy, 'damage to', equipped_pokemon['Name'])
                print(equipped_pokemon['Name'], 'has', equipped_pokemon['Health'], 'health left')

            elif user_input == '2':
                catching()

            elif user_input == '3':
                print('You fled the battle!')
                break

        else:
            print("You can't do that")

        if equipped_pokemon['Health'] <= 0:
            print("All of your pokemon have fainted!")
            print("You rush to the nearest Poke-Centre")
            heal_all_pokemon(personal_pokemon)
        elif pokemon_one['Health'] <= 0:
            print("The wild", pokemon_one['Name'], "fainted!")
            if pokemon_one['Level'] == 3:
                equipped_pokemon['Level'] += 0.25
            elif pokemon_one['Level'] == 4:
                equipped_pokemon['Level'] += 0.5
            elif pokemon_one['Level'] == 5:
                equipped_pokemon['Level'] += 0.75
            elif pokemon_one['Level'] == 6:
                equipped_pokemon['Level'] += 1
        print("The battle ended.")
        if equipped_pokemon['Level'] > 5:
            print(f"Charmander leveled up to level {equipped_pokemon['Level']}!")

    def generate_damage(attack):
        return random.randint(attack['MinDamage'], attack['MaxDamage'])



if __name__ == "__main__":
    locked_room()
