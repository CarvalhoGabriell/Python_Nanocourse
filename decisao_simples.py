nome = input("Digite aqui seu nome: ")
idade = int(input("Informe sua idade: "))
doenca_infeciosa = input("Possui algum sintoma? ").upper()


if idade >= 65:
    print("O usuario: ", nome, "possui atendimento prioritario")
elif doenca_infeciosa=="SIM":
    print("O paciente",nome, " Deve ser levado para a sala de espera especifica")
else:
    print(" O usuario: ", nome, "nao possui prioridade no atendimento")