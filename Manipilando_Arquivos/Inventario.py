from Pacote_funcoes.identificarFuncoes import *

inventario = {}

opcao = mostrarMenu()
while 0 < opcao < 4:
    if opcao == 1:
        registarAtivo(inventario)
    elif opcao == 2:
        persistir(inventario)
    elif opcao == 3:
        resultado = lendoExibindo()
        for linha in resultado:
            lista = linha.split(";")
            print("DATA..........:", lista[1])
            print("DESCRIÇÃO.....:", lista[2])
            print("DEPARTAMENTO..:", lista[3])
    opcao = mostrarMenu()
