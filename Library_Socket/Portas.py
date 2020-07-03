import socket

print("Porta de Dominio....:", socket.getservbyname("domain"))
print("Porta do HTTP....:", socket.getservbyname("http"))
print("Porta do FTP....:", socket.getservbyname("ftp"))