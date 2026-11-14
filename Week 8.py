clue = ["Miss Scarlett", "Colonel Mustard", "Mrs. White", "Reverend Green", "Mrs Peacock", "Professor Plum", "Wadsworth", "Yvette"]
print(clue)
from random import *
shuffle(clue)
print(clue)
clue_alphabetical=sorted(clue)
for name1 in clue_alphabetical:
    for name2 in clue_alphabetical:
        if name1 != name2:
            print(f"{name1} and {name2}", ",")
            if name1 == "Yvette":
                if name2 == "Professor Plum":
                    break
print("Yvette and Reverend Green and")
print("Yvette and Wadsworth.")
