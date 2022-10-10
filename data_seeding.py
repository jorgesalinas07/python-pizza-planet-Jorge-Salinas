import json
import random, requests
from app.test.utils.functions import (get_random_phone, get_random_sequence)

names = ["Jorge Salinas", "Carlos Martinez", "Pedro Perez", "Luis Rodriguez", "Amaranto Lopez", "Andres Parra", 
"Alejandra Zinisterra", "Caroline Verjel", "Rosilveris Carrillo", "Judit Perez", "Daniela Alvarez", "Leidy Molina",
"Katty Hoyos", "Edgardo Mojica", "Andrea Torres", "Ramiro Ranauro", "Andres Garrido", "Ted Mosby", "Barney Steanson",
"David Verjel"]

addresses = ["Avenue "+str(i)+"th" for i in range(1,21)]

beverages=["Beer", "Coke", "Water", "Lemonade", "Orange juge", "Frappe", "Pumking juge", "Regulage juge", "Milk Juge", "Papaya juge"]
ingredients=["Peperoni", "Avocado", "Tomato", "Onion", "House salsa", "Ham", "Cheese", "Pineapple", "Salami", "Mushroom"]
sizes=["Large", "Junior", "Short", "Familiar", "For 4"]

beverages_ids = [i for i in range(1,10)]
ingredients_ids = [i for i in range(1,10)]

size_url = "http://127.0.0.1:5000/size/"
beverage_url = "http://127.0.0.1:5000/beverage/"
ingredient_url = "http://127.0.0.1:5000/ingredient/"
order_url = "http://127.0.0.1:5000/order/"

client_info=[]
orders = []

[requests.post(beverage_url     , json = {'type':beverage, 'price': random.randrange(1,10)}) for beverage in beverages]
[requests.post(size_url         , json = {'name':size, 'price': random.randrange(1,30)}) for size in sizes]
[requests.post(ingredient_url   , json = {'name':ingredient, 'price': random.randrange(1,10)}) for ingredient in ingredients]

for i in range(1,20):
    client_info.append(
        {
            i:{
        "client_address":random.choice(addresses),
        "client_dni":get_random_sequence(),
        "client_name":random.choice(names),
        "client_phone":get_random_phone(),
            }
        }
    )
    names.remove(client_info[i-1][i]["client_name"])
    addresses.remove(client_info[i-1][i]["client_address"])

for _ in range(1,101):
    random_index = (random.randrange(1,20))
    data = {
            **client_info[random_index-1][random_index],
            'ingredients':random.choices(ingredients_ids, k=random.randrange(1,7)),
            'size_id' : random.randrange(1,4),
            'beverages': random.choices(beverages_ids, k=random.randrange(1,6)),
            'date':  f'{random.randrange(1,12)}/{random.randrange(1,28)}/2022'
        }
    create_order = requests.post(order_url, json = data)
    json_response = json.loads(create_order.text)
    