import allure
import requests
import pytest


from data import Endpoint, Message, User


class TestCreateOrder:
    @allure.title('Создать заказ с разными цветами самоката')
    @pytest.mark.parametrize('color', [['BLACK'], ['GREY'], ['BLACK', 'GREY'], []])
    def test_create_order(self, color):
        payload = User.user
        payload['color'] = color
        with allure.step('Запрос на создание заказа самоката с цветами черным/серым/черносерым/без указания цвета отправлен'):
            r = requests.post(Endpoint.CREATE_ORDER, json=payload)
        assert r.status_code == 201
        assert Message.CREATE_ORDER in r.text

