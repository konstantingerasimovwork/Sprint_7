import requests
import allure
from data import URL_ORDER, URL_COURIER


class AcceptOrder:

    @allure.step('Принимаем заказ с id заказа и id курьера ')
    def put_request(self, courier_id, order_id):
        return requests.put(
            f'{URL_ORDER}/accept/{order_id}?courierId={courier_id}', timeout=10)

    
    @allure.step('Принимаем заказ без id заказа')
    def put_request_without_order_id(self, courier_id):
        return requests.put(
            f'{URL_ORDER}/accept/courierId={courier_id}', timeout=10)

    
    @allure.step('Принимаем заказ без id курьера')
    def put_request_without_login_id(self, order_id):
        return requests.put(
            f'{URL_ORDER}/accept/{order_id}', timeout=10)

