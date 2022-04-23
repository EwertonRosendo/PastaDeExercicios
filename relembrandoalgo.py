cadastros = list()
pessoa = list()
nome_senha = dict()
while True:
    # Informando usuario e senha num dicionario
    nome_senha["usuario"] = str(input("Informe seu usuario: "))
    nome_senha["senha"] = str(input("Informe sua senha: "))

    # A lista pessoa está recebendo um cadastro
    pessoa.append(nome_senha.copy())

    # A pessoa cadastrada está sendo passada ao banco de dados
    cadastros.append(pessoa[:])

    # Limpando as variaveis iniciais para utilizar novamente
    nome_senha.clear(), pessoa.clear()

    # Exibindo todos os cadastros
    print(cadastros)

    # Se a aplicação continua ou não
    continuar = str(input("Deseja continuar? [S/N] ")).strip().upper()
    while continuar not in "S N":
        continuar = str(input("Informe um valor valido! Deseja continuar? [S/N] ")) 
    if continuar in "N":
        break



# Fim da aplicação
print("Fim")
