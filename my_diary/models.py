from django.db import models

from users.models import User

NULLABLE = {'null': True, 'blank': True}


class Diary(models.Model):
    '''Модель дневника'''
    title = models.CharField(max_length=150, verbose_name='название')
    descriptions = models.CharField(max_length=200, verbose_name='описание', **NULLABLE)
    text_diary = models.TextField(verbose_name='содержимое', **NULLABLE)
    pictures = models.ImageField(upload_to='diary/photo', **NULLABLE, verbose_name='картинка')
    created_at = models.DateTimeField(auto_now_add=True, **NULLABLE, verbose_name='дата создания')
    updated_at = models.DateTimeField(auto_now=True, **NULLABLE, verbose_name='дата обновления')
    owner = models.ForeignKey(User, verbose_name='владелец', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}, '

    class Meta:
        verbose_name = 'Дневник'
        verbose_name_plural = 'Дневники'