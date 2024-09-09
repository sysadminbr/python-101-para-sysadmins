# define o mapa de rotação de caracteres. 
# ex.: 3 caracteres acima do original
mapa = {
    'a': 'd',
    'b': 'e',
    'c': 'f',
    'd': 'g',
    'e': 'h',
    'f': 'i',
    'g': 'j',
    'h': 'k',
    'i': 'l',
    'j': 'm',
    'k': 'n',
    'l': 'o',
    'm': 'p',
    'n': 'q',
    'o': 'r',
    'p': 's',
    'q': 't',
    'r': 'u',
    's': 'v',
    't': 'w',
    'u': 'x',
    'v': 'y',
    'w': 'z',
    'x': 'a',
    'y': 'b',
    'z': 'c'
}

texto_puro = "oi, sou eu de novo!"

cifrado = []
for caractere in texto_puro:
    if not caractere in mapa.keys():
        cifrado += caractere
        continue
    else:
        cifrado += mapa[caractere]

print(f'mensagem cifrada: {''.join(cifrado)}')



