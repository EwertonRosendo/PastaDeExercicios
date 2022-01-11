nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))
nota4 = float(input("Informe a quarta nota: "))
media = (nota4 + nota3 + nota2 + nota1) / 4
if media < 5:
    print("Infelizmente você foi reprovado por ter uma media de {}, abaixo dos 5 pontos necessarios".format(media))
elif 5 <= media <= 6.9:
    print("Você está de recuperação com uma nota de {}".format(media))
elif media>=7:
    print("Você está aprovado com uma nota de {}".format(media))

