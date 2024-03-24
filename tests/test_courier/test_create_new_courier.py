import allure
from endpoints.courier.create_new_courier import CreateNewCourier
from endpoints.base_endpoints import BaseEndpoints
from helpers import new_login_and_password
from schemas.courier.create_new_courier_schemas import PostOkSchema, PostErrorSchema

class TestRegisterCourier:

    @classmethod
    def setup_class(cls):
        cls.new_courier = CreateNewCourier()
        cls.base = BaseEndpoints()

    @allure.title('Проверка создания курьера')
    def test_register_new_courier(self):
        login, password, first_name = new_login_and_password()
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        response = self.new_courier.post_request(payload)
        response_text = self.base.check_response_text(response)
        response_status_code = self.base.check_response_status_code(response)
        PostOkSchema.parse_obj(response_text)
        assert response_status_code == 201 and response_text == {
            "ok": True}, f'Статус код - {response_status_code} и текст ответа - {response_text}'


    @allure.title('Проверка создания двух одинаковых курьеров')
    @allure.description('BUG: Body ответа не совпадает с документацией')
    def test_register_identical_couriers(self):
        login, password, first_name = new_login_and_password()
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        response = self.new_courier.post_request(payload)
        response = self.new_courier.post_request(payload)
        response_text = self.base.check_response_text(response)
        response_status_code = self.base.check_response_status_code(response)
        PostErrorSchema.parse_obj(response_text)
        assert response_status_code == 409 and response_text == {
            "message": "Этот логин уже используется. Попробуйте другой."}, f'Статус код - {response_status_code} и текст ответа - {response_text}'


    @allure.title('Проверка создания курьера без login')
    @allure.description('BUG: Body ответа не совпадает с документацией')
    def test_register_without_login(self):
        login, password, first_name = new_login_and_password()
        payload = {
            "password": password,
            "firstName": first_name
        }
        response = self.new_courier.post_request(payload)
        response_text = self.base.check_response_text(response)
        response_status_code = self.base.check_response_status_code(response)
        PostErrorSchema.parse_obj(response_text)
        assert response_status_code == 400 and response_text == {
            "message": "Недостаточно данных для создания учетной записи"}, f'Статус код - {response_status_code} и текст ответа - {response_text}'


    @allure.title('Проверка создания курьера без password')
    @allure.description('BUG: Body ответа не совпадает с документацией')
    def test_register_without_password(self):
        login, password, first_name = new_login_and_password()
        payload = {
            "login": login,
            "firstName": first_name
        }
        response = self.new_courier.post_request(payload)
        response_text = self.base.check_response_text(response)
        response_status_code = self.base.check_response_status_code(response)
        PostErrorSchema.parse_obj(response_text)
        assert response_status_code == 400 and response_text == {
            "message": "Недостаточно данных для создания учетной записи"}, f'Статус код - {response_status_code} и текст ответа - {response_text}'


    @allure.title('Проверка создания курьера без firstName')
    @allure.description('BUG: успешная регистрация при отсутсвии поля firstName, схема ответа не совпадает с ожидаемой')
    def test_register_without_first_name(self):
        login, password, first_name = new_login_and_password()
        payload = {
            "login": login,
            "password": password
        }
        response = self.new_courier.post_request(payload)
        response_text = self.base.check_response_text(response)
        response_status_code = self.base.check_response_status_code(response)
        PostErrorSchema.parse_obj(response_text)
        assert response_status_code == 400 and response_text == {
            "message": "Недостаточно данных для создания учетной записи"}, f'Статус код - {response_status_code} и текст ответа - {response_text}'
