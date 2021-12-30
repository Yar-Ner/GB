l = [4, 3, 3, 2, 1]
new = int(input())

i = 1

for n in l:
	if new <= n:
		i += 1
	else:
		break
l.insert(i, new)
print(l)
