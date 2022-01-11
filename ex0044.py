preco = float(input("Informe o valor do produto: "))
print("1- A vista em dinheiro ou cheque = 10% de desconto")
print("2- A vista no cartão = 5% de desconto")
print("3- Em ate duas vezes no cartão = preço normal")
print("4- 3 vezes ou mais no cartão = 20% de juros")
opcao = int(input())
if opcao == 1:
    print("O novo preço do produto é {}, com 10% de desconto".format(preco - (preco*0.1)))
elif opcao == 2:
    print("O novo preço do produto é {}, com 5% de desconto".format(preco - (preco*0.05)))
elif opcao == 3:
    print("O preço do produto permanece o mesmo")
elif opcao == 4:
    print("O novo preço do produto é {}, com 20% de juros".format(preco+(preco*0.2)))