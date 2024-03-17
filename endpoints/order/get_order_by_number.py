import requests
import allure
from data import URL_ORDER


class GetOrderByTrack:


    @allure.step('Получаем заказ по номеру')
    def get_request(self, track):
        return requests.get(
            f'{URL_ORDER}/track?t={track}', timeout=30)


    @allure.step('Получаем заказ без номера')
    def get_without_track_request(self):
        return requests.get(
            f'{URL_ORDER}/track?t=', timeout=30)


