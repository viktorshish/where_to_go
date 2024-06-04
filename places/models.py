from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    description_short = models.TextField(verbose_name='Короткое описание')
    description_long = models.TextField(verbose_name='Длинное описание')
    coordinates_lng = models.FloatField(verbose_name='Долгота')
    coordinates_lan = models.FloatField(verbose_name='Широта')

    def __str__(self):
        return self.title
