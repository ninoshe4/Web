import random
import math

razn = 0
pop = 0
chislo = random.randint(1, 100)

print("Вам загадали число от  1 до 100, у вас три попытки !")

while pop < 3:
    otvet = int(input("Введите ответ:"))
    razn = otvet - chislo
    if abs(razn) < 10:
        print("Вы почти у цели!")
    if abs(razn) > 10:
        print("Ваш ответ в диапазоне 10 от верного!")
    if 10 < abs(razn) > 20:
        print("Ваш ответ в диапазоне 20 от верного!")
    if 20 < abs(razn) > 30:
        print("Ваш ответ в диапазоне 30 от верного!")
    if 30 < abs(razn) > 40:
        print("Ваш ответ в диапазоне 40 от верного!")
    if 40 < abs(razn) > 50:
        print("Ваш ответ в диапазоне 50 от верного!")
    pop += 1

    if otvet == chislo:
        break

if otvet == chislo:
    print("Вы угадали! Вы справились за", pop, "попытки")
else:
    print("Game over")
