Console.Clear();
Console.Write("Введите через пробел значения b1, k1, b2, k2: ");
string[]f = Console.ReadLine().Split(" ", StringSplitOptions.RemoveEmptyEntries);
double b1 = double.Parse(f[0]);
double k1 = double.Parse(f[1]);
double b2 = double.Parse(f[2]);
double k2 = double.Parse(f[3]);

Console.WriteLine(String.Join(" ", GetPoint(b1, k1, b2, k2)));

double[] GetPoint (double onB1, double onK1, double onB2, double onK2)
{
    double[]result = new double[2];
    result[0] = (onB2 - onB1)/(onK1 - onK2);
    result[1] = onK1 * result[0] + onB1;
    return result;
}