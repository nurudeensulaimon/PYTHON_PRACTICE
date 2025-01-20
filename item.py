quantities = {"pink": 3, "green":4}


quantities["red"]=14

print(quantities)


# SET DEFAULT 

test1 = quantities.get("pink",0)
print(test1)


test2 = quantities.get("red", 0)

print(test2)

from dataclasses import dataclass 

@dataclass 

class Item:
	name: str 
	color: str 

items = [
Item("duck", "purple"),
Item("water bottle", "purple"),
Item("uni-duck", "pink"),
Item("sticky notes", "yellow"),
]



items_by_color = {}
for item in items:
	if item.color not in items_by_color:
		items_by_color[item.color]= []
	items_by_color[item.color].append(item.name)

print(items_by_color)


items_by_color = {}
for item in items:
	items_by_color.setdefault(item.color, []).append(item.name)

print(items_by_color)

 

 # Defining anagram


def anagram(string1, string2):
	string1 = string1.replace(" ", "").lower()
	string2 = string2.replace(" ", "").lower()
	return sorted(string1) == sorted(string2)

test1 = anagram("eat", "ate")
test2= anagram("listen", "silent")
test3= anagram("cafe", "nafe")
print(test1)
print(test2)
print(test3)


#Slicing a String Element 
message = "value exalt apprise esteem"
test=message[6:19:2]
print(test)

