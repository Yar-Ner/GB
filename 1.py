a = int(input("Только не ноль! "))
b = int(input("Только не ноль! "))
def my_func(x, y):
	return x / y
try :
	a / b	
except ZeroDivisionError:
	print("Ай АЙ Ай, я же просил")
else:
	print(round(a / b)
