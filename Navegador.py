import urllib
import urllib.request
import json

requests = urllib.request.Request(
    url="https://api.chucknorris.io/jokes/random", 
    headers={'User-Agent': 'CURL'}
)


web = urllib.request.urlopen(requests)
resposta_web = json.load(web)

print(resposta_web["value"])
