URL = 'https://qa-scooter.praktikum-services.ru'

ORDER_INVALID_JSON = [{
    "firstName": 123,
    "lastName": 456,
    "address": 789,
    "metroStation": 4,
    "phone": +7900000000,
    "rentTime": "5",
    "deliveryDate": 123,
    "comment": 123,
    "color": [456]
},
{
    "firstName": None,
    "lastName": None,
    "address": None,
    "metroStation": None,
    "phone": None,
    "rentTime": None,
    "deliveryDate": None,
    "comment": None,
    "color": None
}]

LOGIN_INVALID_JSON = [{
    "login": 12346,
    "password": 123456
},
{
    "login": None,
    "password": None
}]

NEW_COURIER_INVALID_JSON = [{
    "login": 12346,
    "password": 123456,
    "first_name": 123456 
},
    {
    "login": None,
    "password": None,
    "first_name": None
}]
