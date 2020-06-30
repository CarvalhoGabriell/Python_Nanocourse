from PythonAulas.Capitulo_3_e_4.funcoes import *

usuarios = {}

opcao = perguntar()

while opcao == "I" or opcao == "D" or opcao == "L" or opcao == "P":
    if opcao =="I":
        inserir(usuarios)
opcao = perguntar()

