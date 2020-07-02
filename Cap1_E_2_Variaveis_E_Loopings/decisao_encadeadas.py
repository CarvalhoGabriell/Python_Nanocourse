nome=input("Digite o nome aqui: ")
idade=int(input("Digite a idade: "))
doenca_infectocontagiosa=input("Suspeita de doenca infectocontagiosa?").upper()

while doenca_infectocontagiosa!="SIM" and doenca_infectocontagiosa!= "NAO":
    print("Digite SIM ou NAO.")
    doenca_infectocontagiosa = input("Suspeita de doenca infectocontagiosa?").upper()
if doenca_infectocontagiosa=="SIM":
    print("Encaminhe o paciente para sala AMARELA")
else:
    print("Encaminhe o paciente para sala BRANCA")



if idade>=65:
    print("Paciente COM prioridade")
else:
    genero = input("Informe seu genêro: ").upper()
    if genero=="FEMININO" and idade> 10:
       gravidez=input("A paciente está grávidda? ").upper()
       if gravidez=="SIM":
           print("Paciente COM prioridade!!!")
       else:
           print("Paciente SEM prioridade")
    else:
        print("Paciente SEM prioridade")