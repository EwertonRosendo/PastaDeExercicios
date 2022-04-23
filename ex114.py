'''import requests

try:
    requests.get("http://youtube.com.br//")

except:
    print("deu merda")

else:
    print("deu bom")'''

import urllib
import urllib.request

try:
    site = urllib.request.urlopen("http://youtube.com//")

except urllib.error.URLError:
    print("site não acessivel")

else:
    print("Site acessivel")
    print(site.read())