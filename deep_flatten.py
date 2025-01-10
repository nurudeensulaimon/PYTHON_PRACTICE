groups = [["Hong", "Ryan"], ["Anthony","Wilhelmia"], ["Margaret", "Adrian"]]


expected_output = ["Hong", "Ryan", "Anthony", "Wilhelmina", "Margaret", "Andrian"]


names = []
for group in groups:
	for name in group:
	   names.append(name)
print(names)

# FLattening With Comprehension 

names = [
name 
for group in groups 
for name in groups
]

from itertools import chain 
chain(*groups)

list(chain(*groups))

numbers = [1,2,3,4,5]
print(isinstance(numbers,list))


try:
    x=int(input("Enter your favorite integer: "))

except ValueError:
	print("Uh oh,. That's not a number. Try again")
else:
	print(f"I like the number {x}")


