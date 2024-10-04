from django.contrib.auth.forms import UserCreationForm
from my_diary.forms import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    '''Класс для создания пользователя'''
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',)
