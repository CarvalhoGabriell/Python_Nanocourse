from socket import *

servidor="127.0.0.1"
porta=43210

msg =bytes(input("Digite algo aqui: "), 'utf-8')  # <BYTES> para converte em bytes é necessario dois parametros (conteudo, padrão)
obj_socket = socket(AF_INET, SOCK_STREAM)
obj_socket.connect((servidor, porta))
obj_socket.send(msg)

resposta =obj_socket.recv(1024)
print("Recebemos: ", resposta)
obj_socket.close()