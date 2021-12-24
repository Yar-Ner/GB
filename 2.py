sec = int(input())
hour = sec // 3600
sec %= 3600
mins = sec // 60
sec %= 60
a = "{0}:{1}:{2}".format(hour, mins, sec)
print(a)
input()