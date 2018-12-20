# coding: utf-8
import requests

url = "https://api.deezer.com/album/68346981"
url = "https://api.deezer.com/user/2490398346/playlists"
response = requests.get(url).json()

#playlist
print(" Titulo: %s \n duration: %s" %(response['data'][0]['title'], response['data'][0]['duration']))

#print(response)

#album
#print(" Titulo: %s \n Autor: %s \n Data de lançamento: %s \n Número de músicas: %s" %(response['title'], response['artist']['name'], response['release_date'], response['nb_tracks'] ))
