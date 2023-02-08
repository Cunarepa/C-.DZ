Console.Clear();
Console.Write("Введите количество строк массива: ");
int rows = int.Parse(Console.ReadLine());
Console.Write("Введите количество столбцов массива: ");
int columns = int.Parse(Console.ReadLine());
int[,]array = GetArray(rows, columns, 0, 10);
PrintArray(array);
Console.WriteLine(GetRowNumber(array));

int[,]GetArray(int m, int n, int min, int max)
{
    int[,]result = new int[m,n];
    for(int i = 0; i<m; i++)
    {
        for(int j=0; j<n; j++)
        {
            result[i,j]=new Random().Next(min,max+1);
        }
    }
    return result;
}

void PrintArray(int[,] inArray)
{
    for(int i = 0; i<inArray.GetLength(0); i++)
    {
        for(int j=0; j<inArray.GetLength(1); j++)
        {
            Console.Write($"{inArray[i,j]}");
        }
        Console.WriteLine();
    }
}

int GetRowNumber(int [,] array)
{
    int row = 0;
    int minsum = 0;
    for(int i=0; i<array.GetLength(1); i++)
    {
        minsum = minsum + array[0,i];
    }
    for(int i=1; i<array.GetLength(0); i++)
    {
        int sum = 0;
        for(int j = 0; j<array.GetLength(1); j++)
        {
            sum = sum + array[i,j];
        }
        if(minsum>sum)
        {
            minsum=sum;
            row=i;
        }
    }
    return row;
}