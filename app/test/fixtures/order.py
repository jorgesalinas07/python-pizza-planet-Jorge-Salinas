import random
import pytest
from datetime import datetime
from ..utils.functions import (shuffle_list, get_random_sequence,
                               get_random_string)


def date_mock() -> str:
    return f'{random.randrange(1,12)}/{random.randrange(1,28)}/2022'


def client_data_mock() -> dict:
    return {
        'client_address': get_random_string(),
        'client_dni': get_random_sequence(),
        'client_name': get_random_string(),
        'client_phone': get_random_sequence()
    }


@pytest.fixture
def order_uri():
    return '/order/'


@pytest.fixture
def client_data():
    return client_data_mock()


@pytest.fixture
def order(client_data, create_ingredients, create_size, create_beverages) -> dict:
    ingredients = [ingredient.get('_id') for ingredient in create_ingredients]
    beverage = [beverage.get('_id') for beverage in create_beverages]
    size_id = create_size.json.get('_id')
    return {
        **client_data,
        'ingredients': ingredients,
        'size_id': size_id,
        'beverages': beverage
    }


def order_with_created_ingredient_and_beverage(client_data: dict, ingredients: list, size_id: int, 
                                                beverages: list, date: str) -> dict:
    return {
        **client_data,
        'ingredients': ingredients,
        'size_id': size_id,
        'beverages': beverages,
        'date': date
    }


def orders_with_repeted_clients_and_ingredient(top_3_clients, ingredients, size_id, beverage, month_with_more_revenue):
    orders = []
    for i in range(0, 6):
        new_order = order_with_created_ingredient_and_beverage(
            top_3_clients[0], [ingredients[0]], size_id, beverage, month_with_more_revenue)
        orders.append(new_order)

        if i % 2 == 0:
            new_order = order_with_created_ingredient_and_beverage(
                top_3_clients[1], [ingredients[0]], size_id, beverage, date_mock())
            orders.append(new_order)

        if i == 4 or i == 5:
            new_order = order_with_created_ingredient_and_beverage(
                top_3_clients[2], ingredients[0:5], size_id, beverage, date_mock())
            orders.append(new_order)

        new_order = order_with_created_ingredient_and_beverage(
            client_data_mock(), ingredients[0:5], size_id, beverage, date_mock())
        orders.append(new_order)

    return orders


@pytest.fixture
def create_orders(create_order) -> list:
    orders = []
    for _ in range(10):
        new_order = create_order
        orders.append(new_order)
    return orders


@pytest.fixture
def create_order(client, order, order_uri):
    response = client.post(order_uri, json=order)
    return response


@pytest.fixture
def create_repeted_clients_and_ingredients_order(create_ingredients, create_size,
                                                 create_beverages, client_data):
    top_3_clients = [client_data, client_data_mock(), client_data_mock()]
    month_with_more_revenue = date_mock()
    ingredients = [ingredient.get('_id') for ingredient in create_ingredients]
    beverage = [beverage.get('_id') for beverage in create_beverages]
    most_repeated_ingredient = ingredients[0]
    size_id = create_size.json.get('_id')
    orders = orders_with_repeted_clients_and_ingredient(
        top_3_clients, ingredients, size_id, beverage, month_with_more_revenue)

    return orders, most_repeated_ingredient, month_with_more_revenue, top_3_clients
