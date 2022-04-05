def ajuda():
    while True:
        comandoPesquisar = str(input("Digite um comando ou [FIM]: ")).lower().strip()
        if comandoPesquisar in "fim":
            break

        return help(comandoPesquisar)


print(f"\033[1;40m {ajuda()} \033[m")
