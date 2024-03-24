import requests
import allure
from data import URL_COURIER


class DeleteCourier:

    @allure.step('Удаляем курьера')
    def delete_request(self, id, payload):
        return requests.delete(
            f'{URL_COURIER}/{id}', data=payload, timeout=10)


    @allure.step('Удаляем курьера без id')
    def delete_request_without_id(self, payload):
        return requests.delete(
            f'{URL_COURIER}', data=payload, timeout=10)

