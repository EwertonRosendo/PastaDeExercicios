import pacoteAula115
nome_e_idade = dict()
listaIndividual = list()
cadastros = list()
while True:
    try:
        print(f"{'-' * 40}\n{' ' * 13}MENU PRINCIPAL\n{'-' * 40}")
        print("\033[34m")
        print("[1] - Ver pessoas cadastradas ")
        print("[2] - Cadastrar uma nova pessoa ")
        print("[3] - Sair do sistema")
        print("\033[m")
        opcao = int(input("\033[33mSua opção: \033[m"))

        if opcao == 1:
            pacoteAula115.cadastrar(nome_e_idade, listaIndividual, cadastros)
        elif opcao == 2:
            pacoteAula115.cadastrar()
        elif opcao == 3:
            break
        else:
            print("\033[31mERRO: Informe uma opção existente!\033[m")
    except ValueError:
        print("\033[31mERRO: Informe um valor inteiro valido!\033[m")
