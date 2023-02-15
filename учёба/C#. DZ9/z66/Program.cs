Console.Clear();

Console.WriteLine("Задайте значение M: ");
int m = int.Parse(Console.ReadLine());
Console.WriteLine("Задайте значение N: ");
int n = int.Parse(Console.ReadLine());

int SumNutEl(int firstNum, int secondNum)
{

    int sum = 0;
    if (firstNum == secondNum) return secondNum;
    sum = firstNum + SumNutEl(firstNum + 1, secondNum);
    return sum;
}

Console.WriteLine(SumNutEl(m, n));