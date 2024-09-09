import socket

# cria o socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # tenta conectar, enviar "PING", receber texto e imprimir na tela
    client.connect(("localhost", 5555))
    print(f'conectado com sucesso!')
    client.sendall(b"PING!")
    print(f'enviei PING!')
    dados = client.recv(1024)
    print(f'recebi do servidor: {dados}')
except Exception as e:
    # se algo der errado...
    print(f'erro ao conectar no servidor.\n{str(e)}')

client.close()