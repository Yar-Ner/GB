from sys import argv

name, chas, stavka, prem = argv

zp = (int(chas) * int(stavka)) + int(prem)

print("З/п сотрудника составило: ", str(zp))
