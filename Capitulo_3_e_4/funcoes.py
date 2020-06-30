def perguntar():
    return input("O que deseja realizar?\n" +
                 "<I> - Para inserir um usuário\n" +
                 "<D> - Para deletar um usuário\n" +
                 "<P> - Para pesquisar um usuário\n" +
                 "<L> - Para listar os usuários: ").upper()



def inserir(dicionario):
    dicionario[input("Digite seu login: ").upper()] = [input("Digite seu nome: ").upper(),
                                                       input("Digite seu a última data de acesso"),
                                                       input("Digite o último local de acesso").upper()]
