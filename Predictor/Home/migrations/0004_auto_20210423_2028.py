# Generated by Django 3.2 on 2021-04-23 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_remove_predict_gujcet_given_entrance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predict_gujcet',
            name='GUJCET_marks',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='predict_gujcet',
            name='twelve_marks',
            field=models.FloatField(),
        ),
    ]
