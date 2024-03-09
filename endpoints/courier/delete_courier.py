import requests
import allure
from data import URL


class DeleteCourier:

    response = None
    response_json = None

    @allure.step('Удаляем курьера')
    def delete_request(self, id, payload):
        self.response = requests.delete(
            f'{URL}/api/v1/courier/{id}', data=payload, timeout=10)
        self.response_json = self.response.json()

    @allure.step('Удаляем курьера без id')
    def delete_request_without_id(self, payload):
        self.response = requests.delete(
            f'{URL}/api/v1/courier', data=payload, timeout=10)
        self.response_json = self.response.json()

    @allure.step('Получаем содержимое ответа')
    def check_response_text(self):
        return self.response_json

    @allure.step('Получаем статус код')
    def check_response_status_code(self):
        return self.response.status_code

