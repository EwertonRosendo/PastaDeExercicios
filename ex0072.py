contagem = ("ZERO", "UM", "DOIS", "TRÊS", "QUATRO", "CINCO", "SEIS", "SETE", "OITO", "NOVE", "DEZ", "ONZE", "DOZE", "TREZE", "QUATORZE", "QUINZE", "DEZESSEIS"," DEZESSETE", "DEZOITO", "DEZENOVE", "VINTE")
while True:
    c = int(input("Informe um numero: "))
    while c < 0 or c > 20 and c != 999:
        c = int(input("Informe um numero valido ou digite 999 para sair"))
    if c == 999:
        break
    print(contagem[c])
print("FIM")
