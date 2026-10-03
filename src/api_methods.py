import allure
import requests
from src.data import Urls
from pathlib import Path


class ApiMethods:

    @staticmethod
    @allure.step('Создать пользователя')
    def create_user(user_data):
        return requests.post(f'{Urls.BASE_URL}{Urls.REGISTER_USER}', json=user_data)

    @staticmethod
    @allure.step('Авторизоваться пользователем')
    def login_user(login_data):
        return requests.post(f'{Urls.BASE_URL}{Urls.LOGIN_USER}', json=login_data)

    @staticmethod
    @allure.step('Создать объявление')
    def create_ad(listing_data, headers):
        image_path = Path(__file__).parent / 'test_image.jpg'

        with open(image_path, 'rb') as image:
            return requests.post(f'{Urls.BASE_URL}{Urls.CREATED_AD}',
                data=listing_data,
                files={'images': image},
                headers=headers
            )

    @staticmethod
    @allure.step('Изменить объявление')
    def update_ad(listing_id, update_data, headers):
        return requests.patch(f'{Urls.BASE_URL}{Urls.UPDATE_AD}/{listing_id}', 
                              data=update_data,
                              headers=headers)

    @staticmethod
    @allure.step('Удалить объявление')
    def delete_ad(listing_id, headers):
        return requests.delete(f'{Urls.BASE_URL}{Urls.LISTING_AD}/{listing_id}', headers=headers)
    