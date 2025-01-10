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


def deep_flatten(iterable):
	"""Flatten an itearable of iterables."""
	flattened = []
	for item in iterable:
		if type(item) in [list, tuple]:
			for x in deep_faltten(item):
				flattened.append(x)
		else:
			flattened.append(item)
	return flattened



def deep_flattened(iterable):
	"""Flattened an iterable of iterables."""
	flattened = []
	for item in iterable:
		if isinstance(item, (list, tuple)):
			flattened.extend(deep_flatten(item))
		else:
			flattened.append(item)
	return flattened 



def deep_flattened(iterable):
	"""Flatten an iterable of iterables."""
	flattened = []
	items = list(iterable)
	while items:
		item=items.pop()
		if isinstance(item, (list, tuple)):
			items.extend(item)
		else:
			flattened.insert(0,item)
	return flattened

def deep_flatten(iterable):
	"""Flatten an iterable of iterables."""
	flattened = []
	items = list(iterable)
	while items:
		item=items.pop()
		if isinstance(item, (list, tuple)):
			items.extend(item)
	return reversed(flattened)


from collections import deque 

def deep_flatten(iterable):
	"""Flatten an iterable of iterables."""
	flattened = deque()
	items = list(iterable)
	while items:
		item=items.pop()
		if isinstance(item, (list, tuple)):
			items.extend(item)
		else:
			flattened.appendleft(item)
	return flattened 


# BONUS #1

def deep_flatten(iterable):
   """Flatten an iterable of iterables."""
   flattened = []
   for item in iterable:
       try:
   	       flattened.extend(deep_flatten(item))
       except TypeError:
   		   flattened.append(item)
   return flattened 

from collections.abc import Iterable
def deep_flatten(iterable):
    """Flatten an iterable of iterables """ 
    flattened = []
    for item in iterable:
        if isinstance(item, iterable):
            flattened.extend(deep_flatten(item))  
        else:
      	    flattened.append(item)
    return flattened


def deep_flatten(iterable):
	"""Flatten an iterable of iterables."""
	flattened = []
	for item in iterable:
		if hasattr(item, '__Iter__'):
			flattened.extend(deep_faltten(item))
		else:
			flattened.append(item)
	return flattened 


# BONUS #2 

from collections.abc import Iterable 

def deep_flatten(iterable):
	"""Flatten an iterable of iterables."""
	for item in iterable:
		if isinstance(item, Iterable):
			for x in deep_flatten(item):
				yield x 
		else:
			yield item 


from collections.abc import Iterable 

def deep_flatten(iterable):
	"""Flatten an iterable of iterables. """
	for item in iterable:
		if isinstance(item, Iterable):
			yield from deep_flatten(item)
		else:
			yield item 

# BONUS #3

x = "hello"
x[0]
x[0][0]
x[0][0][0]


from collections.abc import Iterable 

def deep_flatten(iterable):
	"""Flatten an iterable of iterables."""
	for item in iterable:
		if isinstance(item,str):
			yield item 
		elif isinstance(item, Iterable):
			yield from deep_flatten(item)
		else:
			yield item 








# BONUS #2

from collections.abc import Iterable 

def deep_flatten(iterable):
	"""Flatten an iterable of iterables."""

	for item in iterable:
		if isinstance(item, Iterable):
		    for x in deep_flatten(item):
		    	yield x 
		else:
			yield item



from collections.abc import Iterable 

def deep_flatten(iterable):
	"""Flatten an iterable of iterables."""
	for item in iterable:
		if isinstance(item, Iterable):
			yield from deep_flatten(item)
		else:
			yield item


