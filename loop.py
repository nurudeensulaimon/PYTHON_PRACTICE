#LOOPING IN PYTHON 
colors = ["red", "green", "blue", "purple"]
i = 0
while i < len (colors):
	print(colors[i])
	i += 1


# Range of Length 
colors = ["red", "green", "blue", "purple"]
for i in range(len(colors)):
	print(colors[i])


# For-in : the usual way 
colors = ["red", "green", "blue","purple"]
for color in colors:
	print(color)


cars = ["Mazda", "Tesla", "Benz", "Toyota", "Honda"]
for car in cars:
	print(car)

presidents = ["Washington", "Adams", "Jefferson", "Madison", "Monroe"]
for i in range(len(presidents)):
	print("President {}: {}".format(i+ 1, presidents[i]))


# enumerate: does the same thing as above code 

presidents = ["Washington", "Adams", "Jefferson", "Madison", "Monroe"]
for num, name in enumerate(presidents, start=1):
	print("President {}: {}".format(num, name))

	# Using Enumerate to loop over two lists 
sectors = ["Retail", "Computing","Logistics", "Finance", "Entertainment"]
potentials = [0.2,0.3, 0.1, 0.4,0.5]
for i, sector in enumerate(sectors):
	potential = potentials[i]
	print("{}% {}".format(potential * 100, sector))
