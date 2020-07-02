from Pacote_funcoes.identificarFuncoes import *

inventario = {}

opcao = mostrarMenu()
while 0 < opcao < 4:
    if opcao == 1:
        resp = "SIM"
        while resp == "SIM":
            registarAtivo(inventario)
    elif opcao == 2:
        persistir(inventario)
    elif opcao == 3:
        lendoExibindo()
    opcao = mostrarMenu()
