import allure
import requests
from data import Endpoint, Message


class TestListOrder:
    @allure.step('Получить список заказов')
    def test_list_order(self):
        r = requests.get(Endpoint.ORDER_LIST)
        assert r.status_code == 200
        assert Message.LIST_ORDERS in r.text

