from dane import users_list


def update_user(users_list: list[dict, dict]) -> None:
    nick_of_user = input("Podaj nick użytkownika do modyfikacji:")
    print(nick_of_user)
    for user in users_list:
        if user ["nick"] == nick_of_user:
            print("Znaleziono !!!")
            user['name']= input("Podaj nowe imię: ")
            user['nick'] = input("Podaj nowA ksywkę: ")
            user['posts'] = int(input("Podaj liczbę postów: "))


update_user(users_list)
for user in users_list:
    print(user)