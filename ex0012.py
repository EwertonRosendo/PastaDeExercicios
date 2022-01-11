valor = float(input("qual o valor atual do produto o qual você deseja dar o desconto? "))
desconto = float(input("quanto de desconto você quer dar ao produto? em porcentagem "))
print("o produto custava {}, mas com desconto de {}% ele passa a custar {:.2f}R$".format(valor, desconto, (valor -(( desconto * 1/100)*valor))))

