try:
    a = int(input("Informe um numero: "))
    b = int(input("Informe o divisor: "))
    r = a/b

except Exception as causa:
    print("Infelizmente tivemos o problema {}".format(causa.__class__))

else:
    print("O resultado da divisão é {}".format(r))

finally:
    print("FINAL DO PROGRAMA")