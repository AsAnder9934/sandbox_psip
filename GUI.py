from tkinter import *
import tkintermapview
import tkinter

users=[]

class User:
    def __init__(self,name,surname,posts,city):
        self.name=name
        self.surname=surname
        self.posts=posts
        self.city=city

def add_user():
    name=entry_name.get()
    surname=entry_surname.get()
    posts=entry_posts.get()
    city=entry_city.get()

    user=User(name, surname, posts, city)
    users.append(user)
    print(f'Lista użytkowników {users}')
    users_list()

    entry_name.delete(0,END)
    entry_surname.delete(0,END)
    entry_posts.delete(0,END)
    entry_city.delete(0,END)

    entry_name.focus()
def users_list():
    listbox_object_list.delete(0,END)
    for idx,user in enumerate(users):
        listbox_object_list.insert(idx, f'{user.name} {user.surname}')

def show_user_details():
    i=listbox_object_list.index(ACTIVE)
    name=users[i].name
    surname=users[i].surname
    posts=users[i].posts
    city=users[i].city

    label_name_details_value.config(text=name)
    label_surname_details_value.config(text=surname)
    label_posts_details_value.config(text=posts)
    label_city_details_value.config(text=city)

def delete_user():
    i = listbox_object_list.index(ACTIVE)
    users.pop(i)
    users_list()

def update_users():
    i = listbox_object_list.index(ACTIVE)
    entry_name.delete(0, END)
    entry_surname.delete(0, END)
    entry_posts.delete(0, END)
    entry_city.delete(0, END)

    entry_name.insert(0,users[i].name)
    entry_surname.insert(0,users[i].surname)
    entry_posts.insert(0,users[i].posts)
    entry_city.insert(0,users[i].city)

    button_add_object.config(text='Zapisz zmiany', command=lambda:update_data(i))

def update_data(i:int):
    users[i].name=entry_name.get()
    users[i].surname=entry_surname.get()
    users[i].posts=entry_posts.get()
    users[i].city=entry_city.get()

    button_add_object.config(text='Dodaj nowy obiekt', command=add_user)

    entry_name.delete(0, END)
    entry_surname.delete(0, END)
    entry_posts.delete(0, END)
    entry_city.delete(0, END)

    entry_name.focus()

    users_list()

# create tkinter window
root=Tk()
root.geometry('800x700')
root.title('Aplikacja do obsługi bazy danych')

# ===============RAMKI DO UPORZĄDKOWANIA STRUKTURY===========================

frame_object_list=Frame(root)
frame_forms=Frame(root)
frame_object_description=Frame(root)

frame_object_list.grid(row=0, column=0, padx=50)
frame_forms.grid(row=0, column=1)
frame_object_description.grid(row=1, column=0, columnspan=2, padx=50, pady=20)

# ===================frame_object_list========================================================
label_object_list=Label(frame_object_list, text='Lista obiektów: ')
listbox_object_list=Listbox(frame_object_list, width=35)
button_show_detail=Button(frame_object_list, text='Pokaż szczegóły', command=show_user_details)
button_delete_object=Button(frame_object_list, text='Usuń obiekt', command=delete_user)
button_eddit_object=Button(frame_object_list, text='Edytuj obiekt', command=update_users)

label_object_list.grid(row=0, column=0)
listbox_object_list.grid(row=1, column=0, columnspan=3)
button_show_detail.grid(row=2, column=0)
button_delete_object.grid(row=2, column=1)
button_eddit_object.grid(row=2, column=2)
# ===================frame_forms====================================================================
label_new_object=Label(frame_forms, text='Formularz dodawania i edycji użytkownika: ')
label_name=Label(frame_forms, text='Imię: ')
label_surname=Label(frame_forms, text='Nazwisko: ')
label_posts=Label(frame_forms, text='Liczba postów: ')
label_city=Label(frame_forms, text='Miejscowość: ')

entry_name=Entry(frame_forms)
entry_surname=Entry(frame_forms, width=30)
entry_posts=Entry(frame_forms)
entry_city=Entry(frame_forms)

label_new_object.grid(row=0, column=0, columnspan=2)
label_name.grid(row=1, column=0, sticky=W)
label_surname.grid(row=2, column=0, sticky=W)
label_posts.grid(row=3, column=0, sticky=W)
label_city.grid(row=4, column=0, sticky=W)

entry_name.grid(row=1, column=1, sticky=W)
entry_surname.grid(row=2, column=1, sticky=W)
entry_posts.grid(row=3, column=1, sticky=W)
entry_city.grid(row=4, column=1, sticky=W)

button_add_object=Button(frame_forms, text='Dodaj nowy obiekt', command=add_user)
button_add_object.grid(row=5, column=0, columnspan=2)
# ===================frame_object_description=================================================

label_object_description=Label(frame_object_description, text='Szczegóły obiektu')
label_name_details=Label(frame_object_description, text='Imię: ')
label_name_details_value=Label(frame_object_description, text='...:  ', width=10)

label_surname_details=Label(frame_object_description, text='Nazwisko: ')
label_surname_details_value=Label(frame_object_description, text='...: : ', width=10)

label_posts_details=Label(frame_object_description, text='Liczba postów: ')
label_posts_details_value=Label(frame_object_description, text='...: : ', width=10)

label_city_details=Label(frame_object_description, text='Miejscowość: ')
label_city_details_value=Label(frame_object_description, text='...: ', width=10)

label_object_description.grid(row=0, column=0, sticky=W)

label_name_details.grid(row=1, column=0)
label_name_details_value.grid(row=1, column=1)
label_surname_details.grid(row=1, column=2)
label_surname_details_value.grid(row=1, column=3)
label_posts_details.grid(row=1, column=4)
label_posts_details_value.grid(row=1, column=5)
label_city_details.grid(row=1, column=6)
label_city_details_value.grid(row=1, column=7)
#========================================================================================================================
# create map widget
map_widget = tkintermapview.TkinterMapView(frame_object_description, width=700, height=300, corner_radius=0)
# set current widget position and zoom
map_widget.set_position(52.2,21)
map_widget.set_zoom(10)
# position widget in app
map_widget.grid(row=2, column=0, columnspan=8)

root.mainloop()

# TODO okodować tak żeby dodawało pinezkę z bazy danych i pokazywało użytkownika
# TODO dokleić GIU do bazy danych
# TODO good luck, have fun