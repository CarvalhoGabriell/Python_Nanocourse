num = int(input("Digite um numero para gerar sua tabuada:"))
print("Veja abaixo a tabuada de {}".format(num))

for valor in range(0, 11, 1):
    print("{} X {} = {}".format(num, valor, num * valor))
