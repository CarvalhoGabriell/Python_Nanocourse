usuarios = {}  # dicionarios
resp = "SIM"
emails = []  # listas

while resp == "SIM":
    emails.append(input("Informe seu email: ").lower())
    resp = input("Digite <SIM> para continuar inserindo <EMAILS>\n").upper()
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

tupla = list(enumerate(emails))  # Tuplas
print(tupla, "\n")

for chave in range(0, len(tupla)):
    print("Email...: ", tupla[chave][1], ",", tupla[chave][0])
    usuarios[tupla[chave]]= [input("Digite seu nome: "), input("Digite seu nível de acesso: ").upper()]
    # Chave do <DICIONARIO>  // <VALOR> da chave do <DICIONARIO>

for chave, dado in usuarios.items():
    print("Usuario..: ", chave[0])
    print("Email....: ", chave[1])
    print("Nome.....: ", dado[0])
    print("Nível....: ", dado[1])
