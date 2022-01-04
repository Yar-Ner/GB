def my_fun(a, b, c):

	mass = [a, b, c]

	maxim1 = max(mass)

	ind = mass.index(maxim1)

	del(mass[ind])


	maxim2 = max(mass)

	print(int(maxim1) + int(maxim2))

my_fun(int(input()), int(input()), int(input()))
