equipamentos = []
valores = []
Ids = []
departamentos = []
marcas = []

res = "SIM"
while res == "SIM":
    equipamentos.append(input("Qual o nome do equipamento? "))
    marcas.append(input("Qual a marca dele? "))
    Ids.append(int(input("Digite o ID do produto para identica-lo: ")))
    valores.append(float(input("Qual o valor do equipamento? ")))
    departamentos.append(input("Qual o departamento ele pertence? "))
    res = input("Digite \"SIM\" para continuar adicionando elementos.").upper()

for indice in range(0, len(equipamentos)):
    print("\nEquipamentos:...: ", (indice + 1))
    print("nome:...: ", equipamentos[indice])
    print("ID.....: ", Ids[indice])
    print("valor:...: R$ ", valores[indice])
    print("Departamento:...:", departamentos[indice])

busca = input("\nDigite qual equipamento deseja buscar: ")
for indice in range(0, len(equipamentos)):
    if busca == equipamentos[indice]:
        print("Marca:...", marcas[indice])
        print("Numero de identificação ID:...",Ids[indice])
        print("Departamento:...", departamentos[indice])
        print("Valor:...",valores[indice])

depreciacao = input("\nDigite nome do equipamento que será depreciado: ")
for indice in range(0, len(equipamentos)):
    if depreciacao == equipamentos[indice]:
        print("Valor antigo do equipamento", valores[indice])
        valores[indice] = valores[indice] * 0.5
        print("Valor com o novo reajuste", valores[indice])

id = input("\nInforme o ID do equipamento que deseja deletar: ")
for indice in range(0, len(equipamentos)):
    if id[indice] == Ids:
        del departamentos[indice]
        del marcas[indice]
        del Ids[indice]
        del valores[indice]
        break

## PRINT DA LISTA AGORA SEM OS PRODUTOS QUE FORAM DELETADOS
for indice in range(0, len(equipamentos)):
        print("\nEquipamento..: ", (indice + 1))
        print("Nome.........: ", equipamentos[indice])
        print("Valor........: ", valores[indice])
        print("Serial.......: ", Ids[indice])
        print("Departamento.: ", departamentos[indice])

# ##PERCORRER UMA LISTA DE SINGULAR, OU SEJA , APENAS PASSANDO O NOME DESSA LISTA
# for artigos in equipamentos:
#     print("Produtos: ", artigos)
