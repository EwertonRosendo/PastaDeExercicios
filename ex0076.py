listagem = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.90, "Estojo", 25.00, "Transferidor", 4.20)
listagem2 = ("Compasso", 9.99, "Mochila", 120.32, "Canetas", 22.30, "Livro", 34.9)
listagemgeral = listagem + listagem2
numitem = 0
texto = str(f"{listagemgeral[numitem]} custa exatos R$ {listagemgeral[numitem+1]:.2f}")
print("{}INICIO{}".format("-"*15, "-"*15))
# dividir o texto em 40 ESPAÇOS
while numitem != len(listagemgeral):
    print(f"{listagemgeral[numitem]} R$ {listagemgeral[numitem+1]:.2f}")
    numitem += 2
print("{}FIM{}".format("-"*15, "-"*15))
