import pytest
import requests
import string
import random
from data import URL_COURIER, URL_ORDER


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

    response = requests.post(f'{URL_COURIER}', data=payload)

    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    yield login_pass
    payload = {
        "login": login_pass[0],
        "password": login_pass[1]
    }
    response = requests.post(
        f'{URL_COURIER}/login', data=payload, timeout=10)
    if response.status_code == 200:
        response_json = response.json()
        courier_id = response_json['id']
        response_delete = requests.delete(
            f'{URL_COURIER}/{courier_id}', data=payload, timeout=10)
        assert response_delete.status_code == 200 and response_delete.json() == {
            'ok': True}


@pytest.fixture(scope="function")
def login_id(register_new_courier_and_return_login_password):

    payload = {
            "login": register_new_courier_and_return_login_password[0],
            "password": register_new_courier_and_return_login_password[1]
        }
    response = requests.post(
        f'{URL_COURIER}/login', data=payload, timeout=10)
    if response.status_code == 200:
        response_json = response.json()
        yield response_json['id']
        response_delete = requests.delete(
            f'{URL_COURIER}/{response_json["id"]}', data=payload, timeout=10)
        assert response_delete.status_code == 200 and response_delete.json() == {
            'ok': True}
    


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
    response = requests.post(f'{URL_ORDER}',
                             data=payload, timeout=10)
    if response.status_code == 201:
        response_json = response.json()
        return response_json['track']


@pytest.fixture(scope="function")
def order_id(order_track):

    response = requests.get(
        f'{URL_ORDER}/track?t={order_track}', timeout=10)
    if response.status_code == 200:
        response_json = response.json()
        yield response_json['order']['id']
        response_finish_order = requests.put(
            f'{URL_ORDER}/finish/{response_json["order"]["id"]}', timeout=10)
        assert response_finish_order.status_code == 200 and response_finish_order.json() == {
            'ok': True}
