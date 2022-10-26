from django.core.mail import send_mail


def send_confirmation_email(user, code):
    full_link = f'http://localhost:8000/api/v1/accounts/activate/{code}/'
    send_mail(
        'Здравствуйте активируйте ваш аккаунт!',
        f'Чтобы активировать ваш аккаунт нужно перейти по ссылке: {full_link}',
        'turat.imankulov@gmail.com',
        [user],
        fail_silently=False)


def send_notification(user, order_id, price):
    email = user.email
    send_mail('уведомления о создании заказа!',
              f'вы создали заказ{order_id}, ожидайте звонка! \n полная стоимость ващего заказа {price}\nспасибо за то что выбрали нас!',
              'from Femir9200_222@mail.ru',
              [email],
              fail_silently=False
              )

def send_code_password_reset(user):
    code = user.activation_code
    email = user.email
    send_mail(
        'письмо с кодом для сброса пароля!',
        f'Ваш код для того чтобы восстановить пароль:{code}\n Никому не передовайте этот код!',
        'from Femir9200_222@mail.ru',
        [email],
        fail_silently=False

    )

