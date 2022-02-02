# Iniciando as variaveis
nome_e_peso = []
dados = list()
qtd_pessoas = 0
soma_de_peso = 0
soma_de_pessoas = 0
maior_peso = 0
menor_peso = 0
c = 0
# Variaveis de teste
nomes = ["Rosendo", "Rosa", "irineu", "davi", "caua", "erick"]
# Importando bibliotecas de teste
from random import choice, randint
# Laço infinito para colocar pessoas numa lista
while True:
    #  nome_e_peso.append(str(input("Informe o nome: "))), nome_e_peso.append(int(input("Informe o peso")))
    nome_e_peso.append(choice(nomes)), nome_e_peso.append(randint(60, 120))
    dados.append(nome_e_peso[:])  # Copia da lista nome_e_peso para a lista de dados
    soma_de_peso += nome_e_peso[1]  # Soma do peso de todas as pessoas cadastradas
    duvida = str(input("Deseja continuar? [S/N]")).upper().strip()
    if duvida in "N NÃO NOA NAO":
        break
    soma_de_pessoas += 1  # soma do numero de pessoas cadastradas
    print(nome_e_peso)
    nome_e_peso.clear()  # Limpando a lista
    # Quebra do laço
print("A media de peso é: {:.2f}".format(soma_de_peso/soma_de_pessoas))
print(f"O total de pessoas cadastradas foram {soma_de_pessoas}")
sorted(dados)
maior_peso = max(dados)
menor_peso = min(dados)
print(maior_peso)
print(menor_peso)
# Laço para mostrar as pessoas acima e abaixo do peso
print("Pessoas acima do peso: ")
for p in dados:
    if p[1] == maior_peso:
        print(f"{p[0]} com {p[1]}kg", end="..")
        c += 1
print("\nPessoas abaixo do peso")
for p2 in dados:
    if p2[1] == menor_peso:
        print(f"{p2[0]} com {p2[1]}kg", end="..")
        c += 1
dados.sort()
print("\n", dados)
