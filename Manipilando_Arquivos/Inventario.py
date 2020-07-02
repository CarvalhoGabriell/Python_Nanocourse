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
            separacao = linha[linha.find(";")+1:-1]
            data = separacao[0:separacao.find(";")]
            separacao = separacao[separacao.find(";")+1:-1]
            descricao = separacao[0:separacao.find(";")]
            departamento = linha[linha.rfind(";")+1:-1]
            print("DATA..........:", data)
            print("DESCRIÇÃO.....:", descricao)
            print("DEPARTAMENTO..:", departamento)
    opcao = mostrarMenu()
