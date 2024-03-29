# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

def task1():
    list_1 = set([1, 1, 2 ,0, -1, 3, 4, 4])
    print(len(list_1))

    list_2 = []
    for i in list_1:
        if i not in list_2:
            list_2.append(i)
    print(len(list_2))


# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

def task2():
    n = int(input("Введите число: "))
    list_1 = [1,2,3,4,5]
    list_2 = list_1[n:] + list_1[:n]
    print(list_2)


# Задача №23. Общее обсуждение
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

def task():
    list1 = [0, -1, 5, 2, 2]
    count = 0

    for i in range(1, len(list1)):
        if list1[i] > list1[i-1]:
            count += 1

    print(count)


# Задача №21. Решение в группах
# Напишите программу для печати всех уникальных значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {"VIII":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально.
# Пользователь его не вводит

list_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
dict_1 = {}
list_2 = []
for i in list_1:
    dict_1 = i
    for i in dict_1:
        if dict_1[i] not in list_2:
            list_2.append(dict_1[i])
print(*list_2)