# ACCEPTING ANY NUMBER OF ARGUMENTS 

def greet(name):
	print("Hello", name)

greet("Nero")


def greet(*names):
	for name in names:
		print("Hello",name)

greet("Nero", 'Dean')


# WRITE A FUNCTION THAT FINDS THE TOTAL LENGTH 


def total_length(*iterables):
	length = 0
	for iterable in iterables:
		length += len(iterable)
	return length 

#BONUS 1

def total_length(*iterables):
	length = 0
	for iterable in iterables:
		length += sum(1 for _ in iterable)
	return length 


total_length = ([4,5,],(6,7))


#total_length('hello', {'red': 50, 'purple': 100})
