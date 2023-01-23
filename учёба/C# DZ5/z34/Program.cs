Console.Clear();
int[]startArray = GetArray(4, 100, 999);
Console.WriteLine(String.Join(" ", startArray));
Console.WriteLine(GetEvenCount(startArray));

int[]GetArray(int size,int minValue, int maxValue)
{
    int[]res = new int[size];
    for (int i = 0; i < size; i++)
    {
        res[i] = new Random().Next(minValue, maxValue+1);
    }
    return res;
}

int GetEvenCount(int[]array)
{
    int count = 0;
    foreach(var item in array)
    {
        if(item%2==0) count++;
    }
    return count;
}
