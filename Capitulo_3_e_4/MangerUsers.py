from Pacote_funcoes.identificarFuncoes import *

usuarios = {}

opcao = perguntar()

while opcao == "I" or opcao == "D" or opcao == "L" or opcao == "P":
    if opcao =="I":
        inserirUsuario(usuarios)
opcao = perguntar()

