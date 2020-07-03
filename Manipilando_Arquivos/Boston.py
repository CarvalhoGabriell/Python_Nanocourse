# indicadores = {}

with open("economic-indicators.csv", "r") as boston:
    total_voos = 0
    maior_transito = 0
    total_passengers = 0
    maior_media_diaria = 0
    ano_usuario = input("Qual ano deseja pesquisar? ")
    for linhas in boston.readlines()[1:-1]:
        lista = linhas.split(",")
        total_voos = total_voos+float(linhas[3])
        if float(lista[2]) > float(maior_transito):
            maior_transito = lista[2]
            ano = lista[0]
            mes = lista[1]
        if ano_usuario == lista[0]:
            total_passengers = total_passengers + float(lista[2])
            if float(lista[5]) > float(maior_media_diaria):
                maior_media_diaria = lista[5]
                mes_maior_diaria = lista[1]
    print("O total de voos internacionais é de: ", total_voos)
    print("O mês/ano de maior movimento no aeroporto de Logan foi: ", str(mes), "/", str(ano))
    print("O total de passageiros do ano ", ano_usuario, " foi de:", total_passengers)
    print("O mês do ano de", ano_usuario, "com maior média diária de Hotel foi o mês", mes_maior_diaria)