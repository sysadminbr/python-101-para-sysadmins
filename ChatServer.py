import socket
from threading import Thread
import select


socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_servidor.bind(('0.0.0.0', 5000))
socket_servidor.listen(1)
print("SERVIDOR INICIADO E AGUARDANDO CONEXOES...")

conexao_cliente, addr_cliente = socket_servidor.accept()
print("CONVERSANDO COM O FULANO")
#conexao_cliente.sendall(b"OLA, VOCE ESTA CONVERSEANDO COM O CICLAO.")

while True:
    recebido = conexao_cliente.recv(1024)
    print(f"Fulano disse: {recebido.decode()}")
    if recebido == b"sair":
            break
    if input is not None:
        texto_enviar = input("> ")
        conexao_cliente.sendall(texto_enviar.encode())
    
    
    




