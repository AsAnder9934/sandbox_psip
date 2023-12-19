import requests
import folium
import os
import sqlalchemy, sqlalchemy.orm, sqlalchemy.orm.session
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import geoalchemy2                                                                      #geometria
load_dotenv()

db_params=sqlalchemy.URL.create(
    drivername='postgresql+psycopg2',
    username=os.getenv('POSTGRES_USER'),
    password=os.getenv('POSTGRES_PASSWORD'),
    host=os.getenv('POSTGRES_HOST'),
    database=os.getenv('POSTGRES_DB'),
    port=os.getenv('POSTGRES_PORT')
)

engine=sqlalchemy.create_engine(db_params)
connection=engine.connect()
base=sqlalchemy.orm.declarative_base()

Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()

class User(base):
    __tablename__='GeoZwierzyniec'

    id=sqlalchemy.Column(sqlalchemy.Integer(),primary_key=True)                         #typ serial (sam będzie odliczał)
    city=sqlalchemy.Column(sqlalchemy.String(100), nullable=False)
    name=sqlalchemy.Column(sqlalchemy.String(100), nullable=False)
    nick=sqlalchemy.Column(sqlalchemy.String(100), nullable=False)
    posts=sqlalchemy.Column(sqlalchemy.Integer(), nullable=False)

base.metadata.create_all(engine)

def add_user_to(db) -> None:                                                            #    .list informacja o tym że to bedzie lista       None - że nie zwróci nic
    """
    add object to db
    :param db: list - user list
    :return: None
    """
    city=input(('Podaj miasto użytkownika: '))
    name=input('Podaj imię: ')
    nick=input('Podaj nick: ')
    posts=input('Podaj liczbę postów: ')
    db_insert=User(city=city, name=name, nick=nick, posts=posts)
    db.add(db_insert)
    db.commit()

def remove_user_from(db) -> None:
    """
    remove object from db
    :param db: sql - db
    :return: None
    """
    name=input('Podaj imię użytkownika do usunięcia: ')
    users_to_remove=session.query(User).filter(User.name==name)
    if users_to_remove:                                                                #musi być nawias kwadratowy ponieważ odwołujemy się do listy
        for num, user in enumerate(users_to_remove):
            print(f'Znaleziono użytkowników: \n{num+1}: {name} ')
            print('0: Usuń wszystkich ')
    numer=int(input(f'Wybierz użytkownika do usunięcia: '))
    if numer == 0:
        for user in users_to_remove:
            session.delete(user)
    else:
        session.delete(users_to_remove[numer-1])
    session.commit()

def show_users_from(db)->None:
    users_to_show= session.query(User)
    if users_to_show:
        for user in users_to_show:
            print(f'Twój znajomy {user.name} dodał {user.posts} postów ')

def update_user(db) -> None:
    nick_of_user = input("Podaj nick użytkownika do modyfikacji: ")
    print(nick_of_user)
    for user in session.query(User):
        if user.nick == nick_of_user:
            print("Znaleziono !!!")
            user.name= input("Podaj nowe imię: ")
            user.nick = input("Podaj nową ksywkę: ")
            user.posts= int(input("Podaj liczbę postów: "))
            user.city= input('Podaj nową nazwę miasta: ')
            session.commit()

# ===========================================================MAPA=======================================================

def get_coordinates(city)->list[float,float]:
    # pobieranie strony internetowej
    users_to_get_coordinates = session.query(User)
    if users_to_get_coordinates:
        for user in users_to_get_coordinates:
            adres_url=f'https://pl.wikipedia.org/wiki/{city}'

    response=requests.get(url=adres_url) #zwraca obiekt, wywołany jest status
    response_html=BeautifulSoup(response.text, 'html.parser')                   #zwraca tekst kodu strony internetowej, zapisany w html

    #pobieranie współrzędnych
    response_html_lat=response_html.select('.latitude')[1].text                         #kropka oznacza klasę, do ID odwołujemy sie przez #
    # latitude=re.sub('(\<).*?(\>)', repl='', string=response_html_latitude, count=0, flags=0)      z biblioteki   re jakieś gówno które nie idzie zamiast tego .text
    response_html_lat=float(response_html_lat.replace(',','.'))

    response_html_long=response_html.select('.longitude')[1].text #kropka oznacza klasę, do ID odwołujemy sie przez #
    response_html_long=float(response_html_long.replace(',','.'))

    return [response_html_lat,response_html_long]

def get_map_one_user(db)->None:
    get_coordinates_user = session.query(User)
    for user in get_coordinates_user:
        city=get_coordinates(user.city)
    map = folium.Map(location=city,
                     tiles='OpenStreetMap',
                     zoom_start=14
                     )  # location to miejsce wycentrowania mapy
    folium.Marker(location=city,
                  popup=f'Użytkownik: {user.name}\n'
                  f'Liczba postow: {user.posts}'
                  ).add_to(map)
    map.save(f'mapka_{user.name}.html')


def get_map_of(db)->None:
    map = folium.Map(location=[52.3,21.0],
                     tiles='OpenStreetMap',
                     zoom_start=7
                     )  # location to miejsce wycentrowania mapy
    for user in session.query(User):
        city = get_coordinates(user.city)
        folium.Marker(location=city,
                      popup=f'Użytkownik: {user.name}\n'
                      f'Liczba postow: {user.posts}'
                      ).add_to(map)

    map.save('mapka.html')
#==========================================================GUI==========================================================
def gui(db)->None:
    while True:
        print(f'MENU: \n'
              f'0. Zakończ program\n'
              f'1. Wyświetl uzytkowników\n'
              f'2. Dodaj użytkownika\n'
              f'3. Usuń użytkownika\n'
              f'4. Modyfikuj użytkownika\n'
              f'5: Wygeneruj mapę z użytkownikiem \n'
              f'6: Wygeneruj mapę z wszystkimi użytkownikami'
              )
        menu_opction=input('Podaj funkcję do wywołania ')
        print(f'wybrano funkcję{menu_opction}')

        match menu_opction:
            case '0':
                print('Kończę pracę ')
                break
            case '1':
                print('Wyświetlanie listy użytkowników')
                show_users_from(session)
            case '2':
                print('Dodaję użytkownika ')
                add_user_to(session)
            case '3':
                print('Usuwanie użytkowników')
                remove_user_from(session)
            case '4':
                print('Modyfikuję użytkownika')
                update_user(session)
            case '5':
                print('Rysuję mapę z użytkownikiem')
                user = input("Podaj nazwę użytkownika do modyfikacji")
                for item in session.query(User):
                    if item.name == user:
                        get_map_one_user(session)
            case '6':
                print('Rysuję mapę z wszystkimi użytkownikami')
                get_map_of(session)