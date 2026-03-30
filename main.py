import os
import json

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

    # Prints all pokemon from pokedex variable - 2 optional arguments allow for a range of pokemon
    @staticmethod
    def print_all_pokemon(start=1,stop=len(pokedex)):
        for index, pokemon in enumerate(pokedex[start - 1 : stop]):
            print(f"{pokemon["name"][language]} - #{pokemon["id"]}")

pokedex_retrieval_functions.print_all_pokemon()