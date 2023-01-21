Console.Clear();
Console.Write("Введите число: ");
int num = int.Parse(Console.ReadLine());
Console.WriteLine($"Сумма цифр = {GetSumNums(num)}");

int GetSumNums(int number)
{
    int sum = 0;
    while(number != 0)
    {
        sum += number%10;
        number/=10;
    }
    return sum;
}