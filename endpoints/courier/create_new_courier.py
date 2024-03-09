import requests
import allure
from data import URL



class CreateNewCourier:
    
    response = None
    response_json = None

    @allure.step('Создаём курьера')
    def post_request(self, payload):
        self.response = requests.post(
            f'{URL}/api/v1/courier', data=payload, timeout=10)
        self.response_json = self.response.json()

    @allure.step('Получаем содержимое ответа')
    def check_response_text(self):
        return self.response_json

    @allure.step('Получаем статус код')
    def check_response_status_code(self):
        return self.response.status_code
    



