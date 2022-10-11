from django.core.mail import send_mail


def send_confirmation_email(user, code):
    send_mail(
        'здравствуте активируйте ваш аккаунт!',
        f'чтобы активировать ваш аккаунт нужно перейти по ссылке',
        'niko01w@mail.ru',
        [user],
        fail_silently=False

    )