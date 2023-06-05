n = int(input())
m = int(input())
set1 = set()
set2 = set()
for i in range(n):
    set1.add(int(input()))
for i in range(m):
    set2.add(int(input()))
print(set1. intersection(set2))

n = int(input())
bush = []
for i in range (n):
    ber = int(input())
    bush.append(ber)
sums = []
for i in range(len(bush)-1):
    sums.append(bush[i] + bush[i-1] + bush[i+1])
sums.append(bush[-2] + bush[-1] + bush[0])
print(max(sums))                 
    