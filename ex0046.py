from time import sleep
print("=-="*3, "INICIO", "=-="*3)
print("Contagem regressiva")
for c in range(10, -1, -1):
    print("Faltam {} segundos".format(c) if c!=1 else "Falta {} segundo".format(c))
    sleep(1)
print("=-="*3, "FIM", "=-="*3)

