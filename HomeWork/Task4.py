# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?
sum = int(input("Введите общее количество сдкланных журавлей: "))
if sum % 6 == 0:
    katya = int(sum / 6 )
    seryozha = katya
    petya = seryozha
    katya = katya * 4
    print(f"Катя сделала {katya} журавликов, Сережа сделал {seryozha} , Петя сделал {petya}")
else:
    print('Введено неверное условие!')