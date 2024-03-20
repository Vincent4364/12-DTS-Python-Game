import random
import time
import os
import sys

random.seed(os.urandom(1024))


def wait_for_input():
    controls_read = input()
    while controls_read == "":
        break

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

inventory = [items[0]['Weapon tier1'][0]]

locations = ["Cursed Library", "Fields of NullPointer", "Castle of SegFault"]

print("")
player_name = input("First, what is your name? ")
print(f'Welcome {player_name}, to Dark Pythons: Echoes of the Fallen Code.')
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
        player['class'] = input()
        if player['class'] == 'Knight':
            player['damage'] = 20
            player['hp'] = 100
            inventory.append(items[0]['Weapon tier1'][0])
            all_locations(locations)
            print('A new knight has stepped foot into the world of Pythorean!')
            break
        elif player['class'] == 'Samurai':
            player['damage'] = 10
            player['hp'] = 100
            inventory.append(items[0]['Weapon tier1'][1])
            all_locations(locations)
            print('A new samurai has stepped foot into the world of Pythorean!')
            break
        elif player['class'] == 'Mage':
            player['damage'] = 10
            player['hp'] = 100
            inventory.append(items[0]['Weapon tier1'][2])
            all_locations(locations)
            print('A new mage has stepped foot into the world of Pythorean!')
            break
        elif player['class'] == 'Bandit':
            player['damage'] = 10
            player['hp'] = 100
            inventory.append(items[0]['Weapon tier1'][3])
            all_locations(locations)
            print('A new bandit has stepped foot into the world of Pythorean!')
            break

    chosen_location = random.choice(locations)
    print(f"\nYou awaken. Looking into the sky, the name {locations} appears in bold writing. It's time to uncover "
          f"your destiny and perhaps, the fate of Pythoria itself.")


def locked_room():
    print('You wake up in a dimly lit room. The air is thick with dust and the scent of ancient parchment. You '
          'remember nothing of how you came to be here, only that the darkness outside this room calls to you, '
          'whispering of a curse and a core...:')
    wait_for_input()

    action = (input("\nDo you inspect the room for an exit, call out for help, or sit in despair? (inspect/call/sit): ")
              .lower())
    while True:
        if action == 'inspect':
            print("\nYour hands brush against the cold stone wall, feeling for a seam. Your fingers catch on a loose "
                  "stone and press it instinctively. A section of the wall grinds open, revealing a sliver of freedom.")
            break
        elif action == 'call':
            print("\nYour voice echoes through unseen halls, met only by silence. It seems you are alone in this "
                  "predicament.")
        elif action == 'sit':
            print("\nAs despair threatens to take hold, you remind yourself that succumbing to it will not change "
                  "your fate. It's time to act.")
        else:
            print("\nUnknown action. Your survival depends on making the right choices.")
    print("\nStepping through the secret passage, you find yourself on a path winding through an ethereal landscape, "
          "torn between realms.")
    print("Suddenly, the ground beneath you gives way, and you are consumed by swirling darkness...")
    player_class()


def all_locations(locations):
    if chosen_location == locations["Cursed Library"]:
        def cursed_library():
            print("\nYou find yourself in the Cursed Library")



if __name__ == "__main__":
    locked_room()
