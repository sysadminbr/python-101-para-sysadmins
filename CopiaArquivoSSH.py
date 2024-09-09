# para usar o ssh, é necessário usar a biblioteca paramiko
# pip install paramiko

import paramiko
import os

# detalhes da conexão
hostname = "10.141.65.51"
port = 22
username = "user1"
password = "password1"

# caminho do arquivo para transferir
arquivo_local = "e-book.pdf"
arquivo_remoto = "/home/user1/e-book.pdf"

try:
    # inicializa o cliente ssh
    # permite conectar em um host que ainda não temos a chave de host dele
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connecta
    ssh.connect(hostname, port, username, password)

    # abre o modo de transferencia sftp (secure ftp)
    sftp = ssh.open_sftp()
    
    # copia o arquivo local para o host remoto
    sftp.put(arquivo_local, arquivo_remoto)
    print(f"File '{os.path.basename(arquivo_local)}' copiado com sucesso para '{arquivo_remoto}'.")

    # fecha as conexões sftp e ssh nessa ordem
    sftp.close()
    ssh.close()

except Exception as e:
    print(f"ocorreu o seguinte erro: {e}")


