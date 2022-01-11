n = int(input("escreva um numero em metros que será convertido para centimetros e milimetros"))
print("{} metros equivale a {} centimetros e a {} milimetros".format(n, n*100, n*1000))
print("{} metros equivale a {}km, {}hm, {}dam, {}m , {}dm, {}cm, {}mm".format(n, n/1000, n/100, n/10, n, n*10, n*100, n*1000))
