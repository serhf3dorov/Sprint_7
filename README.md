# tests for API Яндекс Самокат

## Сценарии, покрытые тестами:


### Создание курьера - ***test_create_courier.py***
* `test_create_courier` - проверка создания курьера
* `test_create_existing_courier` - проверка создания двух одинаковых курьеров
* `test_create_courier_without_one_field` - проверка создания курьера без логина/пароля


### Авторизация курьера - ***test_auth_courier.py***
* `test_auth_courier` - проверка авторизации курьера
* `test_auth_without_login` - проверка авторизации курьера без логина
* `test_auth_without_password` - проверка авторизации курьера без пароля
* `test_auth_not_existing_courier` - проверка авторизации несуществующего курьера


### Удаление курьера - ***test_delete_courier.py***
* `test_delete_courier` - проверка удаления курьера
* `test_delete_not_existing_courier` - проверка удаления несуществующего курьера
* `test_delete_courier_without_id` - проверка удаления курьера без id


### Создание заказа - ***test_create_order.py***
* `test_create_order` - создать заказ с разными цветами самоката


### Получение списка заказов - ***test_list_order.py***
* `test_list_order` - получить список заказов


## Для запуска:
* Установить зависимости
``` shell
pip3 install -r requirements.txt
```
* Запустить все тесты из директории tests
```shell
pytest tests --alluredir=allure_results
```
* Посмотреть отчет
``` shell
allure serve allure_results
```