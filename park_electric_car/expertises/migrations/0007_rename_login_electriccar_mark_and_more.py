# Generated by Django 4.1.3 on 2022-11-19 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expertises', '0006_rename_car_info_id_userinfo_car'),
    ]

    operations = [
        migrations.RenameField(
            model_name='electriccar',
            old_name='login',
            new_name='mark',
        ),
        migrations.RenameField(
            model_name='electriccar',
            old_name='password',
            new_name='model',
        ),
    ]
