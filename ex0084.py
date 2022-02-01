# Iniciando as variaveis
nome_e_peso = []
dados = list()
qtd_pessoas = 0
soma_de_peso = 0
soma_de_pessoas = 0
# Variaveis de teste
nomes = ["Rosendo", "Rosa", "irineu", "davi", "caua", "erick"]
# Importando bibliotecas de teste
import random
# Laço infinito para colocar pessoas numa lista
while True:
    #nome_e_peso.append(str(input("Informe o nome: "))), nome_e_peso.append(int(input("Informe o peso")))
    nome_e_peso.append(random.choice(nomes)), nome_e_peso.append(random.randint(60, 120))
    dados.append(nome_e_peso[:]) # Copia da lista nome_e_peso para a lista de dados
    soma_de_peso += nome_e_peso[1]# Soma do peso de todas as pessoas cadastradas
    soma_de_pessoas += 1# soma do numero de pessoas cadastradas
    print(nome_e_peso)
    nome_e_peso.clear()# Limpando a lista
    # Quebra do laço
    duvida = str(input("Deseja continuar? [S/N]")).upper().strip()
    if duvida in "N NÃO NOA NAO":
        break
print("A media de peso é: {:.2f}".format(soma_de_peso/soma_de_pessoas))
# Laço para mostrar as pessoas acima e abaixo do peso
for p in dados:
    if p[1] > (soma_de_peso/soma_de_pessoas):
        print("{} está acima da media de peso com {}kg".format(p[0], p[1]))
    elif p[1] < (soma_de_peso/soma_de_pessoas):
        print(f"{p[0]} está abaixo da media de peso com {p[1]}kg")
print(f"O total de pessoas cadastradas foram {soma_de_pessoas}")
