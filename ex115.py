import pacoteAula115
cadastros = list()
while True:
    try:

        print(f"{'-' * 40}\n{' ' * 13}MENU PRINCIPAL\n{'-' * 40}")
        print(f"\033[34m")
        print("[1] - Ver pessoas cadastradas ")
        print("[2] - Cadastrar uma nova pessoa ")
        print("[3] - Sair do sistema")
        print("\033[m")
        print(f"{'-' * 40}")
        opcao = int(input("\033[33mSua opção: \033[m"))

        if opcao == 1:
            print(f"{'-' * 40}\n{' ' * 16}OPÇÃO 1\n{'-' * 40}")
            pacoteAula115.mostrarLista(cadastros)
        elif opcao == 2:
            print(f"{'-' * 40}\n{' ' * 16}OPÇÃO 2\n{'-' * 40}")
            pacoteAula115.cadastrar(cadastros)
        elif opcao == 3:
            break
        else:
            print("\033[31mERRO: Informe uma opção existente!\033[m")
    except ValueError:
        print("\033[31mERRO: Informe um valor inteiro valido!\033[m")
