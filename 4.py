lst = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
itog = [i for i in lst if lst.count(i) < 2]

print(itog)
