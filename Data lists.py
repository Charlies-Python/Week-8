subjects = ["maths", "physics", "engineering", "chemistry", "biology"]
print(subjects)
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
print(months[3])
print(months[-1])
print(months[-3])
from random import *
choice(months)
numbers = [1,2,3,4,5,6]
print(numbers)
shuffle(numbers)
print(numbers)
a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(a[0:2])
print(a[1:4])
print(a[-3:])
print(a[2:])
print(a[:7])
print(a[:10:2])
print(a[4:14:3])
print(a[::-1])
ingredients = ["courgette","mushroom","aubergine","tomato","herbs","chilli"]
print(ingredients)
ingredients[2] = "peppers"
print(ingredients)
mos_eisley = ["Luke","Ben","C3PO","R2D2"]
print(mos_eisley)
mos_eisley.append("Han")
mos_eisley.append("Chewie")
print(mos_eisley)
engines = ["Thomas","Edward","Henry","Gordon","James","Percy","Toby","Duck","Donald","Douglas"]
print(engines)
del engines[1]
print(engines)
del engines[2:4]
print(engines)
del engines[-3:]
print(engines)
staff=["Peter","Alex","Angharad","Alex","Lylah","Alex"]
print(staff)
staff.remove("Alex")
print(staff)
staff.remove("Alex")
print(staff)
a = [1,2,3,4,5,6,7,8,9,10]
print(a)
removed1 = a.pop(1)
removed2 = a.pop(4)
removed3 = a.pop(-3)
print(f"The sum of the removed values is {removed1+removed2+removed3}")
print(a)
original_order = ["England", "Scotland", "Wales", "Northern Ireland"]
alphabetical_order = sorted(original_order)
print(original_order)
print(alphabetical_order)
original_order = ["England", "Scotland", "Wales", "Northern Ireland"]
original_order.sort()
print(original_order)
names = ("Monica", "Chandler", "Ross", "Rachel", "Joey", "Phoebe")
reverse_alphabetical = sorted(names, reverse=True)
print(reverse_alphabetical)
letters = ["A","a","C","B","c","b"]
print(sorted(letters))
print(sorted(letters, key=str.lower))
numbers = ["0", "1", "3.14157", "2.71828", "1.41421", "10", "121", "1024"]
print(sorted(numbers))
print(sorted(numbers, key=float))
dates = ["1985-10-25", "1955-11-05", "1955-11-12", "1985-10-26", "2015-10-21", "1955-11-16", "1885-09-02", "1885-09-07", "1985-10-27"]
print(sorted(dates))
flavours = ["up","down","strange","charm","bottom","top"]
print(len(flavours))
avengers = []
avengers.append(["Tony Stark", "Iron Man", ["Genius", "Billionare", "Armored suit"]])
avengers.append(["Steve Rogers", "Captain America", ["Super strength", "Accelerated healing", "Vibranium shield"]])
avengers.append(["Bruce Banner","Hulk",["Genius", "Invulnerability", "Super strength"]])
avengers.append(["Thor", "Thor", ["Super strength", "Mjölnir", "Electric/weather manipulation"]])
avengers.append(["Natasha Romanoff", "Black Widow", ["Super spy"]])
avengers.append(["Clint Barton", "Hawkeye", ["Master archer"]])
print("all Avengers, a list:")
print(avengers)
print("one of the Avengers, also a list:")
print(avengers[4])
print("the powers of one of the Avengers, also a list:")
print(avengers[3][2])
