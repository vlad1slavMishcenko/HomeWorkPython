# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
from random import randint

n = int(input('Введите количество манет: '))
l = []
num1 = 0
num2 = 0


for i in range(n):
    l.append(randint(0,1))


for i in range(n):
    if l[i] == 0:
        num1+= 1
    else:
        num2+= 1
    i+= 1
print(l)
if num1 > num2:
    print(f'Нужно перевернуть {num2} монет')
else:
    print(f'Нужно перевернуть {num1} монет')


               
