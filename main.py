
from dane import users_list

#print(f'Twój znajomy {zmienna_na_dane[0]["nick"]} opublikował {zmienna_na_dane[0]["posts"]} postów!!!')         #    te f (f-string) przed ''klauzula w python do zmiennych jaką wstawiamy     []do którego elementu listy się odwołujemy

for user in users_list:
    print(f'Twój znajomy {user["nick"]} dodał {user["posts"]} postów')

