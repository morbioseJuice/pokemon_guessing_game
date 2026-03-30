import os
import json
import random

# Because the json has 4 languages, why not have the option to change it lol
language = "english"

# Reads data from json and creates python readable pokedex
path = os.path.join(os.path.dirname(__file__), 'pokedex_kanto.json')
with open(path, 'r', encoding='utf-8') as f:
    pokedex = json.load(f)

# A class as a container for general use functions
class utils:
    @staticmethod
    # Clears console - currently unused, but handy
    def clear_console():
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    # Just waits for an input, instead of typing input()
    def wait_for_enter():
        input("\nPress Enter to continue…")

    @staticmethod
    # Special input function to guarantee that a input can be int()ed
    def int_input(prompt, min=None, max=None):
        while True:
            try:
                value = int(input(prompt))

                if min is not None and value < min:
                    print(f"Value can't be lower than {min}")
                    continue

                elif max is not None and value > max:
                    print(f"Value can't be higher than {max}")
                    continue

                return value

            except ValueError:
                print("Invalid number.")

    def yes_no_input(prompt):
        while True:
            user_input = input(prompt)

            if user_input == "yes":
                return True
            elif user_input == "no":
                return False
            else:
                continue

# A class as a container for several functions that read data from the pokedex variable to spit out pokemon information
class pokedex_retrieval_functions:
    # Enter in a Pokemon #, and it spits out its name
    @staticmethod
    def get_pokemon_name(pokemon_number):
        for pokemon in pokedex:
            if pokemon["id"] == pokemon_number:
                found_pokemon = pokemon["name"][language]

                print(found_pokemon)
                return found_pokemon

    # Enter in a Pokemon name, and it spits out its #
    @staticmethod
    def get_pokemon_number(pokemon_name):
        for pokemon in pokedex:
            if pokemon["name"][language] == pokemon_name:
                found_number = pokemon["id"]

                print(found_number)
                return found_number

    @staticmethod
    def get_pokemon_types(pokemon_number):
        for pokemon in pokedex:
            if pokemon["id"] == pokemon_number:
                return pokemon["type"]

    # Prints all pokemon from pokedex variable - 5 optional arguments allow for a range of pokemon, and can decide whether to print names, types, or numbers
    @staticmethod
    def print_all_pokemon(start=1,stop=len(pokedex), q_print_types = True):
        for index, pokemon in enumerate(pokedex[start - 1 : stop]):
            if q_print_types == True:
                print(f"{pokemon["name"][language]} - {pokemon["id"]} --- {pokemon["type"]}")
            else:
                print(f"{pokemon["name"][language]} - {pokemon["id"]} ")

class questions:
    @staticmethod
    def guess_types_by_name(id):
        name = pokedex_retrieval_functions.get_pokemon_name(id)
        types = [p.lower() for p in pokedex_retrieval_functions.get_pokemon_types(id)]

        utils.clear_console()

        guess_types = [
            input(f"Guess {name}'s first type: ").lower(),
            input(f"Guess {name}'s second type (leave blank if it has none): ").lower(),
        ]

        try:
            guess_types.remove("")
        except ValueError:
            pass

        if sorted(types) == sorted(guess_types):
            return [True, types]
        else:
            return [False, types]

    @staticmethod
    def guess_number_by_name(id):
        name = pokedex_retrieval_functions.get_pokemon_name(id)

        utils.clear_console()

        guess_id = utils.int_input(f"Guess {name}'s Pokedex #: ")

        if id == guess_id:
            return [True, id]
        else:
            return [False, id]

while True:
    print("Pokemon Guessing Game by Will\n")
    print("Choose an option: ")
    print("1. Play")
    print("2. View Pokemon")
    print("3. Quit\n")
    opt = utils.int_input("? ", 1, 3)

    match opt:
        case 1:
            should_ask_num = utils.yes_no_input("Would you like to be quizzed on Pokedex #? (yes/no)")
            should_ask_types = utils.yes_no_input("Would you like to be quizzed on Pokemon Type? (yes/no)")

            while True:
                if should_ask_num:
                    return_val = questions.guess_number_by_name(random.randint(0, len(pokedex) - 1))

                    print(f"You got the answer right" if return_val[0] else "You got the answer wrong")
                    print(f"The correct answer was {return_val[1]}")

                if should_ask_types:
                    return_val = questions.guess_types_by_name(random.randint(0, len(pokedex) - 1))

                    print(f"You got the answer right" if return_val[0] else "You got the answer wrong")
                    print(f"The correct answer was {return_val[1]}")

                utils.wait_for_enter()

        case 2:
            pokedex_retrieval_functions.print_all_pokemon()
            utils.wait_for_enter()
        case 3:
            exit()