class Urls:
    BASE_URL = 'https://qa-desk.education-services.ru'

    REGISTER_USER = '/api/signup'
    LOGIN_USER = '/api/signin'
    LISTING_AD = '/api/listings'
    CREATED_AD = '/api/create-listing'
    UPDATE_AD = '/api/update-offer'


class Messages:
    USER_ALREADY_EXISTS = 'Почта уже используется'
    AD_NOT_FOUND_OR_EDIT_FORBIDDEN_MESSAGE = 'Оффер не найден или у вас нет прав на его редактирование'
    SUCCESS_DELETE_AD = 'Объявление удалено успешно'


class StatusCodes:
    OK = 200
    CREATED = 201
    BAD_REQUEST = 400
    UNAUTHORIZED = 401


class TestData:
    LOGIN_DATA = {
        'email': "yakubova_7@gmail.com",
        'password': "sexy56"
    }

    TEST_AD = { 'name': "Тестовое объявление",
               'category': "Садоводство",
               'condition': "Новый",
               'city': "Новосибирск",
               'description': "описание тест",
               'price': "5000"       
    }

    UPDATE_TEST_AD = { 'name': "Новое название",
               'category': "Садоводство",
               'condition': "Новый",
               'city': "Новосибирск",
               'description': "описание тест",
               'price': "5000"       
    }
