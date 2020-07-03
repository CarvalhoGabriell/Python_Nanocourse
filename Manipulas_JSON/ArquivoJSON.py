from Pacote_funcoes.identificarFuncoes import *

inventario = lerArquivos("inventario_json.json")
opcao= menuJson()
while opcao > 0 and opcao < 3:
    if opcao == 1:
        registarAtivoNoJson(inventario, "inventario_json.json")
    elif opcao == 2:
        exibirInformacao("inventario_json.json")
    opcao = menuJson()
    print("PROCESSO FINALIZADO!!!!")
