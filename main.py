import random
import time
import os

#  time_sleep = time.sleep(2)
random.seed(os.urandom(1024))


def setup_player():
    player = {
        'name': introduction(),
        'hp': 0,  # Set by player_class function
        'stamina': 0,  # Set by player_class function
        'level': 1,  # All characters start at one
        'location': None,  # Will be set to current location of player
        'class': None,  # This will be set by the player_class function
        'Attacks knight': [{'Name': 'Slash', 'MinDamage': 5, 'MaxDamage': 10},
                           {'Name': 'Great swing', 'MinDamage': 5, 'MaxDamage': 10}],
        'Attacks samurai': [{'Name': 'bleed', 'MinDamage': 5, 'MaxDamage': 10},
                            {'Name': 'split', 'MinDamage': 5, 'MaxDamage': 10}],
        'Attacks mage': [{'Name': 'rock throw', 'MinDamage': 5, 'MaxDamage': 10},
                         {'Name': 'azure pebble', 'MinDamage': 5, 'MaxDamage': 10}],
        'Attacks bandit': [{'Name': 'Stab', 'MinDamage': 5, 'MaxDamage': 10},
                           {'Name': 'cut', 'MinDamage': 5, 'MaxDamage': 10}],
    }
    player = player_class(player)
    return player


def wait_for_input():
    controls_read = input()
    while controls_read == "":
        break
    return controls_read


enemies = [
    {'Name': 'Corrupted Code Fragment', 'HP': 50, 'Damage': 10},
    {'Name': 'Unsolvable Bug', 'HP': 50, 'Damage': 10},
]

wild_enemy = random.choice(enemies)

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


inventory = []
locations = ["Cursed Library", "Fields of NullPointer", "Castle of SegFault"]


def introduction():
    name = input("Enter the name of your hero: ")
    print("")
    print(f'Welcome {name}, to Dark Pythons: Echoes of the Fallen Code.')
    print('Controls: W,A,S,D to move directions, type in your preferred action when provided.')
    print("After every line of dialogue, the game will wait for the enter key's input to continue:")
    wait_for_input()
    print("Remember, this is a story game, so make sure you do everything you can for the full experience!")
    wait_for_input()
    print("In a world where reality is intertwined with the digital, an ancient curse has fallen over the land of "
          "Pythorean; \ncorrupting its code and trapping its inhabitants in an endless loop of death and despair. Legends "
          "tell of an emboldened hero who will traverse the treacherous \ndepths of the Cursed Library, the perilous "
          "fields of NullPointer, and the dreaded Castle of SegFault, to find and reset the Core of Creation, "
          "thus lifting the \ncurse and restoring balance to Pythoria:")
    wait_for_input()

    print('================================================================')

    return name


def print_player_info(player):
    print(f"\nPlayer Information:")
    print(f"Name: {player['name']}")
    print(f"Class: {player['class']}")
    print(f"HP: {player['hp']}")
    print(f"Stamina: {player['stamina']}")
    print(f"Level: {player['level']}")
    if player['type'] == "knight":
        print(f"Attack one: {player['Attacks knight'][0]}")
        print(f"Attack two: {player['Attacks knight'][1]}")
    elif player['type'] == "samurai":
        print(f"Attack one: {player['Attacks samurai'][0]}")
        print(f"Attack two: {player['Attacks samurai'][1]}")
    elif player['type'] == "mage":
        print(f"Attack one: {player['Attacks mage'][0]}")
        print(f"Attack two: {player['Attacks mage'][1]}")
    elif player['type'] == "bandit":
        print(f"Attack one: {player['Attacks bandit'][0]}")
        print(f"Attack two: {player['Attacks bandit'][1]}")
    all_locations(player)


def player_class(player):
    class_choices = {
        'knight': {'hp': 100, 'attacks': player['Attacks knight']},
        'samurai': {'hp': 100, 'attacks': player['Attacks samurai']},
        'mage': {'hp': 100, 'attacks': player['Attacks mage']},
        'bandit': {'hp': 100, 'attacks': player['Attacks bandit']},
    }
    while True:
        print("Welcome, fragmented one. You have been chosen by the order in hopes you have what it takes to find and "
              "reset the core of creation!")
        class_choice = input("The first step in your journey is picking your players class. Do you wish to be a "
                                "fierce knight, a humble samurai, a keen mage, or a sneaky bandit. ("
                                "knight/samurai/mage/bandit): ")
        if class_choice in class_choices:
            player.update({
                'class': class_choice,
                'hp': class_choices[class_choice]['hp'],
                'attacks': class_choices[class_choice]['attacks'],
            })
            # Depending on class choice, appends the appropriate starting weapon to the inventory
            inventory.append(items[0]['Weapon tier1'][['knight', 'samurai', 'mage', 'bandit'].index(class_choice)])
            locked_room(player)


