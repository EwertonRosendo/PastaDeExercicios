salario = float(input("informe o salario atual do cara "))
aumento = float(input("agora informe quanto de aumento você deseja dar ao cara. (em porcentagem) "))
print("o salario do cara saiu de {} R$ para {:.2f} R$ com um aumento de {}%".format(salario, salario + (salario*(aumento/100)), aumento))