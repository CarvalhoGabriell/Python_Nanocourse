import platform
from datetime import datetime
import getpass

print("Nome da máquina..........: ", platform.node())
print("Arquitetura do sitema....: ", platform.architecture())
print("Sistema Operacional......: ", platform.system())
print("Versão do SO.............: ", platform.release())
print("Prpcessador da máquina...: ", platform.processor())
print("Versão do Python atual...: ", platform.python_version())

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")

print("O ano atual......:", datetime.now().year)
print("O mês atual......:", datetime.now().month)
print("Hoje é dia.......:", datetime.now().day)
print("No momento são......:", datetime.now().hour, "horas")
print("O mês atual......:", datetime.now().minute, "minuto(s)")

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")

info_user = input("Informe seu usuário de acesso: ").upper()

user = getpass.getuser()
password = getpass.getpass("Digite sua senha: ")

if info_user != user and password != "gabiru9090":
    print("Voce nao tem acesso ao sistema....")
else:
    print("Voce foi Logado com sucesso!!!")