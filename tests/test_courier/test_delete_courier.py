import allure
from endpoints.courier.delete_courier import DeleteCourier
from schemas.courier.delete_courier_schemas import DeleteSchema, ErrorSchema


class TestCreateOrder:

    @classmethod
    def setup_class(cls):
        cls.delete_courier = DeleteCourier()

    @allure.title('Проверка удаления курьера')
    def test_delete_courier(self, login_id):
        payload = {
            "id": str(login_id)
        }
        self.delete_courier.delete_request(login_id, payload)
        response_status_code = self.delete_courier.check_response_status_code()
        response_text = self.delete_courier.check_response_text()
        DeleteSchema.parse_obj(response_text)
        assert response_status_code == 200 and response_text == {'ok': True}, f'Статус код - {response_status_code} и текст ответа - {response_text}'


    @allure.title('Проверка удаления курьера с несуществующим id')
    @allure.description('BUG: Тело ответа не совпадает с документацией')
    def test_delete_courier_with_non_exist_id(self):
        payload = {
            "id": 'три'
        }
        self.delete_courier.delete_request(3, payload)
        response_status_code = self.delete_courier.check_response_status_code()
        response_text = self.delete_courier.check_response_text()
        ErrorSchema.parse_obj(response_text)
        assert response_status_code == 404 and response_text == {
            "message": "Курьера с таким id нет"}, f'Статус код - {response_status_code} и текст ответа - {response_text}'


    @allure.title('Проверка удаления курьера без id')
    @allure.description('BUG: Код и тело ответа отличаются')
    def test_delete_courier_without_id(self):
        payload = {
            "id": ''
        }
        self.delete_courier.delete_request_without_id(payload)
        response_status_code = self.delete_courier.check_response_status_code()
        response_text = self.delete_courier.check_response_text()
        ErrorSchema.parse_obj(response_text)
        assert response_status_code == 400 and response_text == {
            "message": "Недостаточно данных для удаления курьера"}, f'Статус код - {response_status_code} и текст ответа - {response_text}'


    @allure.title('Проверка удаления курьера с невалидным id')
    @allure.description('BUG: Тело ответа не совпадает с документацией')
    def test_delete_courier_with_invalid_id(self):
        payload = {
            "id": 3
        }
        self.delete_courier.delete_request(3, payload)
        response_status_code = self.delete_courier.check_response_status_code()
        response_text = self.delete_courier.check_response_text()
        ErrorSchema.parse_obj(response_text)
        assert response_status_code == 404 and response_text == {
            "message": "Курьера с таким id нет"}, f'Статус код - {response_status_code} и текст ответа - {response_text}'
