# Generated by Django 3.1.1 on 2020-09-17 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publication',
            old_name='user',
            new_name='publisher',
        ),
    ]
