def add_user_to(users_list:list) -> None:        #    .list informacja o tym że to bedzize lista       None - że nie zwróci nic
    """
    add object to list
    :param users_list: list - user list
    :return: None
    """

    name=input('Podaj imię')
    nick=input('Podaj nick')
    posts=input('Podaj liczbę postów')
    users_list.append({'name':name,'nick':nick, 'posts': posts})

def remove_user_from(users_list:list) -> None:
    """
    remove object from list
    :param users_list: list - users list
    :return: None
    """
    tmp_list=[]
    name=input('Podaj imię użytkownika do usunięcia: ')
    for user in users_list:
        if user["name"]==name:                                 #musi być nawias kwadratowy ponieważ odwołujemy się do listy
            tmp_list.append(user)
            #users_list.remove(user)
    print(f'Znaleziono użytkowników: ')
    print('0: Usuń wszystkich ')
    for numerek, user_to_be_removed in enumerate(tmp_list):
        print(f'{numerek+1}: {user_to_be_removed}')
    numer=int(input(f'Wybierz użytkownika do usunięcia: ')) #wynikiem operacji inpunt jest string więc musimy zMIENIĆ go dalej na ineger
    if numer == 0:
        for user in tmp_list:
            users_list.remove(user)
    else:
        users_list.remove(tmp_list[numer-1])

    #users_list.remove(tmp_list[numer-1])

def show_users_from(users_list:list)->None:
    for user in users_list:
        print(f'Twój znajomy {user["name"]} dodał {user["posts"]} postów')

def gui(users_list)->None:
    while True:
        print(f'MENU: \n'
              f'0. Zakończ program\n'
              f'1. Wyświetl uzytkowników\n'
              f'2. Dodaj użytkownika\n'
              f'3. Usuń użytkownika\n'
              f'4. Modyfikuj użytkownika\n'
              )
        menu_opction=input('Podaj funkcję do wywołania ')
        print(f'wybrano funkcję{menu_opction}')

        match menu_opction:
            case '0':
                print('Kończę pracę ')
                break
            case '1':
                print('Wyświetlanie listy użytkowników')
                show_users_from(users_list)
            case '2':
                print('Dodaję użytkownika ')
                add_user_to(users_list)
            case '3':
                print('Usuwanie użytkowników')
                remove_user_from(users_list)
            case '4':
                print('Modyfikuję użytkownika')
                update_user(users_list)


# def update_user(users_list) :
#     nick_of_user = input("")
#     for user in users_list:
#         if user['nick'] == nick
#     pass


def update_user(users_list: list[dict, dict]) -> None:
    nick_of_user = input("Podaj nick użytkownika do modyfikacji:")
    print(nick_of_user)
    for user in users_list:
        if user ["nick"] == nick_of_user:
            print("Znaleziono !!!")
            user['name']= input("Podaj nowe imię: ")
            user['nick'] = input("Podaj nowA ksywkę: ")
            user['posts'] = int(input("Podaj liczbę postów: "))