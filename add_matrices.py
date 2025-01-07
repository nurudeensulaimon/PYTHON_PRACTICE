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
# The format of a list dictionary is that the list cannot be a 
# key, it can only be valkues 

# Use enumarate to store the index for each occurrence
for index, character in enumerate(characters):
	character_map[character].append(index)
print(character_map)

# NESTED LIST 
numbers = [1,0,15, [20,-10,15], 17, 0]
print(numbers[3][0])


# PROBLEM STATEMENT 
matrix1 = [[1,-2], [-3, 4]]
matrix2 = [[2, -1], [0,-1]]



def add(matrix1, matrix2):
	"""Add corresponding numbers in given 2-D matrices."""
	combined = []
	for i in range(len(matrix1)):
		row = []
		for j in range(len(matrix1[i])):
			row.append(matrix1[i][j] + matrix2[i][j])
		combined.append(row)
	return combined 

test = add(matrix1, matrix2)
print(test)


fruits = ["loquat", "jujube", "pear", "watermelon", "apple"]
colors = ["brown", "orange", "green", "pink", "purple"]

for fruit in fruits:
	for color in colors:
		print(color,fruit)

# Indexing with enumerate 

fruits = ["loquat", "jujube", "pear", "watermelon", "apple"]
colors = ["brown", "orange", "green", "pink", "purple"]

for n, fruit in enumerate(fruits):
	print(colors[n], fruit)


#Using the built-in zip function 

colors = ["brown", "orange", "green", "pink", "purple"]
fruits = ["loquat", "jujube", "pear", "watermelon", "apple"]
for item in zip(fruits, colors):
	print(item)



