import json
import allure
from endpoints.order.get_list_order import GetListOrder
from schemas.order.get_list_orders_schemas import GetSchema, GetOrdersSchema




class TestGetListOrder:

    @classmethod
    def setup_class(cls):
        cls.list_order = GetListOrder()

    @allure.title('Проверка получения списка заказов')
    def test_get_list_order(self):
        self.list_order.get_request()
        response_status_code = self.list_order.check_response_status_code()
        response_text = self.list_order.check_response_text()
        GetSchema.parse_obj(response_text)
        response_schema = GetSchema.parse_raw(json.dumps(response_text))
        for order in response_schema.orders:
            GetOrdersSchema.parse_obj(order)
        assert response_status_code == 200 and "orders" in response_text