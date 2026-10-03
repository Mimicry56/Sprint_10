import allure
from src.api_methods import ApiMethods
from src.data import Messages, StatusCodes


class TestDeleteAd:

    @allure.title('Проверка успешного удаления объявления')
    def test_delete_ad(self, created_ad, created_user):
        listing_id = created_ad
        headers = created_user['headers']

        response = ApiMethods.delete_ad(listing_id, headers)
        response_body = response.json()

        assert response.status_code == StatusCodes.OK
        assert response_body['message'] == Messages.SUCCESS_DELETE_AD
