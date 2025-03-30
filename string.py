
#STRING STORE TEXT 
message = "This is text"
print(message)

#HOW ARE STRINGS USED?

print("Hello and welcome to this program")

location = "https://pseudorandom.name"
if location.startswith("https://"):
	print("Let's handle *only* HTTPS URLS right now")


#with open("example.txt", mode="wt") as file:
#	file.write("This text will live in a file.")

#from urllib.request import urlopen
#with urlopen("https://pseudorandom.name") as response:
#	print(response.read().decode())

#STRING METHODS IN PYTHON
message = "This is text"
print(len(message))

print(message.upper())

print(message.count("T"))
print(message.replace("text", "a string"))

# Double Quotes vs Single Quotes 
message = "This is text"
message = 'This is text'


# ESCAPE CHARACTERS 
verse = 'I say "high", you say "low".\nYou say "why?" and I say "I don\'t know". \nOh no.'

print(verse)


# STRING CONCATENATE 

