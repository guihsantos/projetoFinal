# Generated by Django 3.1 on 2020-09-07 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('painelInformacoes', '0003_auto_20200907_2038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='painelinformacoes',
            name='user',
        ),
    ]
