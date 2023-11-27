from bs4 import BeautifulSoup
from dane import users_list
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
for item in cities:
    print(get_coordinates(item))

user={'city': 'Gdańsk', "name": "Marek", "nick": "mmmmm", "posts": 251}

### Rysowanie mapy
def get_map_one_user(user: str) -> None:
    city = get_coordinates(user['city'])
    map = folium.Map(
        location=city,
        tiles="OpenStreetMap",
        zoom_start=15,
    )
    folium.Marker(
        location=city,
        popup=f'Tu rządzi: {user["name"]},'              
              f'postów: {user["posts"]} '
    ).add_to(map)
    map.save(f'mapka_{user["name"]}.html')
def get_map_of(users: list[dict,dict]) -> None:
    map = folium.Map(
        location=[52.3, 21.0],
        tiles="OpenStreetMap",
        zoom_start=7,
    )
    for user in users:
        folium.Marker(
            location=get_coordinates(
                city=user['city']),
                popup=f'Użytkownik: {user["name"]} \n'                 
                      f'Liczba postów {user["posts"]}'
        ).add_to(map)
        map.save('mapka.html')
get_map_of(user)