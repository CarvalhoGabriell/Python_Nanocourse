inventario = []
res = "INSERIR"

while res == "INSERIR":
    inventario.append(input("Qual o nome do produto? "))
    inventario.append(input("Qual de qual marca?" ))
    inventario.append(float(input("Qual o valor do produto? ")))
    inventario.append(input("Qual o código do produto? "))
    res = input("Digite \"INSERIR\" para continuar: ").upper()

for elementos in inventario:
    print(elementos)
    print("------------------------------------------")

