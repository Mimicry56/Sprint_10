import random
import string
import allure


@allure.step("Сгенерировать случайную строку длиной {length}")
def generate_random_string(length=8):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

@allure.step("Сгенерировать данные пользователя")
def generate_user_data():
    random_part = generate_random_string()
    password = f'password_{random_part}'

    return {
        'email': f'test_user_{random_part}@yandex.ru',
        'password': password,
        'submitPassword': password
    }

@allure.step('Получить заголовки авторизации')
def get_auth_headers(access_token):
    return {
        'Authorization': f'Bearer {access_token}'
    }
