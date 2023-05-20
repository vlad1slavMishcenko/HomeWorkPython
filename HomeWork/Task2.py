# Задача 2: Найдите сумму цифр трехзначного числа. 
num = int(input("Введите трехзначное число: "))
sum = 0
if num > 99 and num < 1000:
    while num > 0:
        sum = sum + num % 10 
        num = num // 10
    print(sum)    
else:
    print("Введено неверное число")