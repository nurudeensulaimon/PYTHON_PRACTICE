#LOOPING WITH INDEXES 
n = 1
favorite_fruits = ["jujube", "pear", "watermelon", "apple"]
for fruit in favorite_fruits:
	print(n,fruit)
	n += 1 


favorite_fruits = ["jujube", "pear", "watermelon", "apple"]
for i in range(len(favorite_fruits)):
	print(i+1, favorite_fruits[i])


# Enumerate reurns both index and value 
for fruit in enumerate(favorite_fruits):
	print(fruit)


# LOOPING OVER MULTIPLE ITERABLES 

fruits = ["loquat", "jujube", "pear", "watermelon", "apple"]
colors = ["brown", "orange", "green", "pink", "purple"]

for fruit in fruits:
	print(fruit)


# Using Nested For Loops 

fruits = ["loquat", "jujube", "pear", "watermelon", "apple"]
colors = ["browns","oranges", "green", "pink", "purple"]
for fruit in fruits:
	for color in colors:
		print(color,fruit)


drinks = ["mocha", "java", "capuccinno", "tea", "soda"]

for n, drink in enumerate(drinks, start=1):
	print(n, drink)


# Store index positions of duplicate items 
characters = ["Krillin", "Goku", "Goku", "Gohan", "Piccolo",
              "Krillin", "Goku", "Vegeta", "Gohan", "Piccolo",
              "Piccolo", "Goku", "Vegeta", "Goku", "Piccolo"]

character_map = {character:[] for character in set(characters)}
print(character_map)


# Use enumarate to store the index for each occurrence
for index, character in enumerate(characters):
	character_map[character].append(index)
print(character_map)