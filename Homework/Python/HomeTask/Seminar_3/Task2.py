# Задача 2. В списке находятся названия фруктов.
# Выведите все фрукты, названия которых начинаются на заданную букву.
# а –> абрикос, авокадо, апельсин, айва.

fruits = {"а": "абрикос, авокадо, апельсин, айва",
          "б": "банан",
          "в": "виноград, вишня",
          "г": "гранат, груша"
          }

letter = input("Введите первую букву фрукта: ")
if letter in fruits.keys():
    print(f"На букву '{letter}' есть: {fruits[letter]}")
else:
    print("Таких фруктов у нас нет")

    