# Generated by Django 3.2 on 2021-04-23 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_predict_jee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='predict_gujcet',
            name='user',
        ),
        migrations.RemoveField(
            model_name='predict_jee',
            name='user',
        ),
    ]
