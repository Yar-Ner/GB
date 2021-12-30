inp = int(input())


if inp == 1 or inp == 2 or inp == 12:
	print("Зима")
elif inp == 3 or inp == 4 or inp == 5:
	print("Весна")
elif inp == 6 or inp == 7 or inp == 8:
	print("Лето")
elif inp == 9 or inp == 10 or inp == 11:
	print("Осень")

month = {
	1 : "Январь",
	2 : "Февраль",
	3 : "Март",
	4 : "Апрель",
	5 : "Май",
	6 : "Июнь",
	7 : "Июль",
	8 : "Август",
	9 : "Сентябрь",
	10 : "Октябрь",
	11 : "Ноябрь",
	12 : "Декабрь"
}

if inp in month:
	print(inp, " месяц года это ", month[inp])

else:
	print("Неправда")
