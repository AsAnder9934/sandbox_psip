from dane import users_list
from utils.functions import add_user_to, remove_user_from, show_users_from, gui

# add_user_to(users_list)
# remove_user_from(users_list)
# def show_users_from(users_list:list)->None:
#     for user in users_list:
#         print(f'Twój znajomy {user["name"]} dodał {user["posts"]} postów')

gui(users_list)