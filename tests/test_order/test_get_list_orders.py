import json
import allure
from endpoints.order.get_list_order import GetListOrder
from endpoints.base_endpoints import BaseEndpoints
from schemas.order.get_list_orders_schemas import GetSchema, GetOrdersSchema




class TestGetListOrder:

    @classmethod
    def setup_class(cls):
        cls.list_order = GetListOrder()
        cls.base = BaseEndpoints()

    @allure.title('Проверка получения списка заказов')
    def test_get_list_order(self):
        response = self.list_order.get_request()
        response_status_code = self.base.check_response_status_code(response)
        response_text = self.base.check_response_text(response)
        GetSchema.parse_obj(response_text)
        response_schema = GetSchema.parse_raw(json.dumps(response_text))
        for order in response_schema.orders:
            GetOrdersSchema.parse_obj(order)
        assert response_status_code == 200 and "orders" in response_text