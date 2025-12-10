import allure
import requests
import pytest
from data import Endpoint, Message
from helpers import *


class TestCreateCourier:
    @allure.title('Создать курьера')
    def test_create_courier(self):
        login, password, first_name = generate_data()
        payload = {
            'login': login,
            'password': password,
            'firstname': first_name
        }
        with allure.step('Запрос на создание курьера отправлен'):
            r = requests.post(Endpoint.CREATE_COURIER, data=payload)
        assert r.status_code == 201
        assert Message.CREATE_COURIER == r.text
        


    @allure.title('Создать двух одинаковых курьеров')
    def test_create_existing_courier(self):
        data = register_new_courier_and_return_login_password()
        with allure.step('Запрос на создание двух одинаковых курьеров отправлен'):
            r = requests.post(Endpoint.CREATE_COURIER, data={
            'login': data[0],
            'password': data[1],
            'firstname': data[2]
        })
        assert r.status_code == 409
        assert Message.CREATE_EXISTING_COURIER == r.text


    @allure.title('Создать курьера без логина/пароля')
    @pytest.mark.parametrize('field', ['login', 'password'])
    def test_create_courier_without_one_field(self, field):
        payload = generate_data_payload()
        del payload[field]
        with allure.step('Запрос на создание курьера без логина или пароля отправлен'):
            r = requests.post(Endpoint.CREATE_COURIER, data=payload)
        assert r.status_code == 400
        assert Message.CREATE_COURIER_WITHOUT_LOGIN == r.text

