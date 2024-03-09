import requests
import allure
from data import URL


class GetListOrder:

    response = None
    response_json = None

    @allure.step('Получаем список заказов')
    def get_request(self):
        self.response = requests.get(
            f'{URL}/api/v1/orders', timeout=30)
        self.response_json = self.response.json()

    @allure.step('Получаем содержимое ответа')
    def check_response_text(self):
        return self.response_json

    @allure.step('Получаем статус код')
    def check_response_status_code(self):
        return self.response.status_code
