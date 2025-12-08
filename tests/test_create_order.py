import allure
import requests
import pytest


from data import Endpoint, Message, User


class TestCreateOrder:
    @allure.step('Создать заказ с разными цветами самоката')
    @pytest.mark.parametrize('color', [['BLACK'], ['GREY'], ['BLACK', 'GREY'], []])
    def test_create_order(self, color):
        payload = User.user
        payload['color'] = color
        r = requests.post(Endpoint.CREATE_ORDER, json=payload)
        assert r.status_code == 201
        assert Message.CREATE_ORDER in r.text

