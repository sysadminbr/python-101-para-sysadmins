import  socket
from threading import Thread

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(('192.168.100.134', 5000))
print("CONVERSANDO COM O CICLANO")
print("ENVIE QUALQUER COISA PARA COMECAR A CONVERSA")

while True:
    entrada = input("> ")
    cliente.sendall(entrada.encode())
    recebido = cliente.recv(1024)
    print(f"ciclano disse: {recebido.decode()}")
    if recebido == "sair":
        break
