nome = input("Digite aqui seu nome: ")
idade = int(input("Informe sua idade: "))
doenca_infeciosa = input("Possui algum sintoma? ").upper()


if idade >= 65:
    print("O usuario: ", nome, "possui atendimento prioritario")
elif doenca_infeciosa=="SIM":
    print("O paciente",nome, "Deve ser levado para a sala \"VERMELHA\" ")
elif doenca_infeciosa=="NAO":
    print("O paciente deve ser encaminhado para a sala \"BRANCA\" ")
else:
    print(" O usuario: ", nome, "nao possui prioridade no atendimento")