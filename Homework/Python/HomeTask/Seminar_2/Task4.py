# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Сдвиньте все элементы списка на 2 позиции вправо.
# 3 -> [2, 3, -3, -2, -1, 0, 1]


list = []
N = int(input("Введите число: "))
for el in range(-N, N + 1):
    list.append(el)
print(list)

for i in range(2):
    list.insert(i, list[-2 + i])
print(list[:len(list) - 2])

