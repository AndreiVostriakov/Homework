﻿// Составить частотный словарь элементов двумерного массива. Частотный словарь содержит информацию о том, сколько раз встречается элемент входных данных.

int[,] GetArray(int m, int n, int minValue, int maxValue)
{
    int[,] result = new int[m, n];

    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            result[i, j] = new Random().Next(minValue, maxValue + 1);
        }
    }
    return result;
}

void PrintArray(int[,] inArray)
{
    for (int i = 0; i < inArray.GetLength(0); i++)
    {
        for (int j = 0; j < inArray.GetLength(1); j++)
        {
            Console.Write($"{inArray[i, j]}\t ");
        }
        Console.WriteLine();
    }
}

int[] Conver2DTo1Darray(int[,] inArray)
{
    int[] NewArray = new int[inArray.GetLength(0) * inArray.GetLength(1)];
    int k = 0;
    for (int i = 0; i < inArray.GetLength(0); i++)
    {
        for (int j = 0; j < inArray.GetLength(1); j++)
        {
            NewArray[k] = inArray[i, j];
            k++;
        }

    }
    return NewArray;
}

void sortArray(int[] inArray)
{
    int temp;
    for (int i = 0; i < inArray.Length - 1; i++)
    {
        for (int j = i + 1; j < inArray.Length; j++)
        {
            if (inArray[i] > inArray[j])
            {
                temp = inArray[i];
                inArray[i] = inArray[j];
                inArray[j] = temp;
            }
        }
    }
}

void PrintResult(int[] inArray)
{
    int count = 1;
    for (int i = 1; i < inArray.Length; i++)
    {
        if (inArray[i] == inArray[i - 1])
        {
            count++;
        }
        else
        {
            Console.WriteLine($" Количество {inArray[i - 1]} встречается {count} раз");
            count = 1;
        }
    }
    Console.WriteLine($" Количество {inArray.Length - 1} встречается {count} раз");
}

Console.Write("Введите кол-во строк: ");
int row = int.Parse(Console.ReadLine()!);
Console.Write("Введите кол-во столбцов: ");
int col = int.Parse(Console.ReadLine()!);

int[,] array = GetArray(row, col, 0, 3);

PrintArray(array);
Console.WriteLine();
int[] Newarray = Conver2DTo1Darray(array);
sortArray(Newarray);
Console.WriteLine();
PrintResult(Newarray);