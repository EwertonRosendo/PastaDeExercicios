altura = float(input("qual a altura da parede a ser pintada? "))
largura = float(input("qual a largura da parede a ser pintada? "))
area = altura*largura
print("para pintar essa parede de {}m^2 serão necessarios {} litros de tinta". format(area, area/2))