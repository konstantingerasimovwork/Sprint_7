import requests
import allure
from data import URL


class CreateOrder:

    response = None
    response_json = None

    @allure.step('Создаём заказ')
    def post_request(self, payload):
        self.response = requests.post(f'{URL}/api/v1/orders', data=payload, timeout=10)
        self.response_json = self.response.json()
    
    @allure.step('Отменяем заказ')
    def cancel_order(self, track_order):
        payload = {
            "track": str(track_order)
        }
        self.response = requests.put(
            f'{URL}/api/v1/orders/cancel', data=payload, timeout=10)
        self.response_json = self.response.json()

    @allure.step('Получаем содержимое ответа')
    def check_response_text(self):
        return self.response_json

    @allure.step('Получаем статус код')
    def check_response_status_code(self):
        return self.response.status_code
