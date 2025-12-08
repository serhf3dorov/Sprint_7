import allure
import requests


from data import Endpoint, Message
from conftest import create_courier
from helpers import *


class TestAuthCourier:
    @allure.step('Авторизация курьера')
    def test_auth_courier(self, create_courier):
        login_pass = create_courier
        r = requests.post(Endpoint.LOGIN_COURIER, data={
            'login': login_pass[0],
            'password': login_pass[1]
        })
        assert r.status_code == 200
        assert Message.LOGING_COURIER in r.text


    @allure.step('Авторизация курьера без логина')
    def test_auth_without_login(self, create_courier):
        login_pass = create_courier
        r = requests.post(Endpoint.LOGIN_COURIER, data={
            'login': '',
            'password': login_pass[1]
        })
        assert r.status_code == 400
        assert Message.LOGING_COURIER_WITHOUT_DATA == r.text


    @allure.step('Авторизация курьера без пароля')
    def test_auth_without_password(self, create_courier):
        login_pass = create_courier
        r = requests.post(Endpoint.LOGIN_COURIER, data={
            'login': login_pass[0],
            'password': ''
        })
        assert r.status_code == 400
        assert Message.LOGING_COURIER_WITHOUT_DATA == r.text


    @allure.step('Авторизация несуществующего курьера')
    def test_auth_not_existing_courier(self):
        r = requests.post(Endpoint.LOGIN_COURIER, data={
            'login': 'ksenia',
            'password': 'qwerty1234'
        })
        assert r.status_code == 404
        assert Message.LOGING_NOT_EXISTING_COURIER == r.text

