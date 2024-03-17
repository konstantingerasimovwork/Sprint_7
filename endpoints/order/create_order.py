import requests
import allure
from data import URL_ORDER


class CreateOrder:


    @allure.step('Создаём заказ')
    def post_request(self, payload):
        return requests.post(f'{URL_ORDER}', data=payload, timeout=10)
    
    @allure.step('Отменяем заказ')
    def cancel_order(self, track_order):
        payload = {
            "track": str(track_order)
        }
        return requests.put(
            f'{URL_ORDER}/cancel', data=payload, timeout=10)
