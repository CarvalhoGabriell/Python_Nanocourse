import socket
resposta = "SIM"
while resposta == "SIM":
    url =input("Informe aqui sua URL: ")
    ip=socket.gethostbyname(url)
    print("O IP referente a URL informada é: ", ip)
    resposta=input("Digite <SIM> para continuar: ").upper()