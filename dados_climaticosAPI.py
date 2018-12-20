# -*- coding: utf-8 -*-
import requests
city = input('Cidade: ')     
key = input('Chave: ')      
url =('http://api.openweathermap.org/data/2.5/weather?q=%s,uk&APPID=%s' % (city, key))
response = requests.get(url).json()

print(response)
