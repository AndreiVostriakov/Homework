import random

# Задача №9. Решение в группах
# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл while
# Input: 5
# Output: 120

def factorial():
    N = int(input("Введите число: "))
    res = 1
    count = 1
    while count <= N:
        res *= count
        count += 1
    print(res)


# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

def Fi():
    fibonachi_number = int(input("Введите число из последовательности фибоначи "))
    positiv_check = bool(fibonachi_number > 0)
    if positiv_check:
        first_number = 1
        second_number = 1
        curent_number = first_number + second_number
        count = 3
        while first_number < fibonachi_number:
            second_number = first_number
            first_number = curent_number
            curent_number = first_number + second_number
            count += 1

        print(
            "Число {} является {} в последовательности фибоначи ".format(
                fibonachi_number, count
                )
            )

# Задача №13. Общее обсуждение
# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в
# свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала
# 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе.
# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2

def weather():
    n = int(input('общее количестворассматриваемых дней '))
    max_count = 0
    count = 0

    for i in range(1, n + 1):
        el = int(input('среднесуточная температура всоответствующий день '))
        if (el > 0):
            count += 1
            if(count > max_count):
                max_count = count
        else:       
            count = 0
    print(max_count)

# 15. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

def melon():
    N = int(input("Введите кол-во арбузов: "))
    array = []

    for i in range(N):
        i = random.randint(2, 10)
        array.append(i)

    print(max(array), min(array))
    print(array)

