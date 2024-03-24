import allure
from endpoints.order.accept_order import AcceptOrder
from endpoints.base_endpoints import BaseEndpoints
from schemas.order.accept_order_schemas import PutSchema, ErrorSchema


class TestAcceptOrder:

    @classmethod
    def setup_class(cls):
        cls.accept_order = AcceptOrder()
        cls.base = BaseEndpoints()

    @allure.title('Проверка принятия заказа')
    def test_accept_order(self, login_id, order_id):
        response = self.accept_order.put_request(login_id, order_id)
        response_status_code = self.base.check_response_status_code(response)
        response_text = self.base.check_response_text(response)
        PutSchema.parse_obj(response_text)
        assert response_status_code == 200 and response_text == {"ok": True}, f'{response_status_code} and {response_text}'


    @allure.title('Проверка принятия заказа без id заказа')
    @allure.description('BUG: Тело ответа не совпадают с документацией')
    def test_accept_order_without_order_id(self, login_id):
        response = self.accept_order.put_request_without_order_id(login_id)
        response_status_code = self.base.check_response_status_code(response)
        response_text = self.base.check_response_text(response)
        ErrorSchema.parse_obj(response_text)
        assert response_status_code == 400 and response_text == {
            "message":  "Недостаточно данных для поиска"}, f'{response_status_code} and {response_text}'


    @allure.title('Проверка принятия заказа без id курьера')
    @allure.description('BUG: Тело ответа не совпадают с документацией')
    def test_accept_order_without_login_id(self, order_id):
        response = self.accept_order.put_request_without_login_id(order_id)
        response_status_code = self.base.check_response_status_code(response)
        response_text = self.base.check_response_text(response)
        ErrorSchema.parse_obj(response_text)
        assert response_status_code == 400 and response_text == {
            "message":  "Недостаточно данных для поиска"}, f'{response_status_code} and {response_text}'


    @allure.title('Проверка принятия заказа с несуществующим id курьера')
    @allure.description('BUG: Тело ответа не совпадают с документацией')
    def test_accept_order_with_non_existent_login_id(self, order_id):
        response = self.accept_order.put_request(0, order_id)
        response_status_code = self.base.check_response_status_code(response)
        response_text = self.base.check_response_text(response)
        ErrorSchema.parse_obj(response_text)
        assert response_status_code == 404 and response_text == {
            "message": "Курьера с таким id не существует"}, f'{response_status_code} and {response_text}'


    @allure.title('Проверка принятия заказа с несуществующим id заказа')
    @allure.description('BUG: Тело ответа не совпадают с документацией')
    def test_accept_order_with_non_existent_order_id(self, login_id):
        response = self.accept_order.put_request(login_id, 0)
        response_status_code = self.base.check_response_status_code(response)
        response_text = self.base.check_response_text(response)
        ErrorSchema.parse_obj(response_text)
        assert response_status_code == 404 and response_text == {
            "message": "Заказа с таким id не существует"}, f'{response_status_code} and {response_text}'

