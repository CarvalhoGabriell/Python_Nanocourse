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

# # ACESSAR UM LISTA INTERNA E SABER O VALOR MÁXIMO , MENOR E A SOMA.

valores=[]
for elemento in inventario: #(LISTA EXTERNA )
    valores.append(elemento[1])
    if len(valores)>0:
        print("O equipamento mais caro custa: ", max(valores))
        print("O equipamento mais barato custa: ", min(valores))
        print("O total de equipamentos é de: ", sum(valores))

