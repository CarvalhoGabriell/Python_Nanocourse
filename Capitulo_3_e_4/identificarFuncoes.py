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




# def perguntar():
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
