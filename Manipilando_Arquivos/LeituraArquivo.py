with open("texto teste.txt", "r") as test:
    conteudo = test.readlines()
print("Conteudo do arquivo: ", conteudo)
print("O tipo de dado do conteudo: ", type(conteudo))

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")

with open("Aquivo de texto teste.txt", "r") as directory:
    conteudo = directory.read()
print("Conteudo do arquivo: ", conteudo)

