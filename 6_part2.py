from itertools import islice
from itertools import cycle

lst = [2, 5, "Надеюсь на отлично", None, "NaN", 0, 1.2, [1, 2, 3], "Привет", ("x + 5 = 10\n Найдите x")]
for i in islice(cycle(lst), 10):
    print(i)
