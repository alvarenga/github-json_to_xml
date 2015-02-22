from pip._vendor import requests
import json
import xmltodict

s = requests.get('https://api.github.com/users/alvarenga')
# print (json.dumps(res_json.text,indent=1))

print (s.text)
# Converter json para dict
x = json.loads(s.text)

print (x)

# print(xmltodict.unparse({'nome': 'Renzo'}))
print(xmltodict.unparse(x))
