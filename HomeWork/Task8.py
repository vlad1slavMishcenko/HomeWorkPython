# Задача 8: Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).

size1 = int(input("Введите длинну шоколадки: "))
size2 = int(input("Введите ширину шоколадки: "))
num = int(input("Сколько кусочков вы хотите отломить: "))

sum = size1 * size2
if num >= sum:
    print('Слишком большой кусок')
elif num % size1 == 0 or num % size2 == 0:
    print('yes')
else:
    print('no')