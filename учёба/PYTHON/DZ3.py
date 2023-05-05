# A = []
# N = int(input('Вводим количество элементов в массиве: '))
# for i in range (N):
#     A.append(int(input()))
# X = int(input("Искомое число: "))
# print (A.count(X))    

N = int(input("Введите количество элементов в массиве: "))
list = []
for i in range (N):
    list.append(int(input()))
X = int(input("Введите заданное число: "))
diff_min = abs(list[0] - X)
k = list[0]
for i in list:
    if abs(i - X) < diff_min:
        diff_min = abs(i - X)
        k = i
print(k)        
    