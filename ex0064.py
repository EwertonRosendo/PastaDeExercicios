soma = qtdnum = num = 0
print("------------------------INICIO------------------------")
num = int(input("\033[36mInforme numeros para no fim serem somados: "))
while num != 999:
    qtdnum += 1
    soma += num
    print("\033[36mPara encerrar o looping insira 999 como numero!")
    num = int(input("\033[36mInforme numeros para no fim serem somados: "))
print("\033[33mA soma de todos os numeros informados é de ", soma)
print("\033[32mA quantidade de numeros informados pelo usuario é de ", qtdnum)
print("------------------------FIM------------------------")