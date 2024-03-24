# Sprint_6
### Предварительные требования
* Python 3.11
* pytest
* allure
* pydantic
* json

### Запуск тестов
* pytest -v
#### courier
* pytest -v tests/test_courier/test_delete_courier.py
* pytest -v tests/test_courier/test_login_courier.py 
* pytest -v tests/test_courier/test_create_new_courier.py
#### courier
* pytest -v tests/test_order/test_accept_order.py
* pytest -v tests/test_order/test_create_order.py
* pytest -v tests/test_order/test_get_order_by_number.py
* pytest -v tests/test_order/test_get_list_orders.py

Тесты запускаются для https://qa-scooter.praktikum-services.ru

### Дополнительные файлы
* data.py - тестовые данные для тестов
* conftest.py - фикстуры
* allure_results - результаты тестов

### Просмотр web отчёта allure
* allure serve target/allure_results 