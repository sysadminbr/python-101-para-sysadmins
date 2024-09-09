# instalar a biblioteca cryptography
# pip install cryptography

# Fernet abstrai a complexidade de lidar com cifras diretamente
from cryptography.fernet import Fernet

# gera uma senha para criptografia
with open("secret.key", "rb") as key_file:
    key = key_file.read()
fernet = Fernet(key)

# abre o arquivo para ser descriptografado
with open('e-book_criptografado.pdf', 'rb') as file:
    file_data = file.read()

# descriptografa o arquivo
decrypted_data = fernet.decrypt(file_data)

# grava o conteúdo descriptografado em um novo arquivo de saída
with open('e-book.pdf', 'wb') as decrypted_file:
    decrypted_file.write(decrypted_data)

print("arquivo descriptografado com sucesso!")