primeirotermo = int(input("Informe o primeiro termo da PA: "))
razao = int(input("Informe a razao da PA"))
numerotermos = 0
while (primeirotermo + (razao*9)) != (primeirotermo+(razao*numerotermos)):
        numerotermos = numerotermos + 1
        if primeirotermo == (primeirotermo + (razao*(numerotermos-1))):
            print(primeirotermo)
        else:
            pa = (primeirotermo + (numerotermos*razao))
            print(pa, end=(","))
