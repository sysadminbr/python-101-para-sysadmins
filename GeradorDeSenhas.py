import random
from string import ascii_letters,digits
import sys

dicionario = ascii_letters + digits

numero_de_caracteres = sys.argv[1]

senha_final = []
for i in range(int(numero_de_caracteres)):
    senha_final.append(random.choice(dicionario))

print(f'Sua senha gerada eh: {"".join(senha_final)}')


