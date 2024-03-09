import requests
import allure
from data import URL


class GetOrderByTrack:

    response = None
    response_json = None

    @allure.step('Получаем заказ по номеру')
    def get_request(self, track):
        self.response = requests.get(
            f'{URL}/api/v1/orders/track?t={track}', timeout=30)
        self.response_json = self.response.json()

    @allure.step('Получаем заказ без номера')
    def get_without_track_request(self):
        self.response = requests.get(
            f'{URL}/api/v1/orders/track?t=', timeout=30)
        self.response_json = self.response.json()

    @allure.step('Получаем содержимое ответа')
    def check_response_text(self):
        return self.response_json

    @allure.step('Получаем статус код')
    def check_response_status_code(self):
        return self.response.status_code
