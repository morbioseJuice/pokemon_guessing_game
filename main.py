import os
import json

language = "english"

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

class json_retrieval_functions:

    @staticmethod
    def get_pokemon_name(pokemon_number):
        for pokemon in pokedex:
            if pokemon["id"] == pokemon_number:
                found_pokemon = pokemon["name"][language]

                print(found_pokemon)
                return found_pokemon

    @staticmethod
    def get_pokemon_number(pokemon_name):
        for pokemon in pokedex:
            if pokemon["name"][language] == pokemon_name:
                found_number = pokemon["id"]

                print(found_number)
                return found_number

    @staticmethod
    def print_all_pokemon(start=1,stop=len(pokedex)):
        for index, pokemon in enumerate(pokedex[start - 1 : stop]):
            print(f"{pokemon["name"][language]} - #{pokemon["id"]}")

json_retrieval_functions.print_all_pokemon()