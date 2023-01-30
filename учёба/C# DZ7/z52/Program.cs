Console.Clear();
Console.Write("Введите количество строк массива: ");
int rows = int.Parse(Console.ReadLine());
Console.Write("Введите количество столбцов массива: ");
int columns = int.Parse(Console.ReadLine());
int[,] array = GetArray(rows, columns, 0, 10);
PrintArray(array);

double[] averageColumns = GetResultArray(array);
Console.WriteLine($"Среднее арифметическое каждого столбца: {String.Join (";", averageColumns)}");

int[,] GetArray(int m, int n, int min, int max)
{
    int[,] result = new int[m, n];
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            result[i, j] = new Random().Next(min, max + 1);
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
            Console.Write($"{inArray[i, j]}");
        }
        Console.WriteLine();
    }
}

double[] GetResultArray(int[,] array)
{
    double[] result = new double[array.GetLength(1)];
    for (int columns = 0; columns < array.GetLength(1); columns++)
    {
        double sum = 0;
        for (int rows = 0; rows < array.GetLength(0); rows++)
        {
            sum += array[rows, columns];
        }
        result[columns] = Math.Round(sum / array.GetLength(0), 2);
    }
    return result;
}