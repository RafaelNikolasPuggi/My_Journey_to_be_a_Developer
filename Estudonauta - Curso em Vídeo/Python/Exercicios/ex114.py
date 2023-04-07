import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('Não foi possivel conectar ao site no momento.')
else:
    print('O site está conectado.')
    print(site.read())