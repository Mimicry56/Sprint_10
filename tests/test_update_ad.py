import allure
from src.api_methods import ApiMethods
from src.data import StatusCodes, TestData, Messages

class TestEditAd:

    @allure.title('Проверка успешного редактированич объявления')
    def test_update_ad_success(self, created_ad, created_user):
        listing_id = created_ad
        headers = created_user['headers']
        response = ApiMethods.update_ad(listing_id, TestData.UPDATE_TEST_AD, headers)
        response_body = response.json()

        assert response.status_code == StatusCodes.OK
        assert response_body['name'] == TestData.UPDATE_TEST_AD['name']

    @allure.title('Проверка неуспешного редактированич объявления с другим токкеном')
    def test_update_other_user_ad(self, created_ad, other_user_headers):
        response = ApiMethods.update_ad(created_ad, TestData.UPDATE_TEST_AD, other_user_headers)
        response_body = response.json()

        assert response.status_code == StatusCodes.UNAUTHORIZED
        assert response_body['message'] == Messages.AD_NOT_FOUND_OR_EDIT_FORBIDDEN_MESSAGE
