from django.conf import settings
from django.db import models
from django.utils import timezone


class Blog(models.Model):
    title = models.CharField('タイトル', max_length=100)
    image = models.ImageField(upload_to='images', verbose_name='イメージ画像')
    thumbnail = models.ImageField(upload_to='images', verbose_name='サムネイル', null=True, blank=True)
    skill = models.CharField('スキル', max_length=100)
    url = models.CharField('URL', max_length=100, null=True, blank=True)
    created = models.DateField('作成日時')
    description = models.TextField('説明')

    def __str__(self):
        return self.title

class Car(models.Model):
    name = models.CharField('車種', max_length=100)
    size = models.CharField('サイズ', max_length=100)

    def __str__(self):
        return self.name

