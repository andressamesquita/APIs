# -*- coding: utf-8 -*-
import requests

url = 'https://community-sentiment.p.mashape.com/text/'

response = unirest.post(url,
  headers={
    "X-Mashape-Key": "suachave",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json"
  },
  params={
    "txt": "Today is  a good day"
  }
)

print(response)
