import os
ip_ou_host = input("Digite um ip ou host a ser verificado: ")
# os.system chama todos os comandos relacionados com o sistema
os.system("ping -n 6 {}".format(ip_ou_host))
