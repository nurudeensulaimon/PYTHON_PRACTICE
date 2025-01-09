# ACCEPTING ANY NUMBER OF ARGUMENTS 

def greet(name):
	print("Hello", name)

greet("Nero")


def greet(*names):
	for name in names:
		print("Hello",name)

greet("Nero", "Dean")
