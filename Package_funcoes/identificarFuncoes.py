def preecherInventario(lista):
    resp = "SIM"
    while resp == "SIM":
        equipamento = [input("Nome do Equipamento: "),
                       float(input("Valor: ")),
                       int(input("Numero do ID: ")),
                       input("Departamento: ")]
        lista.append(equipamento)
        resp = input("Digite \"SIM\" para continuar.").upper()

def exibirInventario(lista):
    for elemento in lista:
        print("INVENTARIO DA EMPRESA \n")
        print("NOME....: ", elemento[0])
        print("VALOR....: ", elemento[1])
        print("ID....: ", elemento[2])
        print("DEPARTAMENTO....: ", elemento[3], "\n")

def buscarEquipamento(lista):
    busca = input("\nDigite qual equipamento deseja buscar: ").upper()
    for elemento in lista:
        if busca == elemento[0]:
            print("Numero de identificação ID:...", elemento[2])
            print("Departamento:...", elemento[3])
            print("Valor:...", elemento[1])

def depreciacaoEquipamento(lista, porcentagem):
    depreciacao = input("\nDigite nome do equipamento que será depreciado: ").upper()
    for elemento in lista:
        if depreciacao == elemento[0]:
            print("Valor antigo do equipamento", elemento[1])
            elemento[1] = elemento[1] * (1-porcentagem/100)
            print("Valor com o novo reajuste", elemento[1])

def excluirEquipamento(lista):
    id = int(input("\nInforme o ID do equipamento que deseja deletar: "))
    for elemento in lista:
        if elemento[2] == id:
            lista.remove(elemento)
            print("Equipamento", elemento, " foi Excluido com sucesso!!!")
    return "Itens excluidos com sucesso!!!"


def resumirValores(lista):
    valores = [],
    for elemento in lista:
        valores.append(elemento[1])
        if len(valores) > 0:
            print("O equipamento mais caro custa: ", max(valores))
            print("O equipamento mais barato custa: ", min(valores))
            print("O total de equipamentos: ", sum(valores))





## def perguntar():
#     return input("O que deseja realizar?\n" +
#                  "<I> - Para inserir um usuário\n" +
#                  "<D> - Para deletar um usuário\n" +
#                  "<P> - Para pesquisar um usuário\n" +
#                  "<L> - Para listar os usuários: ").upper()
#
#
#
# def inserir(dicionario):
#     dicionario[input("Digite seu login: ").upper()] = [input("Digite seu nome: ").upper(),
#                                                        input("Digite seu a última data de acesso"),
#                                                        input("Digite o último local de acesso").upper()]
