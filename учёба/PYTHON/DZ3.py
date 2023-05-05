# A = []
# N = int(input('Вводим количество элементов в массиве: '))
# for i in range (N):
#     A.append(int(input()))
# X = int(input("Искомое число: "))
# print (A.count(X))    

# N = int(input("Введите количество элементов в массиве: "))
# list = []
# for i in range (N):
#     list.append(int(input()))
# X = int(input("Введите заданное число: "))
# diff_min = abs(list[0] - X)
# k = list[0]
# for i in list:
#     if abs(i - X) < diff_min:
#         diff_min = abs(i - X)
#         k = i
# print(k)       

points_eng = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}
points_ru = {1: "АВЕИНОРСТ", 2: "ДКЛМПУ", 3: "БГЁЬЯ", 4: "ЙЫ", 5: "ЖЗХЦЧ", 8: "ШЭЮ", 10: "ФЩЪ"}
word = input("Введите слово: ").upper()
points = 0
if word[0] in 'AEIOULNSTRDGBCMPFHVWYKJXQZ':
    for let in word:
        for i in points_eng:
            if let in points_eng[i]:
                points +=i
else:
    for let in word:
        for i in points_ru:
            if let in points_ru[i]:
                points +=i
print(points)                                