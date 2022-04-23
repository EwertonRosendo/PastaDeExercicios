import requests

try:
    requests.get("http://youtube.com.br//")

except:
    print("deu merda")

else:
    print("deu bom")