inventario = []
resp = "SIM"

while resp == "SIM":
    equipamento = [input("Nome do Equipamento: ").upper(),
                   float(input("Valor: ")),
                   int(input("Numero do ID: ")),
                   input("Departamento: ").upper()]
    inventario.append(equipamento)
    resp =input("Digite \"SIM\" para continuar.").upper()

## EXIBIR DADIS DI INVENTARIO
for elemento in inventario:
    print("INVENTARIO DA EMPRESA \n")
    print("NOME....: ", elemento[0])
    print("VALOR....: ", elemento[1])
    print("ID....: ", elemento[2])
    print("DEPARTAMENTO....: ", elemento[3], "\n")

## BUSCAR UM ITEM DO INVENTARIO
busca = input("\nDigite qual equipamento deseja buscar: ").upper()
for elemento in inventario:
    if busca == elemento[0]:
        print("Numero de identificação ID:...", elemento[2])
        print("Departamento:...", elemento[3])
        print("Valor:...",elemento[1])

#DEPRECIAR PREÇO DO EQUIPAMENTO
depreciacao = input("\nDigite nome do equipamento que será depreciado: ").upper()
for elemento in inventario:
    if depreciacao == elemento[0]:
        print("Valor antigo do equipamento", elemento[1])
        elemento[1] = elemento[1] * 0.8
        print("Valor com o novo reajuste", elemento[1])

## EXCLUIR EQUIPAMENTO DO INVENTARIO
id = int(input("\nInforme o ID do equipamento que deseja deletar: "))
for elemento in inventario:
    if elemento[2] == id:
        inventario.remove(elemento)

# ACESSAR UM LISTA INTERNA E SABER O VALOR MAXIMO , MENOR E A SOMA.
## RESUMO DE VALORES DO IVENTARIO
valores=[],
for elemento in inventario:
    valores.append(elemento[1])
    if len(valores)>0:
        print("O equipamento mais caro custa: ", max(valores))
        print("O equipamento mais barato custa: ", min(valores))
        print("O total de equipamentos: ", sum(valores))
