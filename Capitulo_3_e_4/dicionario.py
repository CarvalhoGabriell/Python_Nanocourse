usuarios = {}

usuarios = {
    "gabriel": ["23/12/1999", "lab_livre", "Gabriel Carvalho"],
    "sindy": ["14/02/2019", "wow_lab", "Syndyca Araujo"],
    "felipe": ["18/05/2018", "acesso_remoto", "Felipe Carvalho"]
}
print(usuarios)

usuarios["cleybson"] = ["27/06/2018", "lab_01", "Cleybson Roger"]
print(usuarios)

print(usuarios.get("gabriel"))

