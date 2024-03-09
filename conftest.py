import pytest
import requests
import string
import random
from data import URL


@pytest.fixture(scope="function")
def register_new_courier_and_return_login_password():

    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login_pass = []

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(f'{URL}/api/v1/courier', data=payload)

    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    return login_pass


@pytest.fixture(scope="function")
def login_id(register_new_courier_and_return_login_password):

    payload = {
            "login": register_new_courier_and_return_login_password[0],
            "password": register_new_courier_and_return_login_password[1]
        }
    response = requests.post(
        f'{URL}/api/v1/courier/login', data=payload, timeout=10)
    if response.status_code == 200:
        response_json = response.json()
        return response_json['id']


@pytest.fixture(scope="function")
def order_track():

    payload = {
            "firstName": "Konstantin",
            "lastName": "Grasimov",
            "address": "Odesskaya,21",
            "metroStation": "4",
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Comment",
            "color": ['BLACK', 'GREY']
        }
    response = requests.post(f'{URL}/api/v1/orders',
                             data=payload, timeout=10)
    if response.status_code == 201:
        response_json = response.json()
        return response_json['track']


@pytest.fixture(scope="function")
def order_id(order_track):

    response = requests.get(
        f'{URL}/api/v1/orders/track?t={order_track}', timeout=10)
    if response.status_code == 200:
        response_json = response.json()
        return response_json['order']['id']
