print("Gerador de PA")
print("-="*10)
primeiro = int(input("Informe o primeiro termo: "))
razao = int(input("Informe a razão da PA: "))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print("{}".format(termo), end=" ")
        termo += razao
        cont += 1
    print("PAUSADA")
    mais = int(input("Quantos termos você quer mostrar a mais? "))
print("FIM")
