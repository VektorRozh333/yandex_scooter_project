from selenium.webdriver.common.by import By

BASE_URL = 'https://qa-scooter.education-services.ru/'

DATA_FORM_TEST = {
    "first_name": 'Райан',
    "last_name": 'Гослинг',
    "address": 'Пушкина, д. 13',
    "metro": 'Красногвардейская',
    "user_number": '+88005553535',
    "delivery_time": '01.09.2033',
    "comments": 'Spasibo tovarisch'
}

DATA_FORM = [

    [
        'Райан',
        'Гослинг',
        'Пушкина, д. 13',
        'Красногвардейская',
        '+88005553535'
    ],
]