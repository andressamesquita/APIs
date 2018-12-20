# -*- coding: utf-8 -*-
import requests
city = input('Cidade: ')     #'London'
key = input('Chave: ')       #'c20a21ddb76e3c3d5fe17c18c7dfb852'
url =('http://api.openweathermap.org/data/2.5/weather?q=%s,uk&APPID=%s' % (city, key))
response = requests.get(url).json()

print(response)
