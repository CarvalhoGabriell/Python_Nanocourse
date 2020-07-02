usuarios = {}
emails = ["gagabiru@io.com", "zikaBala@hot.com"]

tupla = list(enumerate(emails))
# print(tupla)

for chave in range(0, len(tupla)):
    print("Email: ", tupla[chave][1])
    usuarios[tupla[chave]] = [input("Informe seu nome: "), input("Digite seu nível: ").upper()]


for chave, dado in usuarios.items():  # O metodo ITENS , sempre retorna uma TUPLA
    print("Usuário:............ ", chave[0])
    print("Email:.............. ", chave[1])
    print("Nome:............... ", dado[0])
    print("Nível:.............. ", dado[1])