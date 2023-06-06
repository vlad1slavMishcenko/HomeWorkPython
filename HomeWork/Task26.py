#  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 



a = int(input("Введите число: "))
b = int(input("Введите степень: "))
res = a
def mult(x,y,res):
    
    if y == 1:
        return res
    else:
        res = res * x
        return mult(x,y -1,res)
    
n = mult(a,b,res)
print(n)
