with open("texto teste.txt", "r") as test:
    cont = test.readlines()

print("Conteudo do arquivo: ", cont)
print("O tipo de dado do conteudo: ", type(cont))