# Generated by Django 4.1.3 on 2022-11-19 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expertises', '0008_alter_carinfo_options_alter_electriccar_options_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ElectricCar',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='car',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='user',
        ),
        migrations.DeleteModel(
            name='CarInfo',
        ),
        migrations.DeleteModel(
            name='UserInfo',
        ),
    ]
