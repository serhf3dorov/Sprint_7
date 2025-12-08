import allure
import requests


from data import Endpoint, Message
from helpers import *


class TestDeleteCourier:
    @allure.step('Удалить курьера')
    def test_delete_courier(self):
        login_pass = register_new_courier_and_return_login_password()
        r = requests.post(Endpoint.LOGIN_COURIER, data={
            'login': login_pass[0],
            'password': login_pass[1]
        })
        courier_id = r.json()['id']
        r_delete = requests.delete(f'{Endpoint.DELETE_COURIER}{courier_id}')
        assert r_delete.status_code == 200
        assert Message.DELETE_COURIER == r_delete.text


    @allure.step('Удалить несуществующего курьера')
    def test_delete_not_existing_courier(self):
        login_pass = register_new_courier_and_return_login_password()
        r = requests.post(Endpoint.LOGIN_COURIER, data={
            'login': login_pass[0],
            'password': login_pass[1]
        })
        courier_id = 666666
        r_delete = requests.delete(f'{Endpoint.DELETE_COURIER}{courier_id}')
        assert r_delete.status_code == 404
        assert Message.DELETE_NOT_EXISTING_COURIER == r_delete.text


    @allure.step('Удалить курьера без id')
    def test_delete_courier_without_id(self):
        r = requests.delete(Endpoint.DELETE_COURIER)
        assert r.status_code == 404
        assert Message.DELETE_COURIER_WITHOUT_ID == r.text

