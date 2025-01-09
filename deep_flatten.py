groups = [["Hong", "Ryan"], ["Anthony","Wilhelmia"], ["Margaret", "Adrian"]]


expected_output = ["Hong", "Ryan", "Anthony", "Wilhelmina", "Margaret", "Andrian"]


names = []
for group in groups:
	for n in group:
	   names.append(n)
print(names)