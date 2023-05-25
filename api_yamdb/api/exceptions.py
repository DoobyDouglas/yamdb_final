from rest_framework.exceptions import ValidationError


class UsernameValueException(ValidationError):
    default_detail = (
        'Имя не соответствует форме. '
        'Допустимы только буквы от "a" до "z" без учёта регистра, '
        'цифры от 0 до 9 и символы ". @ + - _".'
    )
