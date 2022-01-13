spisok = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [num for i, num in enumerate(spisok) if i > 0 and spisok[i] > spisok[i - 1]]
result = [first for first, second in zip(spisok[1:], spisok[:-1]) if first > second]
print(result)
