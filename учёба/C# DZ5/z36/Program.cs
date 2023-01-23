Console.Clear();
int[]startArray = GetArray(4, -100, 100);
Console.WriteLine(String.Join(" ", startArray));
Console.WriteLine(GetSumOdd(startArray));

int[]GetArray(int size, int minValue, int maxValue)
{
    int[]res = new int[size];
    for (int i = 0; i < size; i++)
    {
        res[i] = new Random().Next(minValue, maxValue+1);
    }
    return res;
}

int GetSumOdd(int[] array)
{
    int sum = 0;
    for (int i=0; i < array.Length; i++)
    {
        if(i%2==1) sum+=array[i];
    }
    return sum;
}