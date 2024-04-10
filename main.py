import random
import time
import os

#  time_sleep = time.sleep(2)
random.seed(os.urandom(1024))


def setup_player():
    player = {  # dictionary that holds player information
        'name': introduction(),
        'hp': 0,  # Set by player_class function, players health
        'stamina': 0,  # Set by player_class function, players stamina
        'level': 1,  # All characters start at one, players level
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

    return player_class(player)


def wait_for_input():
    print('')
    controls_read = input("0 to restart game, any other key to continue: ")
    while controls_read == "":
        print('')
        break
    if controls_read == '0':
        main()
    return controls_read


enemies = [
    {'Name': 'Corrupted Guardian', 'HP': 35, 'Attack Name': 'Glitch Pulse', 'Damage': 5},
    {'Name': 'Code Fragment', 'HP': 50, 'Attack Name': 'Binary Barrage', 'Damage': 8},
    {'Name': 'Unsolvable Bug', 'HP': 50, 'Attack Name': 'Infinite Loop Lash', 'Damage': 10, },
]

boss_enemies = [
    {'Name': 'Architect of Desolation', 'HP': 100, 'Attack_Name': 'Eclipse of Ruin', 'Damage': random.randint(10,15)},
    {'Name': '', 'HP': 150, 'Attack_Name': 'pass', 'Damage': random.randint(15,20)},
    {'Name': '', 'HP': 200, 'Attack_Name': 'pass', 'Damage': random.randint(20,25)},
]

wild_enemy = random.choice(enemies)

items = [
    {
        'Weapon tier1': [
            {'Type': 'Sword', 'Name': 'SharpArray', 'Damage': 8},  # Starting weapon for Knight class
            {'Type': 'Katana', 'Name': 'CyberSlicer', 'Damage': 7},  # Starting weapon for Samurai class
            {'Type': 'Staff', 'Name': 'CodeCaster', 'Damage': 8},  # Starting weapon for Mage class
            {'Type': 'Dagger', 'Name': 'AsyncEdge', 'Damage': 6},  # Starting weapon for Bandit class
        ],
        'Weapon tier2': [
            {'Type': 'Sword', 'Name': 'RecurseRipper', 'Damage': 15},
            {'Type': 'Katana', 'Name': 'SliceIndexer', 'Damage': 14},
            {'Type': 'Staff', 'Name': 'GambitGenerator', 'Damage': 16},
            {'Type': 'Dagger', 'Name': 'FatalFloat', 'Damage': 13}
        ],
        'Weapon tier3': [
            {'Type': 'Sword', 'Name': 'DefBlade', 'Damage': 23},
            # Combining the Python function definition keyword def with "Blade", suggesting a sword that can define or alter reality itself, following the rules of its wielder, much like a function follows its defined parameters and actions.
            {'Type': 'Katana', 'Name': 'CyberShinobi', 'Damage': 21},
            {'Type': 'Staff', 'Name': 'YieldScepter', 'Damage': 22},
            {'Type': 'Dagger', 'Name': 'ByteBlade', 'Damage': 20}
            ],
        'Healing Items': [
            {'Type': 'Healing Item', 'Name': 'Potent Health Potion', 'Potency': 25}
            ]
    }
]


inventory = []
locations = ["Cursed Library", "Fields of NullPointer", "Castle of SegFault"]


def introduction():
    print('')
    name = input("Enter the name of your hero: ")
    print("")
    print(f'Welcome {name}, to Dark Pythons: Echoes of the Fallen Code.')
    print('Controls: W,A,S,D to move directions, type in your preferred action when provided.')
    print("After every line of dialogue, the game will wait for 0 to restart the game or any input to continue ")
    wait_for_input()
    print("Remember, this is a story game, so make sure you do everything you can for the full experience!")
    wait_for_input()
    print("In a world where reality is intertwined with the digital, an ancient curse has fallen over the land of "
          "Pythorean; corrupting its code and trapping its inhabitants in an endless loop of death and despair. Legends"
          "tell of an emboldened hero who will traverse the treacherous depths of the Cursed Library, the winding "
          "paths of the Archives of Legacy Code, and the dreaded Enchanted Forge of Debugging, to find and reset the "
          "Core of Creation, thus lifting the curse and restoring balance to Pythoria:")
    wait_for_input()

    print('================================================================')

    return name


def print_player_info(player):
    print(f"\nPlayer Information:")
    print(f"Name: {player['name']}")
    print(f"HP: {player['hp']}")
    print(f"Level: {player['level']}")
    if player['class'] == "knight":
        print(f"Attack one: {player['Attacks knight'][0]}")
        print(f"Attack two: {player['Attacks knight'][1]}")
    elif player['class'] == "samurai":
        print(f"Attack one: {player['Attacks samurai'][0]}")
        print(f"Attack two: {player['Attacks samurai'][1]}")
    elif player['class'] == "mage":
        print(f"Attack one: {player['Attacks mage'][0]}")
        print(f"Attack two: {player['Attacks mage'][1]}")
    elif player['class'] == "bandit":
        print(f"Attack one: {player['Attacks bandit'][0]}")
        print(f"Attack two: {player['Attacks bandit'][1]}")

    wait_for_input()
    locked_room(player)


def player_class(player):
    class_choices = {
        'knight': {'hp': 100, 'attacks': player['Attacks knight']},
        'samurai': {'hp': 100, 'attacks': player['Attacks samurai']},
        'mage': {'hp': 100, 'attacks': player['Attacks mage']},
        'bandit': {'hp': 100, 'attacks': player['Attacks bandit']},
    }
    print("Welcome, fragmented one. You have been chosen by the order in hopes you have what it takes to find and "
          "reset the core of creation!")
    wait_for_input()
    print("The first step in your journey is picking your players class, Do you wish to be a fierce knight, "
          "a humble samurai, a keen mage, or a sneaky bandit")
    while True:
        class_choice = input("(knight/samurai/mage/bandit): ").lower()
        if class_choice in class_choices:
            player.update({
                'class': class_choice,
                'hp': class_choices[class_choice]['hp'],
                'attacks': class_choices[class_choice]['attacks'],
            })
            # Depending on class choice, appends the appropriate starting weapon to the inventory
            inventory.append(items[0]['Weapon tier1'][['knight', 'samurai', 'mage', 'bandit'].index(class_choice)])
            print_player_info(player)
            break
        else:
            print("\nUnknown class. Your survival depends on making the right choices.")


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
            wait_for_input()
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

    print("\nStepping through the secret passage, you find yourself on a path winding through an ethereal landscape, "
          "torn between realms.")
    wait_for_input()
    print("Suddenly, the ground beneath you gives way, and you are consumed by swirling darkness...")
    wait_for_input()
    Cursed_Library(player)


def choose_attack(player):
    print("Choose your attack:")
    for i, attack in enumerate(player['attacks']):
        print(f"{i + 1}. {attack['Name']} (Damage: {attack['MinDamage']}-{attack['MaxDamage']})")
    choice = int(input()) - 1
    return choice


def game_reload(player):
    # Assuming the respective location functions are defined elsewhere in your code.
    if player['hp'] <= 0:
        print("You died! Resetting game at the beginning of current level ")
        if player['location'] == 'Enchanted Forge of Debugging':
            Enchanted_Forge_of_Debugging(player)
        elif player['location'] == 'Cursed Library':
            Cursed_Library(player)
        elif player['location'] == 'Castle of SegFault':
            Archives_of_Legacy_Code(player)


def attack_system(player):
    player_action = input("Do you want to attack, run, or use an item? (attack/run/item): ").lower()
    if player_action == 'attack':
        chosen_attack_index = choose_attack(player)
        chosen_attack = player['attacks'][chosen_attack_index]
        damage = random.randint(chosen_attack['MinDamage'], chosen_attack['MaxDamage'])
        return damage, chosen_attack['Name'], player_action
    else:
        return player_action


def battle(player):
    action_result = attack_system(player)
    if isinstance(action_result, tuple):  # checks if action_result is an instance of a tuple
        damage, chosen_attack_name, _ = action_result  # unpacks the values from the action result tuple into three
        # separate variables ( _ is used as a placeholder for the third variable which is not needed for the function)
    if action_result == 'attack':
        print(f"You use {action_result[1]} dealing {action_result[0]} damage.")
        enemies[0]['HP'] -= action_result[0]
        if enemies[0]['HP'] <= 0:
            print(f"You have defeated the {enemies[0]['Name']}!")
            enemies[0]['HP'] = 35  # Reset enemy HP for future battles
            return True
    elif action_result == 'run':
        print(f"You attempt to away from the {enemies[0]['Name']}.")
        success_rate = random.randint(0,10)
        if success_rate == range(1,3):
            print(f"You manage to escape the {enemies[0]['Name']}.")
            enemies[0]['HP'] = 35  # Reset enemy HP for future battles
            return True
        else:
            print(f"You are unable to escape the {enemies[0]['Name']}.")
            print("The enemy uses this chance to attack you!")
            return False
    elif action_result == "item":
        player_inventory(player)
        pass
    else:
        print("Invalid action. Please choose again.")

    # Enemy's turn to attack
    if wild_enemy['HP'] > 0:
        print(f"The {wild_enemy['Name']} attacks you for {wild_enemy['Damage']} damage.")
        player['hp'] -= wild_enemy['Damage']
        if player['hp'] <= 0:
            print("You were defeated!")
            game_reload(player)
            return False

    print(f"Your HP: {player['hp']}, Enemy HP: {wild_enemy['HP']}")
    return None  # The battle continues


def cursed_library_puzzle(player):
    print("\nThe Ethereal Librarian presents you with a final challenge: 'To find the Tome of Reset, you must first "
          "solve this riddle: I speak without a mouth and hear without ears. I have no body, but I come alive with "
          "wind. What am I?'")
    print("\n1. The Whispering Tome")
    print("2. The Echoing Chasm")
    print("3. The Silent Watcher")
    print("4. The Boundless Echo")
    answer = input("Choose the correct book (Enter 1, 2, 3, or 4): ")

    if answer == "4":
        print("\nCorrect! The Boundless Echo holds the key to breaking the curse. As you speak the title, the book "
              "glows with a soft light, guiding you to the Tome of Reset.")
        return True
    else:
        print("\nIncorrect. The library's curse grows stronger, repelling you with a forceful energy. You must "
              "prepare to try again.")
        return False


def archives_of_legacy_code_puzzle():
    print("\nTo access the deepest secrets of the Archives, you must reconstruct the Ancient Code. Arrange the "
          "following code snippets in the correct order.")

    correct_order = 'DBCA'
    print("\nA. Code.execute()")
    print("B. Code.compile()")
    print("C. Code.debug()")
    print("D. Code.write()")
    order = input("Enter the letters in the correct order (e.g., ABCD): ").upper()

    if order == correct_order:
        print("\nYou've successfully reconstructed the Ancient Code. The archive's secrets unveil themselves, "
              "guiding you towards the truth of Pythoria's corruption.")
        return True
    else:
        print("\nThe code fragments reject your arrangement. You must clear your "
              "mind and attempt the puzzle once more.")
        return False


def boss_enemy_info(player):
    while player['location'] == 'Cursed Library':
        boss_enemy = boss_enemies[0]
        rounds = 1
        boss_name = boss_enemy['Name']
        boss_initial_hp = boss_enemy['HP']
        print(f"The battle against {boss_enemy['Name']} begins!")
        return rounds, boss_name, boss_initial_hp, boss_enemy

    while player['location'] == "Fields of NullPointer":
        boss_enemy = boss_enemies[1]
        rounds = 2
        boss_name = boss_enemy['Name']
        boss_initial_hp = boss_enemy['HP']
        print(f"The battle against {boss_enemy['Name']} begins!")
        return rounds, boss_name, boss_initial_hp, boss_enemy

    while player['location'] == "Castle of SegFault":
        boss_enemy = boss_enemies[2]
        rounds = 3
        boss_name = boss_enemy['Name']
        boss_initial_hp = boss_enemy['HP']
        boss_attack = boss_enemy['Attack']
        boss_attack_name = boss_enemy['Attack_Name']
        print(f"The battle against {boss_enemy['Name']} begins!")
        return rounds, boss_name, boss_initial_hp, boss_enemy, boss_attack, boss_attack_name


def boss_enemy_battle(player):
    boss_enemy_info(player)
    rounds, boss_initial_hp, boss_name, boss_enemy, boss_attack, boss_attack_name = boss_enemy_info(player)
    chosen_attack, damage = attack_system(player)
    while player['HP'] > 0 and boss_initial_hp > 0:
        print(f"\n--- Round {rounds} ---")
        attack_system(player)
        chosen_attack = attack_system(chosen_attack)
        damage = attack_system(damage)
        print(f"You deal {damage} damage to {boss_name}.")
        boss_enemy['HP'] -= damage
        if boss_enemy['HP'] > 0:
            player['HP'] -= boss_attack
            print(f"{boss_name} attacks you with {boss_attack_name} dealing {boss_attack} damage!")

        # Boss healing mechanic, activates once per battle, when below 50% HP for the first time.
        if boss_enemy['HP'] < boss_initial_hp / 2 and 'healed' not in boss_enemy:
            heal_amount = random.randint(20, 40)
            boss_enemy['HP'] += heal_amount
            boss_enemy['healed'] = True  # Ensure the boss can only heal once per battle.
            print(f"{boss_enemy['Name']} codes the power to heal themselves, restoring {heal_amount} HP!")

        if player['HP'] <= 0:
            print("You have been defeated. The world dims as the Architect's laughter echoes through the library.")
            return False

        if boss_enemy['HP'] <= 0:
            print(
                f"{boss_enemy['Name']} has been defeated! Peace returns to the library as the corrupted code dissolves into nothingness.")
            return True

        # Check if it's time to move to the next round or end the battle.
        if rounds == 2:
            print("The battle intensifies as you both prepare for the final clash.")
        elif rounds > 2:
            break  # Just in case, prevents infinite loop if something goes wrong.

        rounds += 1
        wait_for_input()  # Assuming this is to pause the game, waiting for the player to press a key.

    # In case the battle somehow continues beyond two rounds, this ensures an outcome.
    if player['HP'] > 0:
        print(
            "In a last, desperate effort, you finally overcome the Architect of Desolation. The library is safe, for now.")
        return True
    else:
        print(
            "Exhausted and beaten, you fall to the Architect of Desolation. This is not the end, however; you will return.")
        return False


def player_inventory(player):
    user_input = input("(potions/weapons)")
    if user_input == "potions":
        user_choice = input("Which potion will you use?")
        print("You use a potion to heal yourself for 20 HP.")
        player['hp'] += 20
    elif user_input == "weapons":
        print("You use a weapon to heal yourself for 20 HP.")
        player['hp'] += 20


def Cursed_Library(player):
    player['location'] = "Cursed Library"
    print("Confused and distraught, you stumble to your feet.")
    wait_for_input()
    print('Your met error filled IDE which prints the simple message, "Welcome to the Cursed Library"')
    wait_for_input()
    print("\nWalking past the IDE, you find yourself before two archaic, towering doors. You step through, and the scent of ancient knowledge and forgotten tales fills your nostrils. Shelves upon shelves of glowing tomes line the endless halls, each tome another player, lost within the librarys halls, for all eternity.")
    wait_for_input()

    print("\nYou're approached by an ethereal librarian, a ghostly figure bound to serve the library for eternity. 'Welcome, traveler,' the librarian rasps. 'Beware the corrupted knowledge and the guardians that protect it. Seek out the Archives of Legacy Code to break the curse. But first, prove your worth.'")
    wait_for_input()

    print("\nTwo corrupted guardians approach, their forms flickering between reality and code. It's time to battle.")
    wait_for_input()
    battle(player)

    if not battle(player):
        game_reload(player)
        return

    print("With the first enemy defeated, the second charges at you in a state of rage")
    battle(player)

    if not battle(player):
        game_reload(player)
        return

    print("\nWith the guardians defeated, the librarian nods in approval. 'You possess strength and resolve. The Tome "
          "of Reset lies beyond the Great Hall, guarded by the Architect of Desolation. Prepare yourself.'")
    wait_for_input()

    # Introducing a New NPC: The Lost Coder
    print("\nVenturing deeper, you encounter a Lost Coder, trapped in the library's curse. 'I can offer you "
          "assistance,' the coder says, handing you a potent healing code fragment.")
    items[0]['Healing Items'][0]['Amount'] += 1
    print("'Use it wisely, for the Master of Bugs is no ordinary foe.'")
    wait_for_input()

    # Approaching the Boss Battle
    print("\nThe Great Hall looms before you, vast and filled with the hum of corrupted data. At its center, the Architect of Desolation, a colossal entity of code and malice, guards the Tome of Reset.")
    wait_for_input()
    print("'Foolish traveler,' it booms. 'You dare challenge my dominion? Come then, and fall like those before you.'")
    boss_enemy_battle(player)

    # Boss Battle
    if not boss_enemy_battle(player):
        game_reload(player)
        return

    print("As the architect of desolation begins to crumble, you turn around, expecting to be granted passage, but the librarains aura implys otherwise.")
    wait_for_input()
    print('"The librarian mumbles, "you have one final challenge".')
    archives_of_legacy_code_puzzle()

    if not archives_of_legacy_code_puzzle():
        game_reload(player)
        return

    # Resetting the player's location or directing them to the next part of the adventure
    Archives_of_Legacy_Code(player)


def Archives_of_Legacy_Code(player):
    player['location'] = "Archives of Legacy Code"
    print("\nLeaving the Cursed Library behind, you follow a trail of glitched reality, leading to the Archives of "
          "Legacy Code. This ancient repository houses the source codes of Pythoria, including scripts so old and "
          "powerful that few dare to examine them.")
    wait_for_input()

    print("\nAs you navigate through towering stacks of parchments and scrolls, the air crackles with static energy. "
          "Suddenly, an avatar of the Archive's guardian materializes before you. 'Welcome, seeker of truths,' it "
          "intones. 'Here lies the foundation of all that Pythoria was, is, and will be. But be warned, some "
          "truths might just rewrite you.'")
    wait_for_input()

    archives_of_legacy_code_puzzle()

    if not archives_of_legacy_code_puzzle():
        game_reload(player)
        return

    print("Deciphering the Ancient Code reveals a hidden history of Pythoria, written by the first codemancers who "
          "sought to blend magic and technology. You learn of the Original Bug, a flaw so severe that it "
          "threatened to unravel the fabric of reality.")
    wait_for_input()

    # Boss Battle: Archivist of Corruption
    print("\nAs you delve deeper into the Archives, you encounter the Archivist of Corruption, a twisted amalgamation "
          "of corrupted code and malevolent energy. It guards the darkest secrets of Pythoria's past.")
    wait_for_input()
    print("The Archivist's eyes flare with dark power as it prepares to strike. It's time to battle!")
    battle(player)

    # Boss Battle Outcome
    if not battle(player):
        game_reload(player)
        return

    print("\nThe Archivist of Corruption falls, its essence dispersing like digital smoke. With its defeat, the way "
          "forward clears, and you can continue your quest for truth.")
    wait_for_input()

    # Introducing the Concept of the Debugging Forge
    print("\nAmong the texts, you find a reference to the Enchanted Forge of Debugging, created by the ancients as a "
          "means to combat the Original Bug. It speaks of a powerful artifact, the Ultimate Debugging Tool, "
          "capable of purging the deepest corruptions.")
    wait_for_input()

    print("'To seek the forge is to seek the salvation of Pythoria,' the guardian's voice echoes in your mind as "
          "you prepare to leave the Archives. 'But be forewarned, the path is perilous and the forge's protector, "
          "the Fragmented Sentinel, allows no one to wield its power unchecked.'")
    wait_for_input()

    print("\nWith newfound knowledge and determination, you step out of the Archives of Legacy Code. Ahead lies the "
          "journey to the Enchanted Forge of Debugging, where the fate of Pythoria awaits to be rewritten.")
    wait_for_input()

    # Resetting the player's location or directing them to the next part of the adventure
    Enchanted_Forge_of_Debugging(player)


def Enchanted_Forge_of_Debugging(player):
    player['location'] = "Enchanted Forge of Debugging"
    print("\nPushing open the heavy, steel doors of the Enchanted Forge of Debugging, you're greeted by the heat of "
          "flames and the clang of hammer on anvil. This forge crafts not just weapons, but also spells and codes "
          "to debug reality itself. Each artifact here holds the power to alter the fabric of Pythoria.")
    wait_for_input()

    print("\nA figure emerges from the shadows, their eyes glowing with a coder's fire. 'Ah, a brave soul has "
          "arrived,' they announce, their voice echoing through the vast chamber. 'I am the Forge Master, keeper "
          "of this place. If you seek to wield the power of debugging, you must first demonstrate your capability "
          "by repairing the Corrupted Golem.'")
    wait_for_input()
    print("To aid you in your task, I shall bestow upon you a potent healing fragment")
    items[0]['Healing Items'][0]['Amount'] += 1
    wait_for_input()

    print("\nWith a wave of the Forge Master's hand, the Corrupted Golem lumbers toward you, its code visibly glitching "
          "with malice. This is your first challenge.")
    battle(player)

    if not battle(player):
        game_reload(player)
        return

    print("The Golem crumbles to the ground, its corrupted code purged. The Forge Master nods in approval, 'Well done. "
          "But greater challenges await.'")
    wait_for_input()

    # Introducing a New NPC: The Apprentice Debugger
    print("\nAs you delve deeper into the forge, you encounter an Apprentice Debugger, eager but overwhelmed. 'I "
          "discovered a potent Debugging potion, but it's too much for me to handle,' they say, offering it to you.")
    items[0]['Healing Items'][0]['Amount'] += 1
    print("'Use this in your forthcoming battle. The Fragmented Sentinel, guardian of the forge, will not fall easily.'")
    wait_for_input()

    # Approaching the Boss Battle
    print("\nThe heart of the forge pulses with a powerful energy, where the Fragmented Sentinel awaits, a behemoth "
          "pieced together from countless lines of code and magical essence.")
    wait_for_input()
    print("'Foolhardy debugger,' it bellows. 'Your efforts to cleanse this place of its necessary chaos are futile. "
          "Prepare to be deleted.'")
    boss_enemy_battle(player)

    # Boss Battle
    if not boss_enemy_battle(player):
        game_reload(player)
        return

    print("\nAs the Sentinel dissolves, its fragments scattering like lost data, the core of the forge reveals the "
          "Ultimate Debugging Tool. You grasp it, and a wave of clarity washes over the forge.")
    wait_for_input()

    print("\nCalmness envelops the forge as its corrupted elements are debugged and order is restored. The Forge "
          "Master approaches, offering a smile. 'You have done what many believed impossible. The Enchanted Forge "
          "of Debugging shall now create tools for the betterment of Pythoria.'")
    print("\nThe forge's doors open to the world outside, promising new adventures. Yet, the tale of Pythoria is "
          "far from over...")
    wait_for_input()

    # Resetting the player's location or directing them to the next part of the adventure


def main():
    setup_player()


if __name__ == "__main__":
    main()

