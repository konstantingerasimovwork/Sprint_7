import requests
import allure
from data import URL_COURIER



class CreateNewCourier:
    
    @allure.step('Создаём курьера')
    def post_request(self, payload):
        return requests.post(
            f'{URL_COURIER}', data=payload, timeout=10)
