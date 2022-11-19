from django.contrib import admin
# Из модуля models импортируем модель Post
from .models import UserInfo, CarInfo, ElectricCar

admin.site.register(UserInfo)
admin.site.register(CarInfo)
admin.site.register(ElectricCar)
