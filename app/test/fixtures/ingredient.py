import pytest

from ..utils.functions import get_random_price, get_random_string


def ingredient_mock() -> dict:
    return {
        'name': get_random_string(),
        'price': get_random_price(10, 20)
    }


@pytest.fixture
def ingredient_uri():
    return '/ingredient/'


@pytest.fixture
def ingredient():
    return ingredient_mock()


@pytest.fixture
def ingredients():
    return [ingredient_mock() for _ in range(3)]


@pytest.fixture
def create_ingredient(client, ingredient_uri) -> dict:
    response = client.post(ingredient_uri, json=ingredient_mock())
    return response


@pytest.fixture
def create_ingredients(client, ingredient_uri) -> list:
    ingredients = []
    for _ in range(3):
        new_ingredient = client.post(ingredient_uri, json=ingredient_mock())
        ingredients.append(new_ingredient.json)
    return ingredients
    
@pytest.fixture
def repeted_ingredients(ingredient) -> list:
    most_repeated_ingredient = ingredient
    ingredients = []
    for _ in range(2):
        ingredients.append(most_repeated_ingredient)
        ingredients.append(most_repeated_ingredient)
        ingredients.append(ingredient_mock())

    return ingredients, most_repeated_ingredient
