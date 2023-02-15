Console.Clear();

Console.WriteLine("Введите M: ");
int mA = int.Parse(Console.ReadLine());

Console.WriteLine("Введите N: ");
int nA = int.Parse(Console.ReadLine());

int Ackermann(int m, int n)
{
    if (m == 0) return n + 1;
    else if (n == 0) return Ackermann(m - 1, 1);
    else return Ackermann(m - 1, Ackermann(m, n - 1));
}

Console.WriteLine(Ackermann(mA, nA));