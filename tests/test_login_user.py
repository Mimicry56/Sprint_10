import allure
from src.api_methods import ApiMethods
from src.data import StatusCodes

class TestLoginUser:

    @allure.title('Проверка успешной авторизации существующего пользователя')
    def test_login_existing_user_success(self, created_user):
        user_data = created_user['user_data']

        response = ApiMethods.login_user({
            'email': user_data['email'],
            'password': user_data['password'],
        })

        assert response.status_code == StatusCodes.CREATED
        assert response.json()['user']['email'] == user_data['email']
        assert response.json()['token']['access_token']
