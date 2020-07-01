usuarios = {}
# Dentro dos "" existem as chaves e logo apos os ":" existem uma lista com valores atribuidos para essa chave.
usuarios = {
    "gabriel": ["23/12/1999", "lab_livre", "Gabriel Carvalho"],
    "sindy": ["14/02/2019", "wow_lab", "Syndyca Araujo"],
    "felipe": ["18/05/2018", "acesso_remoto", "Felipe Carvalho"],
    "felipe": ["03/07/2011", "primeiro_acesso", "Felipe Carvalho Fernandes"]
}
print(usuarios, "\n")

# Criando dicionários de forma singular, assim fazendo de forma em OBJETO a OBJETO
usuarios["cleybson"] = ["27/06/2018", "lab_01", "Cleybson Roger"]
usuarios["Jonas"] = ["04/08/2019", "primeiro_acesso", "Jonas Khanvald"]
print(usuarios)

# Metodo GET serve poara retornar os valores passados entre os "".
print(usuarios.get("gabriel"))

