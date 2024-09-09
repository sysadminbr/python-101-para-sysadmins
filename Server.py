import socket

# cria o socket, registra a porta no windows, e sinaliza que pode receber conexões
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 5555))
server_socket.listen()

# aguarda uma nova conexão, envia bem vindo, e encerra
client_socket, client_addr = server_socket.accept()
dados = client_socket.recv(1024)
client_socket.sendall(dados)
client_socket.close()






