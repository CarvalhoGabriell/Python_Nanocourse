inventario = []
res = "inserir"

while res == "inserir":
    inventario.append(input("Qual o nome do produto? "))
    inventario.append(input("Qual de qual marca?" ))
    inventario.append(input("Qual o valor do produto? "))
    inventario.append(input("Qual o código do produto? "))
    res = input("Digite \"inserir\" para continuar: ")

for elementos in inventario:
    print(elementos)
    print("------------------------------------------")