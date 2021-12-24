viruchka = int(input("Выручка: "))
izderzhka = int(input("Издержки: "))

if viruchka < izderzhka:
	print("Убыток")
elif viruchka > izderzhka:
	print("Выручка больше")
	kol_vo = int(input("Количество сотрудников: "))
	print("Выручка:", viruchka - izderzhka)
	print("Рентабельность: ", int(pribil / viruchka))
	itog = pribil / kol_vo
	print("Прибыль на одного сотрудника: ", itog)	
else:
	print("Не думал что будет такая подлянка, они равны)")