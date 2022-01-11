somatorio = 0
qtdnum = 0
for c in range(1, 501):
    if c % 3 == 0 and c % 2 != 0:
        somatorio += c
        qtdnum = qtdnum + 1
print(somatorio)
print(qtdnum)
