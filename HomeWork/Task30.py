# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


size = int(input("Введите размер списка: "))
elem_1 = int(input('Введите первый элемент: '))
num = int(input("Введите разность прогрессии: "))
lis_1 = []

for  i in range(size):
    lis_1.append(elem_1)
    elem_1 += num
print(lis_1)
