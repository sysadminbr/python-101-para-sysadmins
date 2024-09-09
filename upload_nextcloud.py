import requests
import os

pasta_para_upload = r'C:\Users\Luciano\Documents\tmp\to_upload'

for basedir, dirs, files in os.walk(pasta_para_upload):
    for cur_dir in dirs:
        dir_atual = basedir + '\\' + cur_dir
        dir_remoto = dir_atual.replace(pasta_para_upload, "")
        dir_remoto = dir_remoto.replace("\\", "/")
        print(f"criando a pasta {dir_atual} como {dir_remoto}")
        requests.request(
            method='MKCOL',
            url=f'http://192.168.100.145/remote.php/dav/files/admin/REDE/' + dir_remoto,
            auth=('admin', 'admin')
        )


    for cur_file in files:
        arquivo_atual = basedir + '\\' + cur_file
        arquivo_remoto = arquivo_atual.replace(pasta_para_upload, "")
        arquivo_remoto = arquivo_remoto.replace("\\", "/")
        print(f'enviando o arquivo {arquivo_atual}')
        with open(arquivo_atual, "rb") as arquivo_binario_atual:
            r = requests.put(
                url=f'http://192.168.100.145/remote.php/dav/files/admin/REDE/' + arquivo_remoto,
                auth=('admin', 'admin'),
                data=arquivo_binario_atual
            )
            if r.ok:
                print(f'arquivo enviado com sucesso!')
            else:
                print(f'erro ao enviar o arquivo!')




"""
with open("programa1.py","rb") as arquivo_upload:
    requests.put(
        url='http://192.168.100.145/remote.php/dav/files/admin/programa1.txt',
        auth=('admin','admin'),
        data=arquivo_upload
    )
"""