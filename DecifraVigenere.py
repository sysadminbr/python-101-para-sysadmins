from string import ascii_lowercase


chave_segredo = "oponopono"
texto_cifrado = "qpgfsio r dzpbrhp seo apgfo!"

texto_puro = []
index_atual_chave = 0
for caractere in texto_cifrado:
    if not caractere in ascii_lowercase:
        texto_puro += caractere
        continue
    else:
        indice_rotacao = ascii_lowercase.index(chave_segredo[index_atual_chave])
        soma_rotacao = ascii_lowercase.index(caractere) - indice_rotacao
        caractere_resultante = ascii_lowercase[ soma_rotacao % len(ascii_lowercase) ]
        texto_puro += caractere_resultante
        index_atual_chave +=1
        if index_atual_chave == len(chave_segredo):
            index_atual_chave = 0

print(f'texto decifrado: {''.join(texto_puro)}')
