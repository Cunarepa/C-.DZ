def recurs(A, B):
    if B == 0:
        return 1
    if B < 0:
        return 1/A * recurs(A, B+1)
    return recurs(A, B-1) * A
    
A = int(input())
B = int(input())
print(recurs(A, B))    


def sum(A, B):
    if B == 0:
        return A
    return sum(A+1, B-1)

A = int(input())
B = int(input())
print(sum(A, B))