clue = ["Miss Scarlett", "Colonel Mustard", "Mrs. White", "Reverend Green", "Mrs Peacock", "Professor Plum", "Wadsworth", "Yvette"]
print(clue)
from random import *
shuffle(clue)
print(clue)
for name1 in clue:
    for name2 in clue:
        if name1 != name2:
            print(f"{name1} found out that {name2} was Mr Boddy's killer")
