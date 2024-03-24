import allure
from endpoints.order.get_order_by_number import GetOrderByTrack
from endpoints.base_endpoints import BaseEndpoints
from schemas.order.get_order_by_number_schemas import GetOrderSchema, ErrorSchema


class TestGetListOrder:

    @classmethod
    def setup_class(cls):
        cls.order = GetOrderByTrack()
        cls.base = BaseEndpoints()

    @allure.title('Проверка получения заказа по номеру')
    @allure.description('BUG: Status в ответе стоит самым последним, в документации под track')
    @allure.description('BUG: Если заказ не принят в работу, отсутвтует courierFirstName(в документации это не указано)')
    def test_get_order_by_track(self, order_track):
        response = self.order.get_request(order_track)
        response_status_code = self.base.check_response_status_code(response)
        response_text = self.base.check_response_text(response)
        response_order = response_text.get("order")
        GetOrderSchema.parse_obj(response_order)
        assert response_status_code == 200 and "order" in response_text, f'Статус код - {response_status_code} и body ответа - {response_text["order"]}'


    @allure.title('Проверка получения заказа без номера')
    @allure.description('BUG: Body ответа не совпадает с документацией')
    def test_get_order_without_track(self):
        response = self.order.get_without_track_request()
        response_status_code = self.base.check_response_status_code(response)
        response_text = self.base.check_response_text(response)
        ErrorSchema.parse_obj(response_text)
        assert response_status_code == 400 and response_text == {
            "message":  "Недостаточно данных для поиска"}, f'Статус код - {response_status_code} и текст ответа - {response_text}'


    @allure.title('Проверка получения заказа с несуществующим номером')
    @allure.description('BUG: Body ответа не совпадает с документацией')
    def test_get_order_with_non_expected_track(self):
        response = self.order.get_request(0)
        response_status_code = self.base.check_response_status_code(response)
        response_text = self.base.check_response_text(response)
        ErrorSchema.parse_obj(response_text)
        assert response_status_code == 404 and response_text == {
            "message": "Заказ не найден"}, f'Статус код - {response_status_code} и текст ответа - {response_text}'
