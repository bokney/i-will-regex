
# what is the actual goal

# to pars a html file and get info from it
import re

pokemon_list = []
lines = []

with open("data/giant_bomb_original_150.html", mode='r') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    l = re.search(r"<h3>.+</h3>", l)

    if l:
        first_space = 0
        for c in l.group():
            first_space += 1
            if c == ' ':
                break

        pokemon_list.append(l.group()[first_space:-5])

for f in pokemon_list:
    print(f)
    
