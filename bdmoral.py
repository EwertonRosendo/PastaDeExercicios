import random
listaDeCadastros = list()
pessoaCadastrada = dict()
listaDePessoa = list()

# cadastro

def cadastrar():
    '''
            
    CODIGO REALL
            
    pessoaCadastrada["email"] = str(input("Email: ")).lower()
    pessoaCadastrada["username"] = str(input("Usuario: ")).lower()
    pessoaCadastrada["senha"] = str(input("Senha: "))

    '''
    # Criando testes automaticos
    # INICIO

    emailBeta = ("ewerton@gmal", "joabe@gmal", "erica@gmal", "karlao@gmal", "manu@gmal", "davi@gmal", "erick@gmal", "caua@gmal")
    usernamesBeta = ("geragera", "araçoiabei", "hellcife", "nassauloco", "seloquinha", "bawzinho123", "minecloucooo", "dragonfodase")
    senhasBeta = ("2535325353", "23534523523", "52532523452", "325424525234", "435342523543", "34523523531", "34542352354")

    # FIM
    pessoaCadastrada["email"] = emailBeta[random.randint(0, 7)]
    pessoaCadastrada["username"] = usernamesBeta[random.randint(0,  4)]
    pessoaCadastrada["senha"] = random.choice(senhasBeta)
    listaDePessoa.append(pessoaCadastrada.copy())
    listaDeCadastros.append(listaDePessoa[:])
    pessoaCadastrada.clear(), listaDePessoa.clear()
    print("{}NOVO USUARIO CADASTRADO{}".format('~' * 10, '~' * 10))
    print(listaDeCadastros)
    print("~" * 30)


# Pesquisar
# [['email': 'email', 'username': 'meunomenojogo', 'senha':'minha senha'], ['email2': 'email2', 'username2': 'meunomenojogo2', 'senha2':'minha senha2']]
def pesquisar():
    c = -1
    email = str(input("Informe o email do usuario a ser pesquisado! "))
    for individuo in listaDeCadastros:
        if individuo[0]['email'] == email:
            c += 1
    if c != -1:
        print("\033[32mUsuario encontrado!\033[m")
    else:
        print("\033[31mUsuario não encontrado\033[m")


# Editar

# Apagar
def deletar():
    usuario = str(input("Informe o usuario a ser deletado: "))
    for individuo in listaDeCadastros:
        if individuo[0]['username'] == usuario:
            del individuo[0]
    print(listaDeCadastros)






while True:
    print("[1] - Cadastrar")
    print("[2] - Pesquisar")
    print("[3] - Editar")
    print("[4] - Apagar")
    escolha = int(input("Escolha uma opção: "))

    while escolha > 4 or escolha < 0:
        escolha = int(input("Informe um valor valido! "))

    if escolha == 1:
        cadastrar()

    if escolha == 2:
        pesquisar()

    if escolha == 4:
        deletar()

    if escolha == 0:
        break
