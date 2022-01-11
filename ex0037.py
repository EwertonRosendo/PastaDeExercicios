nome = str(input("Pô, me diz seu nome ai: ")).strip()
num = int(input("Informe um numero, pls: "))
escolha = int(input(" 1- Converter para binario \n 2- Converter para octal \n 3- Converter para hexadecimal\n"))
if escolha == 1:
    print("\033[32m a opção escolhida foi binario, o numero convertido é {} \033[m".format(bin(num)[2:]))
elif escolha == 2:
    print("\033[32m a opção escolhida foi octal, o numero convertido é {} \033[m".format(oct(num)[2:]))
elif escolha == 3:
    print("\033[32m a opção escolhida foi hexadecimal, o numero convertido é {} \033[m".format(hex(num)[2:]))
else:
    print("\033[31m {}, você não escolheu nenhuma das opções validas. Por favor, rode o aplicativo novamente! \033[m ".format(nome))

