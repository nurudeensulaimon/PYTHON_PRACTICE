def tail(sequence,n):
	"""Return the last n items of given sequence."""
	return sequence[-n:]


print(tail([1,2,3,4,5],2))


def tail(sequence, n):
	"""Return the last n items of given sequence."""
	return list(sequence[-n:])

def tail(sequence, n):
	"""Return the last n items of given sequence."""
	if n == 0:
		return []
	return list(sequence[-n:])


# BONUS 1 
def tail(sequence, n):
 	"""Return the last n items of given sequence."""
 	if n <= 0:
 		return []
 	return list(sequence[-n:])


ssh-keygen -t ed25519 -C "nurudeen.a.sulaimon@gmail.com"




# BONUS 2

def tail(iterable, n):
	"""Return the last n items of given iterable."""
	sequence = list(iterable)
	if n <= 0:
		return []
	return sequence[-n]


def anagram(word1, word2):
	if word1 == reversed(word2):
		return True 
	else:
		return False


test=anagram("tea", "eat")
print(test)


