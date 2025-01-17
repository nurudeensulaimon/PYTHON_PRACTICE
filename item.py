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

items_by_color 
