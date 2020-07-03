baseDdaods = []

with open("iris.data", "r") as arquivo:
    for info in arquivo.readlines():
        baseDdaods.append(info.split(","))

print(baseDdaods)

print(baseDdaods[0][4])