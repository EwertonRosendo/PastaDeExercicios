from random import randint
num = []
matrix = []
matrix2 = []
matrix3 = []
matriz_real = []
p = 0
p1 = 0
for c in range(0, 9):
    num.append(randint(0, 100))
    if c < 3:
        matrix.append(num[:])
        num.clear()
    elif 3 < c < 7:
        matrix2.append(num[:])
        num.clear()
    else:
        matrix3.append(num[:])
        num.clear()
print(f"{matrix}\n{matrix2}\n{matrix3}")
'''print(matrix, end="\n")
print(matrix2, end="\n")
print(matrix3, end="\n")'''
