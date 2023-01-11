Console.Clear();
Console.WriteLine("Введите пятизначное число N ");
int N = Convert.ToInt32(Console.ReadLine());
int secondDigit = N/1000;
int fourthDigit = N/10;
Console.WriteLine(N);
if (N<=9999 || N>99999)
{
    Console.WriteLine("Введённое число не является пятизначным");
}
else if ((N-N%10000)/10000 == N%10 && (secondDigit%10 == fourthDigit%10))
{
    Console.WriteLine("является полиндромом");
}
else if ((N-N%10000 != N%10) && (secondDigit%10 != fourthDigit%10))
{
    Console.WriteLine("не является полиндромом");
}
