﻿Console.Clear();
Console.Write("Введите количество строк 1 массива: ");
int rowsA = int.Parse(Console.ReadLine());
Console.Write(" Введите количество столбцов 1 массива: ");
int columnsA = int.Parse(Console.ReadLine());
Console.Write("Введите количество строк 2 массива: ");
int rowsB = int.Parse(Console.ReadLine());
Console.Write("Введите количество столбцов 2 массива: ");
int columnsB = int.Parse(Console.ReadLine());
if(columnsA != rowsB)
{
    Console.WriteLine("Невозможно выполнить действие!");
    return;
}

int[,]A = GetArray(rowsA, columnsA, 0, 10);
int[,]B = GetArray(rowsB, columnsB, 0, 10);
PrintArray(A);
Console.WriteLine();
PrintArray(B);
Console.WriteLine();
PrintArray(GetProizvMat(A,B));

int[,]GetArray(int m, int n, int min, int max)
{
    int[,]result = new int[m,n];
    for(int i=0; i<m; i++)
    {
        for(int j=0; j<n; j++)
        {
            result[i,j]=new Random().Next(min, max+1);
        }
    }
    return result;
}

void PrintArray(int[,] inArray)
{
    for(int i=0; i<inArray.GetLength(0); i++)
    {
        for(int j=0; j<inArray.GetLength(1); j++)
        {
            Console.Write($"{inArray[i,j]}");
        }
        Console.WriteLine();
    }
}

int[,]GetProizvMat(int[,] arrayA, int[,] arrayB)
{
    int[,]arrayC = new int[arrayA.GetLength(0), arrayB.GetLength(1)];
    for(int row = 0; row<arrayA.GetLength(0); row++)
    {
        for(int column = 0; column<arrayB.GetLength(1); column++)
        {
            for(int k = 0; k<arrayA.GetLength(1); k++)
            {
                arrayC[row, column] += arrayA[row,k] * arrayB[k, column];
            }
        }
    }
    return arrayC;
}