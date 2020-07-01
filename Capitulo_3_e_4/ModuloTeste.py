from Pacote_funcoes.identificarFuncoes import *

listaEmpresa = []
print("Preenchendo a lista")
preecherInventario(listaEmpresa)
print("EXIBINDO OS ITENS DA LISTA\n")
exibirInventario(listaEmpresa)

print("BUSCANDO ITEM DO INVENTARIO")
buscarEquipamento(listaEmpresa)

print("ALTERANDO VALOR DO EQUIPAMENTO")
depreciacaoEquipamento(listaEmpresa, 30)

print("EXCLUINDO ITEM DO INVENTARIO")
excluirEquipamento(listaEmpresa)

print("RESUMINDO VALORES DO INVENTARIO")
resumirValores(listaEmpresa)