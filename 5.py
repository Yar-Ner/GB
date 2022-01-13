a = []
one = 1

for i in range(100, 1001):
    if i%2 == 0:
        a.append(i)

for i in a:
    one = one * i
print(one) 
