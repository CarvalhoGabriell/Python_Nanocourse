inventario = []
resp = "SIM"

while resp == "SIM":
    equipamento = [input("Nome do Equipamento: "),
                   float(input("Valor: ")),
                   int(input("Numero do ID: ")),
                   input("Departamento: ")]
    inventario.append(equipamento)
    resp =input("Digite \"SIM\" para continuar.").upper()

for elemento in inventario:
    print("INVENTARIO DA EMPRESA \n")
    print("NOME....: ", elemento[0])
    print("VALOR....: ", elemento[1])
    print("ID....: ", elemento[2])
    print("DEPARTAMENTO....: ", elemento[3], "\n")


# # ACESSAR UM LISTA INTERNA E SABER O VALOR M�XIMO , MENOR E A SOMA.
valores=[],
for elemento in inventario: #(LISTA EXTERNA )
    valores.append(elemento[1])
    if len(valores)>0:
        print("O equipamento mais caro custa: ", max(valores))
        print("O equipamento mais barato custa: ", min(valores))
        print("O total de equipamentos � de: ", sum(valores))