def locked_room(player):
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
    all_locations(player)


def choose_attack(player):
    print("Choose your attack:")
    for i, attack in enumerate(player['attacks']):
        print(f"{i + 1}. {attack['Name']} (Damage: {attack['MinDamage']}-{attack['MaxDamage']})")
    choice = int(input()) - 1
    return player['attacks'][choice]


def game_reload(player):
    if player['hp'] <= 0:
        print("You died! Resetting game at the beginning of current level ")
        if player['location'] == 'Fields of NullPointer':
            Fields_of_NullPointer(player)
        elif player['location'] == 'Cursed Library':
            Cursed_Library(player)
        elif player['location'] == 'Castle of SegFault':
            Castle_of_SegFault(player)


def battle(player):
    print(f"While traversing {player['location']} you are attacked by an {wild_enemy['Name']}!")
    while player['hp'] > 0 and wild_enemy['HP'] > 0:
        player_action = input("Do you want to attack, run, or use an item? (attack/run/item): ").lower()
        if player_action == "attack":
            chosen_attack = choose_attack(player)
            damage = random.randint(chosen_attack['MinDamage'], chosen_attack['MaxDamage'])
            print(f"You use {chosen_attack['Name']} dealing {damage} damage.")
            wild_enemy['HP'] -= damage
            if wild_enemy['HP'] <= 0:
                print(f"You have defeated the {wild_enemy['Name']}!")
                wild_enemy['HP'] = 50  # Reset enemy HP for future battles
                return True  # Battle won
        elif player_action == "run":
            print("You successfully escape the battle.")
            return False  # Battle escaped
        elif player_action == "item":
            player_inventory()  # Assuming this function lets the player use an item
        else:
            print("Invalid action. Please choose again.")

        # Enemy's turn to attack if they're still alive
        if wild_enemy['HP'] > 0:
            print(f"The {wild_enemy['Name']} attacks you for {wild_enemy['Damage']} damage.")
            player['hp'] -= wild_enemy['Damage']
            if player['hp'] <= 0:
                print("You were defeated!")
                wild_enemy['HP'] = 50  # Reset enemy HP for future battles
                return False  # Battle lost

        print(f"Your HP: {player['hp']}, Enemy HP: {wild_enemy['HP']}")


def player_inventory():
    pass


def all_locations(player):
    chosen_location = input("A UI system with 3 options appears before you. It reads A - Fields of NullPointer, "
                            "B - Cursed Library, and C - Castle of SegFault. Which do you choose? ")
    if chosen_location == "A":
        Fields_of_NullPointer(player)
    elif chosen_location == "B":
        Cursed_Library(player)
    elif chosen_location == "C":
        Castle_of_SegFault(player)

    battle_result = battle(player)
    if battle_result:
        print("After your victory, you proceed on your adventure.")
    else:
        print("After escaping from the enemy, you proceed on your adventure.")


def Cursed_Library(player):
    player['location'] = "Cursed Library"
    print(
        f"\nYou awaken. Looking into the sky, the name Cursed Libray appears in bold writing. It's time to uncover "
        f"your destiny and perhaps, the fate of Pythoria itself.")


def Fields_of_NullPointer(player):
    player['location'] = "Fields of NullPointer"
    print(
        f"\nYou awaken. Looking into the sky, the name Fields of NullPointer appears in bold writing. It's time "
        f"to uncover your destiny and perhaps, the fate of Pythoria itself.")


def Castle_of_SegFault(player):
    player['location'] = "Castle of SegFault"
    print(
        f"\nYou awaken. Looking into the sky, the name Castle of SegFault appears in bold writing. It's time to "
        f"uncover your destiny and perhaps, the fate of Pythoria itself.")


def main():
    setup_player()


if __name__ == "__main__":
    main()

