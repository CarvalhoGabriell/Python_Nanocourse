from Pacote_funcoes.identificarFuncoes import *

usuarios = {}
opcao = menuOpcao()
while opcao == "I" or opcao == "D" or opcao == "L" or opcao == "P":
    if opcao =="I":
        inserirUsers(usuarios)
        print("Usuário inserido com sucesso!!!\n")
    if opcao == "D":
        deletarUsers(usuarios, input("Qual usuário deseja deletar? ").upper())
    if opcao == "L":
        listarUser(usuarios)
    if opcao == "P":
        pesquisaUsers(usuarios, input("Qual login deseja pesquisar? ").upper())
    opcao = menuOpcao()

