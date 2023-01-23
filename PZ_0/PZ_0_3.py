# Задано натурально число N. Каждый повтор самой большой цифры числа N,продублировать.


chislo_per = int(input("Введите число: "))

izmen = [int(i) for i in str(chislo_per)]

for index, item in enumerate(izmen):
	if item == max(izmen):
	    izmen[index-1] = max(izmen)

print("Результат: ",int(''.join(map(str, izmen))))