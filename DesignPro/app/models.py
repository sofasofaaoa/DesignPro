from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    pass


class Request(models.Model):
    user = models.ForeignKey('MyUser', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    summary = models.TextField(max_length=1000, help_text='Введите описание вашего проекта')
    date_time = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    photo = models.ImageField(null=True)
    STATUS = (
        ('n', 'New'),
        ('i', 'In process'),
        ('c', 'Completed')
    )
    status = models.CharField(max_length=1, choices=STATUS, default='n')

    def __str__(self):
        return '%s (%s)' % (self.title, self.user.name)




class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
