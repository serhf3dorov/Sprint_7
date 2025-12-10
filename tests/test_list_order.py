import allure
import requests
from data import Endpoint, Message


class TestListOrder:
    @allure.title('Получить список заказов')
    def test_list_order(self):
        with allure.step('Запрос на получение списка заказов отправлен'):
            r = requests.get(Endpoint.ORDER_LIST)
        assert r.status_code == 200
        assert Message.LIST_ORDERS in r.text

