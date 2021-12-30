l = list(input())

for i in range(1, len(l), 2):
	l[i - 1], l[i] = l[i], l[i - 1]

print(l)
