quilometros = float(input("Infome quantos quilometros tem sua viagem: "))
if quilometros > 200:
    print("Como sua viagem tem mais de 200Kms, custará 0,45R$ por Km")
    print("Logo, sua viagem custará {}R$".format(quilometros*0.45))
else:
    print("Como sua viagem tem menos de 200Kms, custará 0,50R$ por Km")
    print("Logo, sua viagem custará {}R$".format(quilometros*0.5))