from itertools import count
from itertools import islice


a = int(input())

for i in islice(count(a), a+10):
    print(i)
