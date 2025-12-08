import pytest
from helpers import *


@pytest.fixture(scope='function')
def create_courier():
    login_pass = register_new_courier_and_return_login_password()
    yield login_pass
    delete_courier(login_pass[0], login_pass[1])

