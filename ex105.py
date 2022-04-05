dicionarioDasNotas = dict()
def notas(*valoresDasNotas, sit=False):
    print(valoresDasNotas)
    global dicionarioDasNotas
    dicionarioDasNotas['total'] = len(valoresDasNotas)
    maior = 0
    menor = 0
    somaDasNotas = 0
    for c, n in enumerate(valoresDasNotas):
        somaDasNotas += n
        if c == 1:
            maior = n
            menor = n
        else:
            if n < menor:
                menor = n
            if n > maior:
                maior = n
    dicionarioDasNotas["maior"] = maior
    dicionarioDasNotas["menor"] = menor
    dicionarioDasNotas["media"] = float(somaDasNotas/len(valoresDasNotas))
    if sit == True:
        if dicionarioDasNotas["media"] >= 7:
            dicionarioDasNotas["situação"] = "BOM"
        else:
            dicionarioDasNotas["situação"] = "RUIM"
    return dicionarioDasNotas


print(notas(7, 5, 4, 9, 8, sit=True))
