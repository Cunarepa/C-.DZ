Console.WriteLine("Введите число N: ");
int N = int.Parse(Console.ReadLine());
if(N<0)
{
    N*=-1;
}
for(int i=1; i<=N; i++)
{
    Console.Write($"{i*i*i}, ");
}