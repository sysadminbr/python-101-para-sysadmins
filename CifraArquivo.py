# instalar a biblioteca cryptography
# pip install cryptography

# Fernet abstrai a complexidade de lidar com cifras diretamente
from cryptography.fernet import Fernet

# gera uma senha para criptografia
key = Fernet.generate_key()
fernet = Fernet(key)

# salva a chave em um arquivo para posterior uso.
with open('secret.key', 'wb') as key_file:
    key_file.write(key)

# abre o arquivo para ser criptografado
with open('e-book.pdf', 'rb') as file:
    file_data = file.read()

# criptografa o arquivo
encrypted_data = fernet.encrypt(file_data)

# grava o conteúdo criptografado em um novo arquivo de saída
with open('e-book_criptografado.pdf', 'wb') as encrypted_file:
    encrypted_file.write(encrypted_data)

print("arquivo criptografado com sucesso!")