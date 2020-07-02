chaves_acess = {}
resp = "SIM"

while resp == "SIM":
    chaves_acess[(input("Informe seu email: "), int(input("Informe sua senha: ")))] = input("Nome do seu Login: ")
    resp = input("Digite <SIM> para continuar!!!").upper()

print("EXIBINDO AS CHAVES DE ACESSO\n")
for valores in chaves_acess.keys():
    print("Email...:", valores[0])
    print("Senha...:", valores[1])

print("EXIBINDO O NOME DO LOGIN\n")
#pesquisa = int(input("Informe sua <SENHA>: "))
# for senha, user in chaves_acess.items():
#     print("EXIBINDO NOME DO USUÁRIO PESQUISADO")
#     if senha[1] == pesquisa:
#         print(user)

# PESQUISANDO USUARIO TANTO PELA SENHA COMO PELO EMAIL

pesquisa = input("Informe seu <EMAIL>: ")
for email, user in chaves_acess.items():
    print("EXIBINDO NOME DO USUÁRIO PESQUISADO\n")
    if email[0] == pesquisa:
        print("Usuário de Login: ", user)
        print("Senha: ********")
