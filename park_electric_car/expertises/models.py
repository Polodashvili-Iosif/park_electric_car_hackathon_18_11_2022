from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class CarInfo(models.Model):
    mark = models.CharField(max_length=30)
    engine_model = models.CharField(max_length=30)
    chassis_number = models.CharField(max_length=30)
    vin = models.CharField(max_length=17)
    state_number = models.CharField(max_length=8)
    model = models.CharField(max_length=30)
    release_year = models.IntegerField()


class UserInfo(models.Model):
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    patronymic = models.CharField(max_length=20)
    passport_num = models.CharField(max_length=20)
    passport_serial = models.CharField(max_length=20)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    car = models.ForeignKey(
        CarInfo,
        on_delete=models.CASCADE,

    )


class ElectricCar(models.Model):
    mark = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
