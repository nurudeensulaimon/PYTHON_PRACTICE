def deep_add(list_or_number):
	"""Return sum of values in given list, iteraing deeply."""
	total 


def add(*matrices):
	combined = []
	for rows in zip(*matrices):
		row = []
		for values in zip(*rows):
			total = 0
			for n in values:
				total += n 
			row.append(total)
		combined.append(row)
	return combined 

matrix1 = [[1,9], [7,3]]
matrix2 = [[5,-4], [3,3]]
matrix3 = [[2,3], [-3,1]]

test=add(matrix1, matrix2, matrix3)
print(test)


def add(matrix1, matrix2):
	"""Add corresponding numbers in given 2-D matrices."""
	combined = []
	for i in range(len(matrix1)):
		row = []
		for j in range(len(matrix1[i])):
			row.append(matrix1[i][j] + matrix2[i][j])
		combined.append(row)
	return combined 

matrix1 = [[1,9], [7,3]]
matrix2 = [[5,-4], [3,3]]

test=add(matrix1, matrix2)
print(test)

