from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    pass


class Request(models.Model):
    user = models.ForeignKey('MyUser', on_delete=models.SET_NULL, null=True, default='user.username')
    title = models.CharField(max_length=200)
    summary = models.TextField(max_length=1000, help_text='Введите описание вашего проекта')
    date_time = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    STATUS = (
        ('n', 'New'),
        ('i', 'In process'),
        ('c', 'Completed')
    )
    status = models.CharField(max_length=1, choices=STATUS, default='n')
    comm = models.TextField(max_length=500, blank=True, null=True)
    photo = models.ImageField(upload_to='img/',
                              help_text="Максимальный размер изображения 2MB",
                              blank=True,
                              null=True)
    design = models.ImageField(upload_to='designs/',
                               help_text="Максимальный размер изображения 2MB",
                               blank=True,
                               null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
