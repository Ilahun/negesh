from django.db import models

# Create your models here.
class TopBack(models.Model):
    name = models.CharField('ФИО', max_length=500)
    email = models.EmailField('E-mail адрес')
    theme = models.CharField('Тема сообщения', max_length=200)
    description = models.CharField('Сообщение', max_length=12555)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'