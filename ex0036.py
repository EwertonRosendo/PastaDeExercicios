valorcasa = float(input("Qual o valor da casa? "))
valorsalario = float(input("qual o seu salario? "))
anos = float(input("Em quantos anos você planeja pagar o emprestimo"))
meses = anos*12
mensalidade = valorcasa/meses
if mensalidade > (valorsalario * 0.3):
    print("-"*20)
    print("\033[31m Infelizmente o emprestimo foi negado por não cumprir os termos de pagamento\033[m")
    print("\033[31m o emprestimo seria de {:.2f}R$ por mês".format(mensalidade))
elif mensalidade <= valorsalario*0.3:
    print("-"*20)
    print("\033[32m Parabens, o emprestimo para o pagamento de sua casa foi aprovado!\033[m")
    print("\033[32m O emprestimo será de {:.2f}R$ por mês".format(mensalidade))
