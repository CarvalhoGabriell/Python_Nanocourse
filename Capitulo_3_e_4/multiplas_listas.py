# produtos = []
# marcas = []
# Ids = []
# valores = []
# departamentos = []
#
# res = "SIM"
# while res == "SIM":
#     produtos.append(input("Qual o nome do produto? "))
#     marcas.append(input("Qual a marca dele? "))
#     Ids.append(int(input("Digite o ID do produto para identica-lo: ")))
#     valores.append(float(input("Quanto custa? ")))
#     departamentos.append(input("Qual o departamento ele pertence? "))
#     res = input("Digite \"SIM\" para continuar adicionando elementos.").upper()
#
# for indice in range(0, len(produtos)):
#     print("\nEquipamentos:... ", (indice + 1))
#     print("nome:... ", produtos[indice])
#     print("ID.....", Ids[indice])
#     print("valor:... R$ ", valores[indice])
#     print("Departamento:... ", departamentos[indice])
#
#
# busca = input("\nDigite o nome do produto que deseja buscar: ")
# for indice in range(0, len(produtos)):
#     if busca == produtos[indice]:
#         print("Marca:...", marcas[indice])
#         print("Numero de identificação ID:...",Ids[indice])
#         print("Departamento:...", departamentos[indice])
#         print("Valor:...",valores[indice])
#
# depreciacao = input("\nDigite nome do produto que será depreciado: ")
# for indice in range(0, len(produtos)):
#     if depreciacao == produtos[indice]:
#         print("Valor antigo do produto", valores[indice])
#         valores[indice] = valores[indice] * 0.5
#         print("Valor novo com o reajuste", valores[indice])
#
#
# id = input("\nInforme o ID do produto que deseja deletar: ")
# for indice in range(0, len(produtos)):
#     if id[indice] == Ids:
#         del departamentos[indice]
#         del marcas[indice]
#         del Ids[indice]
#         del valores[indice]
#         break
#
# for indice in range(0, len(produtos)):
#         print("\nEquipamento..: ", (indice + 1))
#         print("Nome.........: ", produtos[indice])
#         print("Valor........: ", valores[indice])
#         print("Serial.......: ", Ids[indice])
#         print("Departamento.: ", departamentos[indice])


## ACESSAR UM LISTA INTERNA E SABER O VALOR MÁXIMO , MENOR E A SOMA.

# valores=[]
# for elemento in  produtos: #(LISTA EXTERNA )
#     valores.append(elemento[1])
#     if len(valores)>0:
#     print("O equipamento mais caro custa: ", max(valores))
#     print("O equipamento mais barato custa: ", min(valores))
#     print("Ototal de equipamentos é de: ", sum(valores))


# PERCORRER UMA LISTA DE SINGULAR, OU SEJA , APENAS PASSANDO O NOME DESSA LISTA
# for artigos in produtos:
# #     print("Produtos: ", artigos)

num = Double(522.20)
print(num)