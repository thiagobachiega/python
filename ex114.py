import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.youtube.com')
except urllib.error.URLError:
    print('O site não está acessivel!')
else:
    print('Consegui acessar o site')
