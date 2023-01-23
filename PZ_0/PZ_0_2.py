# Пользователь должен загадать число, а компьютер, используя оптимальный алгоритм
# должен его угадать

import random

print("Для обратной связи с компьютером используйте фразы Больше.Меньше.Равно")
x, y = 0, 100
zag = int(input("Введите любое число от 1 до 100:"))
if zag > 100:
    zag = int(input("Ошибка! Введите число от 1 до 100: "))


comp = random.randrange(x, y + 1)
popitka = 1
while x != y:
    print("Ваше число равно, больше или меньше: ", comp)
    user_answer = input()
    if 'Больше' in user_answer:
        x = comp
        comp = random.randrange(x, y)
        popitka += 1
    elif 'Меньше' in user_answer:
        y = comp
        comp = random.randrange(x, y)
        popitka += 1
    elif 'Равно' in user_answer:
        break

print('Число, которое вы загадали:', zag,  ' Число, которое отгадал компьюетр: ', comp, 'Количество попыток:', popitka)
