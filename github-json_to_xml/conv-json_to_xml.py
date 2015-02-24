from pip._vendor import requests
import json
import xmltodict

s = requests.get('https://api.github.com/users/renzon')

# Converter json para dict
x = {}
x['wg'] = json.loads(s.text)
y = xmltodict.unparse(x, pretty=True)
print(y)