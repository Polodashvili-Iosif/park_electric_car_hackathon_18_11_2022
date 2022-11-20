# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class CarInfo(models.Model):
    mark = models.CharField(max_length=30, verbose_name='Марка',)
    model = models.CharField(max_length=30, verbose_name='Модель')
    vin = models.CharField(max_length=17, verbose_name='VIN')
    state_number = models.CharField(max_length=8, verbose_name='Гос. номер')
    year = models.IntegerField(verbose_name='Год выпуска')
    category = models.CharField(max_length=3, verbose_name='Категория')
    color = models.CharField(max_length=20, verbose_name='Цвет')
    engine_number = models.CharField(max_length=30, verbose_name='Номер двигателя')
    power_hp = models.CharField(max_length=20, verbose_name='Л.с.')
    power_kwt = models.CharField(max_length=20, verbose_name='Кв./ч.')
    type = models.CharField(max_length=20, verbose_name='Тип')

    class Meta:
        verbose_name = u'Автомобиль'
        verbose_name_plural = u'Автомобили'

    def __unicode__(self):
        return f'{self.mark} {self.model}'


class UserInfo(models.Model):
    first_name = models.CharField(max_length=20, verbose_name='Имя')
    second_name = models.CharField(max_length=20, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=20, verbose_name='Отчество')
    passport_num = models.CharField(max_length=20, verbose_name='Номер паспорта')
    passport_serial = models.CharField(max_length=20, verbose_name='Серия паспорта')
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
    )
    car = models.ForeignKey(
        CarInfo,
        on_delete=models.CASCADE,
        verbose_name='Автомобиль',
    )

    class Meta:
        verbose_name = u'Информация о пользователе'
        verbose_name_plural = u'Информация о пользователях'

    def __unicode__(self):
        return f'{self.second_name} {self.first_name} {self.patronymic}'


class ElectricCar(models.Model):
    auto = models.CharField(max_length=60, verbose_name='Автомобиль')

    class Meta:
        verbose_name = u'Электрический автомобиль'
        verbose_name_plural = u'Электрические автомобили'

    def __unicode__(self):
        return f'{self.mark} {self.model}'
