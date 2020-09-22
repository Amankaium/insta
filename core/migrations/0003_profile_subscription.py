# Generated by Django 3.1.1 on 2020-09-19 13:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_auto_20200917_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='subscription',
            field=models.ManyToManyField(related_name='subscriber', to=settings.AUTH_USER_MODEL, verbose_name='Подписка'),
        ),
    ]