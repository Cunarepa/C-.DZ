Console.Clear();
Console.Write("Введите числа через пробел: ");
int[]numbers = GetArrayFromString(Console.ReadLine());
Console.WriteLine ($"Количество чисел больше 0: {GetCountPositiveElements(numbers)}");


int[]GetArrayFromString(string stringArray)
{
    string[]nums = stringArray.Split(" ", StringSplitOptions.RemoveEmptyEntries);
    int[]result = new int [nums.Length];
    for(int i = 0; i<result.Length; i++)
    {
        result[i]= int.Parse(nums[i]);
    }
    return result;
}


int GetCountPositiveElements(int[]array)
{
    int count = 0;
    foreach (int item in array)
    {
        if (item > 0)  count++;
    }
    return count;
}
        