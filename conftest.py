import pytest
from helpers import *


@pytest.fixture(scope='function')
def create_courier():
    login_pass = register_new_courier_and_return_login_password()
    yield login_pass
    response_post = requests.post(Endpoint.LOGIN_COURIER, data={
        'login': login_pass[0],
        'password': login_pass[1],
    })
    courier_id = response_post.json()['id']
    requests.delete(f'{Endpoint.DELETE_COURIER}{courier_id}')
