from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail


def confirmation_code_send(user):
    confirmation_code = default_token_generator.make_token(user)
    send_mail(
        subject='Регистрация',
        message=f'Код для регистрации: {confirmation_code}',
        from_email='admin@yandex.ru',
        recipient_list=[user.email]
    )
