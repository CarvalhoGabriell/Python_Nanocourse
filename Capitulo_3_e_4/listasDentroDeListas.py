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