# define o mapa de rotação de caracteres. 
# ex.: 3 caracteres abaixo do original (reverso para decifrar)
mapa = {
    'd': 'a',
    'e': 'b',
    'f': 'c',
    'g': 'd',
    'h': 'e',
    'i': 'f',
    'j': 'g',
    'k': 'h',
    'l': 'i',
    'm': 'j',
    'n': 'k',
    'o': 'l',
    'p': 'm',
    'q': 'n',
    'r': 'o',
    's': 'p',
    't': 'q',
    'u': 'r',
    'v': 's',
    'w': 't',
    'x': 'u',
    'y': 'v',
    'z': 'w',
    'a': 'x',
    'b': 'y',
    'z': 'c'
}


texto_cifrado = "rl, vrx hx gh qryr!"

texto_puro = []
for caractere in texto_cifrado:
    if not caractere in mapa.keys():
        texto_puro += caractere
        continue
    else:
        texto_puro += mapa[caractere]

print(f'mensagem decifrada: {''.join(texto_puro)}')
