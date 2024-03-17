import requests
import allure
from data import URL_ORDER


class GetListOrder:


    @allure.step('Получаем список заказов')
    def get_request(self):
        return requests.get(
            f'{URL_ORDER}', timeout=30)


