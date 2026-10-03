import allure
from src.api_methods import ApiMethods
from src.data import Messages, StatusCodes
from src.helpers import generate_user_data


class TestCreateUser:

    @allure.title('Проверка успешного создания пользователя')
    def test_create_user_success(self):
        user_data = generate_user_data()
        response = ApiMethods.create_user(user_data)
        response_body = response.json()

        assert response.status_code == StatusCodes.CREATED
        assert response_body['user']['email'] == user_data['email']

    @allure.title('Проверка ошибки при создании уже существующего пользователя')
    def test_create_existing_user_returns_error(self, created_user):
        user_data = created_user['user_data']
        response = ApiMethods.create_user(user_data)
        response_body = response.json()

        assert response.status_code == StatusCodes.BAD_REQUEST
        assert response_body['message'] == Messages.USER_ALREADY_EXISTS
