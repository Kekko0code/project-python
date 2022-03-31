import requests as rq
response = rq.get("https://www.animesaturn.it/")
#print("status site: " , response.status_code)
if response.ok:
    print("tutto ok")
else:
    print("non tutto ok")