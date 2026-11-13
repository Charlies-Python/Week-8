for c in range(0,10):
    print(c)
print()
for c in range(0,11):
    print(c)
print()
for c in range(0,100,3):
    print(c)
print()
for c in range(10,0,-1):
    print(c)
print()
characters = ["The Cat", "The Fish", "Thing 1", "Thing 2", "Sally", "Sally's brother"]
for name in characters:
    print(name)
print()
for i in range(0,len(characters)):
    print(f"character {i} is {characters[i]}")
print()
for i in [1,6,17,23,32,45,46,49,120,1234567890]:
    if i % 2 == 0:
        print(i)
print()
for i in range(0,10):
    for j in range(0,10):
        print(f"This is i={i} and j={j}")
print()
for name1 in characters:
    for name2 in characters:
        if name1 != name2:
            print(f"{name1} shakes hands with {name2}")
print()
for i in range(1,11):
    thisline = ""
    for j in range(1,11):
        thisline = f"{thisline}{i*j}\t"
    print(thisline)
print()
lines = [[4,9,2],[3,5,7],[8,1,6]]
for i in range(0,len(lines)):
    output = f"Row {i+1}:"
    for item in lines[i]:
        output = f"{output} {item}"
    print(output)
print()
i = 1
while i**2 < 100:
  print(f"{i} squared is {i**2}")
  i += 1
print()
franchises = ["Star Wars", "Alien", "Harry Potter", "Star Trek", "Marvel Cinematic Universe",\
"Batman", "X Men", "James Bond", "The Lord of the Rings", "Jurassic Park", "DC Extended Universe",\
"The Fast and the Furious", "Transformers", "Pirates of the Caribbean", "The Hunger Games",\
"Twilight", "Mission: Impossible", "Indiana Jones"]

non_t_franchises = []

while franchises:
    if franchises[0][0].lower() == "t":
        del franchises[0]
    else:
        non_t_franchises.append(franchises.pop(0))

print(f"The franchises that don't start with 'T' are: {non_t_franchises}")
print()
import random
balls = ["yellow","blue","red","purple","orange","green","brown","black"]
potted = []
random.shuffle(balls)
while balls:
    thisball = balls.pop()
    potted.append(thisball)
    if thisball == "black":
        break
print(f"Balls potted: {potted}")
print()
i=0
while True:
    i=i+1
    if i**2 > 99:
        break
    print(f"{i} squared is {i**2}")
print()
i = 0
while i < 21:
    i = i + 1
    if i % 5 == 0:
        continue
    print(i)
