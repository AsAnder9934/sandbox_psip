# from dane import users_list
#
#
# def update_user(users_list: list[dict, dict]) -> None:
#     nick_of_user = input("Podaj nick użytkownika do modyfikacji:")
#     print(nick_of_user)
#     for user in users_list:
#         if user ["nick"] == nick_of_user:
#             print("Znaleziono !!!")
#             user['name']= input("Podaj nowe imię: ")
#             user['nick'] = input("Podaj nowA ksywkę: ")
#             user['posts'] = int(input("Podaj liczbę postów: "))
#
#
# update_user(users_list)
# for user in users_list:
#     print(user)

from bs4 import BeautifulSoup
import requests
import re
import folium

cities=['Mały_Płock', 'Warszawa']
#pobranie strony interetowej
def get_coordinates(nazwa_miejscowosci:str)->list[float, float]:
    adres_URL = f'https://pl.wikipedia.org/wiki/{nazwa_miejscowosci}'
    response = requests.get(url=adres_URL)
    response_html = BeautifulSoup(response.text,'html.parser')

    #pobieranie współrzędnych
    response_html_latitude=response_html.select('.latitude')[1].text    # . ponieważ to oznacza class
    #latitude=re.sub('(\<).*?(\>)', repl='', string=response_html_latitude, count=0, flags=0)      z biblioteki   re jakieś gówno które nie idzie zamiast tego .text
    response_html_latitude=float(response_html_latitude.replace(',','.'))

    response_html_longitude=response_html.select('.longitude')[1].text
    response_html_longitude=float(response_html_longitude.replace(',','.'))

    return [response_html_latitude, response_html_longitude]
# for item in cities:
#     print(get_coordinates(item))

### Rysowanie mapy
city=get_coordinates(nazwa_miejscowosci='Mały_Płock')
map=folium.Map(location=city, tiles='OpenStreetMap', zoom_start=15)

for item in cities:
    folium.Marker(location=get_coordinates(nazwa_miejscowosci=item), popup='GEOINF').add_to(map)
map.save('mapka.html')