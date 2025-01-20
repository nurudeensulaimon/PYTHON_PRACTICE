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

print(items_by_color)


items_by_color = {}
for item in items:
	items_by_color.setdefault(item.color, []).append(item.name)

print(items_by_color)

 

 # Defining anagram


def anagram(string1, string2):
	string1 = string1.replace(" ", "").lower()
	string2 = string2.replace(" ", "").lower()
	return sorted(string1) == sorted(string2)

test1 = anagram("eat", "ate")
test2= anagram("listen", "silent")
test3= anagram("cafe", "nafe")
print(test1)
print(test2)
print(test3)


#Slicing a String Element 
message = "value exalt apprise esteem"
test=message[6:19:2]
print(test)

for n in range(2,5):
	print(n)

# A TAIL FUNCTION THAT RETURNS THE lAST ELEMENTS 

def tail(data,count):
	""" Returns the last 'elements of 'data'.
	Args:
	    data: A list or any iterable data type.
	    count. The number of elements to return from the end.

	    Returns 
	    The last 'count' elements if data is a list, or the last 'count'
	    character(s) if 'data' is a string. If count is 1, returns 
	    from the end. 

	Returns:
	    The last 'count' elements if 'data' is a list, or the last 'count'
	    character(s) if 'data' is  a string. If count is 1, returns 
	    a single element.

	    """

	try:
	 	# Ensure count is a postive integer
	 	if count <= 0:
	 		raise ValueError("Count must be a positive integer")
	 	# If the input is not iterable, convert it to a list or 
	 	# string representation
	 	if not isinstance(data,(list,str)):
	 		data = str(data)

	 	#Return the last 'count' elements 
	 	if isinstance(data, list) or isinstance(data, str):
	 		return data[-count:] if count > 1 else data[-1]
	 	else:
	 	    raise TypeError("Unsupported data type")
	except (TypeError, IndexError) as e:
		return f"Error: {e}"


print(tail([1,2,3,4,5],2))
print(tail("Hello, World!", 1))
print(tail(123456,3))
print(tail([1,2],5))
