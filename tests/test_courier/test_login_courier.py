import pytest
import allure
from endpoints.courier.login_courier import LoginCourier
from endpoints.base_endpoints import BaseEndpoints
from schemas.courier.login_courier_schemas import PostOkSchema, PostErrorSchema
from data import LOGIN_INVALID_JSON


class TestLoginCourier:

    @classmethod
    def setup_class(cls):
        cls.login_courier = LoginCourier()
        cls.base = BaseEndpoints()

    @allure.title('Проверка логина курьера в системе')
    def test_login_courier(self, register_new_courier_and_return_login_password):
        payload = {
            "login": register_new_courier_and_return_login_password[0],
            "password": register_new_courier_and_return_login_password[1]
        }
        response = self.login_courier.post_request(payload)
        response_status_code = self.base.check_response_status_code(response)
        response_text = self.base.check_response_text(response)
        PostOkSchema.parse_obj(response_text)
        assert response_status_code == 200 and 'id' in response_text, f'{response_status_code} and {response_text}'


    @allure.title('Проверка логина курьера в системе с несуществующим login')
    @allure.description('BUG: Тело ответа не совпадает с документацией')
    def test_get_error_with_incorrect_login(self, register_new_courier_and_return_login_password):
        payload = {
            "login": 'test',
            "password": register_new_courier_and_return_login_password[1]
        }
        response = self.login_courier.post_request(payload)
        response_status_code = self.base.check_response_status_code(response)
        response_text = self.base.check_response_text(response)
        PostErrorSchema.parse_obj(response_text)
        assert response_status_code == 404 and response_text == {
            "message": "Учетная запись не найдена"}, f'Статус код - {response_status_code} и текст ответа - {response_text}'


    @allure.title('Проверка логина курьера в системе с несуществующим password')
    @allure.description('BUG: Тело ответа не совпадает с документацией')
    def test_get_error_with_incorrect_password(self, register_new_courier_and_return_login_password):
        payload = {
            "login": register_new_courier_and_return_login_password[0],
            "password": 'test'
        }
        response = self.login_courier.post_request(payload)
        response_status_code = self.base.check_response_status_code(response)
        response_text = self.base.check_response_text(response)
        PostErrorSchema.parse_obj(response_text)
        assert response_status_code == 404 and response_text == {
            "message": "Учетная запись не найдена"}, f'Статус код - {response_status_code} и текст ответа - {response_text}'


    @allure.title('Проверка логина курьера в системе без login')
    @allure.description('BUG: Тело ответа не совпадает с документацией')
    def test_get_error_without_login(self, register_new_courier_and_return_login_password):
        payload = {
            "password": register_new_courier_and_return_login_password[1]
        }
        response = self.login_courier.post_request(payload)
        response_status_code = self.base.check_response_status_code(response)
        response_text = self.base.check_response_text(response)
        PostErrorSchema.parse_obj(response_text)
        assert response_status_code == 400 and response_text == {
            "message": "Недостаточно данных для входа"}, f'Статус код - {response_status_code} и текст ответа - {response_text}'


    @allure.title('Проверка логина курьера в системе без password')
    @allure.description('BUG: Приходит 504 ошибка')
    def test_get_error_without_password(self, register_new_courier_and_return_login_password):
        payload = {
            "login": register_new_courier_and_return_login_password[0]
        }
        response = self.login_courier.post_request(payload)
        response_status_code = self.base.check_response_status_code(response)
        response_text = self.base.check_response_text(response)
        PostErrorSchema.parse_obj(response_text)
        assert response_status_code == 400 and response_text == {
            "message": "Недостаточно данных для входа"}, f'Статус код - {response_status_code} и текст ответа - {response_text}'


    @allure.title('Проверка логина курьера в системе с невалидными login и password')
    @allure.description('BUG: на вторые тестовые данные приходит JSONDecodeError')
    @pytest.mark.parametrize('payload', [LOGIN_INVALID_JSON[0], LOGIN_INVALID_JSON[1]])
    def test_login_with_invalid_data(self, payload):
        response = self.login_courier.post_request(payload)
        response_status_code = self.base.check_response_status_code(response)
        assert response_status_code == 404, f'Статус код - {response_status_code}'
