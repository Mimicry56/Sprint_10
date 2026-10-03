import allure
from src.api_methods import ApiMethods
from src.data import StatusCodes, TestData

class TestCreateAd:

    @allure.title('Проверка успешного создания объявления')
    def test_create_ad_success(self, created_user):
        headers = created_user['headers']
        response = ApiMethods.create_ad(TestData.TEST_AD, headers)
        response_body = response.json()

        assert response.status_code == StatusCodes.CREATED
        assert response_body['name'] == TestData.TEST_AD['name']
