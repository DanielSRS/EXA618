import requests

r = requests.get("https://github.com/DanielSRS")
print(r.status_code)
print(r.headers)
print(r.content)
