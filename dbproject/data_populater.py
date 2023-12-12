import datetime
import random
from bruh import session
from user_class_def import user 
example_names = [
    "Hovhannes",
    "Hakob",
    "Sargis",
    "Grigor",
    "Harutyun",
    "Gevorg",
    "Ashot",
    "Suren",
    "Levon",
    "Gurgen",
    "Roza",
    "Siranush",
    "Anahit",
    "Mariam",
    "Seda",
    "Astghik",
    "Hasmik",
    "Haykanush",
    "Gohar",
    "Satenik"
]

example_surnames = [
    "Sargsyan",
    "Harutyunyan",
    "Grigoryan",
    "Hovhannisyan",
    "Hakobyan",
    "Khachatryan",
    "Vardanyan",
    "Petrosyan",
    "Karapetyan",
    "Gevorgyan",
    "Hakobi",
    "Harutyuni",
    "Karapeti",
    "Khachaturi",
    "Sargsi",
    "Gevorgi",
    "Mkrtichi",
    "Petrosi",
    "Avetisi",
    "Arshaki"
]

def random_date():
    start_date = datetime.datetime(1900, 1, 1)
    end_date = datetime.datetime(2015, 1, 1)
    random_days = random.randrange((end_date - start_date).days)
    date = start_date + datetime.timedelta(days=random_days)
    return date

for _ in range(777):  
    username = random.choice(example_names)
    usersurname = random.choice(example_surnames)
    userbirth = random_date()

    new_user = user(username=username, usersurname=usersurname, userbirth=userbirth)
    session.add(new_user)
    
    