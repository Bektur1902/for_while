
counter1 = 0
counter2 = 0

for i in range(-100,101):
	if i % 13 == 0 and i % 2 == 0:
		i ** 2
		counter1 += 1
		print('Первое условие', counter1, i)

for i in range(-100,101,7):
	if i % 2 == 1:
		counter2 += 1
		print('Второе условие', counter2, i)
