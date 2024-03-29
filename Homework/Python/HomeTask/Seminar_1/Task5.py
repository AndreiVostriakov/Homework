# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:* 123 -> 6 (1 + 2 + 3)
#           100 -> 1 (1 + 0 + 0)

def sum_number():
    flag = True
    res = 0
    while flag:
        num = int(input("Введите трёхзначное число: "))
        if num >= 100 and num < 1000:
            res = (num // 100) + (num // 10 % 10) + (num % 10)
            print(res)
            flag = False
        else:
            print("Число не трёхзначное")


# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

def made_toys():
    S = int(input("Введите кол-во сделанных журавликов: "))
    if not S % 6:
        petya = S // 6
        sergey = petya
        kate = petya * 4
        print(f"Петя сделал {petya} штук(и), Катя сделала {kate} штук(и), и Серёжа сделал {sergey} штук(и)")
        

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

def sum_number1():
    flag = True
    res1 = 0
    res2 = 0
    while flag:
            num = int(input("Введите шестизначное число: "))
            if num >= 100000 and num < 1000000:
                res1 = (num // 100000) + (num // 10000 % 10) + (num // 1000 % 10)
                res2 = (num // 100 % 10) + (num // 10 % 10) + (num % 10)
                if res1 == res2:
                    print("Yes")
                    flag = False
                else:
                    print("No")
                    flag = False
            else:
                print("Число не шестизначное.")
                

# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

def piece_of_chocolate():
    n = int(input("Введите длину шоколадки: "))
    m = int(input("Введите ширину шоколадки: "))
    k = int(input("Введите кол-во долек, которые необходимо отломить от шоколадки: "))
    if k < n * m and ((k % n == 0) or (k % m == 0)):
        print("Yes")
    else:
        print("No")