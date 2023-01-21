Console.Clear();
Console.WriteLine("Введите число A: ");
int A = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Введите число B: ");
int B = Convert.ToInt32(Console.ReadLine());
Console.WriteLine ($"{A} в степени {B} = {Pow(A,B)}");


int Pow(int num, int rank)
{
    if(rank==0) return 1;
    int result = num;
    for (int i=2; i<=rank; i++)
    {
        result *= num;
    }
    return result;
}