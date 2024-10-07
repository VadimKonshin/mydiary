import secrets
import string
from random import sample

from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm
from users.models import User


class UserCreateView(CreateView):
    '''Класс создания пользователя'''
    model = User
    form_class = UserRegisterForm
    template_name = 'users/user_form.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        '''функция активации пользователя'''
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}/'
        send_mail(subject='Подтвержение почты',
                  message=f'Для подтверждения авторизации на сайте {url}',
                  from_email=EMAIL_HOST_USER,
                  recipient_list=[user.email]
                  )
        return super().form_valid(form)


def email_verification(request, token):
    '''функция активации пользователя'''
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))


def reset_password(request):
    context = {
        'success_message': 'Пароль успешно сброшен. Новый пароль был отправлен на ваш адрес электронной почты.',
    }
    if request.method == 'POST':
        email = request.POST.get('email')
        user = get_object_or_404(User, email=email)

        # Генерируем новый пароль
        characters = string.ascii_letters + string.digits
        password = ''.join(sample(characters, 10))  # Используем sample

        user.set_password(password)
        user.save()

        # Отправляем новый пароль на email
        send_mail(
            subject='Восстановление пароля',
            message=f'Здравствуйте, вы запрашивали обновление пароля. Ваш новый пароль: {password}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )

        return render(request, 'users/reset_password.html', context)

    return render(request, 'users/reset_password.html')


def generate_password():
    '''функция генерации пароля'''
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(password_characters) for _ in range(10))
    return password
