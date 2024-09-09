from urllib3 import request

webclient = request("GET", "http://iconfig.me/ipv4")
print(webclient.data)