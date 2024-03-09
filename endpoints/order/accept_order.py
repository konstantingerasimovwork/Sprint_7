import requests
import allure
from data import URL


class AcceptOrder:

    response = None
    response_json = None

    @allure.step('Принимаем заказ с id заказа и id курьера ')
    def put_request(self, courier_id, order_id):
        self.response = requests.put(
            f'{URL}/api/v1/orders/accept/{order_id}?courierId={courier_id}', timeout=10)
        self.response_json = self.response.json()
    
    @allure.step('Принимаем заказ без id заказа')
    def put_request_without_order_id(self, courier_id):
        self.response = requests.put(
            f'{URL}/api/v1/orders/accept/courierId={courier_id}', timeout=10)
        self.response_json = self.response.json()
    
    @allure.step('Принимаем заказ без id курьера')
    def put_request_without_login_id(self, order_id):
        self.response = requests.put(
            f'{URL}/api/v1/orders/accept/{order_id}', timeout=10)
        self.response_json = self.response.json()
    
    @allure.step('Завершаем заказ')
    def finish_order(self, order_id):
        self.response = requests.put(
            f'{URL}/api/v1/orders/finish/{order_id}', timeout=10)
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
