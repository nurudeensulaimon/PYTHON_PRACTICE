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