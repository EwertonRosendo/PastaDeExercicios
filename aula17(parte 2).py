'''teste = list()
teste.append("Ewerton")
teste.append(18)
galera = []
galera.append(teste[:])
teste[0] = "maria"
teste[1] = 20
galera.append(teste[:])
print(galera)'''
#galera = [["João", 19], ["Ana", 33], ["Joaquim", 13], ["Maria", 41]]
#print(galera[3][0])
'''for p in galera:
    print(p[0], end=" ")
    print(p[1])'''
individuo = []
pessoas = list()
for c in range(0, 2):
    individuo.append(str(input("Informe um nome: "))), individuo.append(int(input("Informe sua idade")))
    pessoas.append(individuo[:])
    del individuo[:]
for p in pessoas:
    print(f"A pessoa {p[0]} tem {p[1]} anos")