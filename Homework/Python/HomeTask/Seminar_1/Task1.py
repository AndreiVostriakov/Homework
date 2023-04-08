# Задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и выводит название этого дня недели.
# 1 –> Понедельник
# 10 –> Нет такого дня
# 7 –> Воскресение

week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
print("Для выхода из программы используйте число '0'")
flag = True
while flag:
    number = int(input("Введите число, обозначающее день недели: "))
    if number > 0 and number <= 7:
        print(f"Это {week[number - 1]}")
    elif number == 0:
        flag = False
    else:
        print("Такого дня нет")
        