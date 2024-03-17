import pytest
import json
import allure
from endpoints.order.create_order import CreateOrder
from endpoints.base_endpoints import BaseEndpoints
from schemas.order.create_order_schemas import PostSchema
from data import ORDER_INVALID_JSON


class TestCreateOrder:

    @classmethod
    def setup_class(cls):
        cls.new_order = CreateOrder()
        cls.base = BaseEndpoints()

    @allure.title('Проверка создания заказа')
    @allure.description('BUG: Тест падает, если передавать только 1 цвет, с 2-мя цветами тест проходит')
    @pytest.mark.parametrize('color', ['BLACK', 'GREY', ['BLACK', 'GREEN'], ''])
    def test_create_order(self, color):
        payload = {
            "firstName": "Konstantin",
            "lastName": "Grasimov",
            "address": "Odesskaya,21",
            "metroStation": "4",
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Comment",
            "color": [color]
        }
        response = self.new_order.post_request(payload)
        response_status_code = self.base.check_response_status_code(response)
        response_text = self.base.check_response_text(response)
        PostSchema.parse_obj(response_text)
        assert response_status_code == 201 and 'track' in response_text, f'Статус код - {response_status_code} и текст ответа - {response_text}'


    @allure.title('Проверка создания заказа с невалидными данными')
    @allure.description('BUG: заказы создаются с невалидными данными')
    @pytest.mark.parametrize('payload', [ORDER_INVALID_JSON[0], ORDER_INVALID_JSON[1]])
    def test_create_order_with_invalid_data(self, payload):
        json_payload = json.dumps(payload)
        response = self.new_order.post_request(json_payload)
        response_status_code = self.base.check_response_status_code(response)
        assert response_status_code == 400, f'Статус код - {response_status_code}'
