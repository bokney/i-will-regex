import re

def create_pokemon_list() -> list[str]:

    pokemon_list = []
    lines = []

    with open("data/giant_bomb_original_150.html", mode='r') as f:
        lines = f.readlines()

    for l in lines:
        m = re.search(r"<h3>.+</h3>", l)

        if m:
            first_space = 0
            for c in m.group():
                first_space += 1
                if c == ' ':
                    break

            pokemon_list.append(m.group()[first_space:-5])

    return pokemon_list
 
# print(create_pokemon_list())