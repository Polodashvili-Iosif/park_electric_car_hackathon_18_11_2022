# Generated by Django 4.1.3 on 2022-11-19 01:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.CharField(max_length=30)),
                ('engine_model', models.CharField(max_length=30)),
                ('chassis_number', models.CharField(max_length=30)),
                ('vin', models.CharField(max_length=17)),
                ('state_number', models.CharField(max_length=8)),
                ('model', models.CharField(max_length=30)),
                ('release_year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ElectricCars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('second_name', models.CharField(max_length=20)),
                ('patronymic', models.CharField(max_length=20)),
                ('passport_num', models.CharField(max_length=20)),
                ('passport_serial', models.CharField(max_length=20)),
                ('car_info_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expertises.carinfo')),
                ('user_info_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expertises.userinfo')),
            ],
        ),
    ]