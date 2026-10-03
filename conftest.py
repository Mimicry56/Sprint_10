import pytest
from src.api_methods import ApiMethods
from src.helpers import generate_user_data, get_auth_headers
from src.data import TestData


@pytest.fixture
def created_user():
    user_data = generate_user_data()

    response = ApiMethods.create_user(user_data)
    response_body = response.json()

    access_token = response_body['access_token']['access_token']
    headers = get_auth_headers(access_token)

    yield {
        'user_data': user_data,
        'headers': headers
    }


@pytest.fixture
def created_ad(created_user):
    headers = created_user['headers']
    
    response = ApiMethods.create_ad(TestData.TEST_AD, headers)
    response_body = response.json()

    return response_body['id']

@pytest.fixture
def other_user_headers():
    response = ApiMethods.login_user(TestData.LOGIN_DATA)
    response_body = response.json()

    access_token = response_body['token']['access_token']
    return get_auth_headers(access_token)
