from dane import users_list

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
add_user_to(users_list)
add_user_to(users_list)
add_user_to(users_list)

#print(f'Twój znajomy {zmienna_na_dane[0]["nick"]} opublikował {zmienna_na_dane[0]["posts"]} postów!!!')         #    te f (f-string) przed ''klauzula w python do zmiennych jaką wstawiamy     []do którego elementu listy się odwołujemy

for user in users_list:
    print(f'Twój znajomy {user["nick"]} dodał {user["posts"]} postów')

