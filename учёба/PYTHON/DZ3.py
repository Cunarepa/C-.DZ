A = []
N = int(input('Вводим количество элементов в массиве: '))
for i in range (N):
    A.append(int(input()))
X = int(input("Искомое число: "))
print (A.count(X))    