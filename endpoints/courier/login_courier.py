import requests
import allure
from data import URL



class LoginCourier:

    response = None
    response_json = None

    @allure.step('Логин курьера в системе')
    def post_request(self, payload):
        self.response = requests.post(
            f'{URL}/api/v1/courier/login', data=payload, timeout=10)
        self.response_json = self.response.json()
    
    @allure.step('Удаляем курьера')
    def delete_courier(self, courier_id):
        payload = {
            "id": str(courier_id)
        }
        self.response = requests.delete(
            f'{URL}/api/v1/courier/{courier_id}', data=payload, timeout=10)
        self.response_json = self.response.json()

    @allure.step('Получаем содержимое ответа')
    def check_response_text(self):
        return self.response_json

    @allure.step('Получаем статус код')
    def check_response_status_code(self):
        return self.response.status_code
