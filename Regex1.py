# instalar a biblioteca: pip install requests
import requests
import re

# acessa o site e baixa a página com informações do meu IP
resposta = requests.get(
    url="https://ifconfig.me/",
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'}
)


ip = re.findall(r'<td\sid="ip_address_cell"><strong id="ip_address">([0-9a-z\:]+)<\/strong><\/td>', resposta.text)

print(f'o meu IP neste momento é: {ip[0]}')