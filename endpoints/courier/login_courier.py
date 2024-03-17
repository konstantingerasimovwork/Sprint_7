import requests
import allure
from data import URL_COURIER



class LoginCourier:

    @allure.step('Логин курьера в системе')
    def post_request(self, payload):
        return requests.post(
            f'{URL_COURIER}/login', data=payload, timeout=10)
    
    @allure.step('Удаляем курьера')
    def delete_courier(self, courier_id):
        payload = {
            "id": str(courier_id)
        }
        return requests.delete(
            f'{URL_COURIER}/{courier_id}', data=payload, timeout=10)

