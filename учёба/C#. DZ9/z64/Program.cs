Console.WriteLine("Задайте значение N: ");
int N = int.Parse(Console.ReadLine());

void PrintNumbers(int start)
{
    if (start < 1) return;
    Console.Write($"{start} ");
    if (start == 1) return;
    PrintNumbers(start - 1);
}

PrintNumbers(N);