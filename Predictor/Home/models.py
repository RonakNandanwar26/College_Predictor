from django.db import models
import pandas as pd
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.TextField(default='')

    def __str__(self):
        return self.name


class Predict_Gujcet(models.Model):
    twelve_board = models.CharField(max_length=10)
    twelve_marks = models.FloatField()
    GUJCET_marks = models.FloatField()
    enter_category = models.CharField(max_length=10)
    choose_field = models.CharField(max_length=50)

    def __str__(self):
        return self.user.name



class Predict_JEE(models.Model):
    twelve_board = models.CharField(max_length=10)
    twelve_marks = models.FloatField()
    JEE_marks = models.FloatField()
    enter_category = models.CharField(max_length=10)
    choose_field = models.CharField(max_length=50)

    def __str__(self):
        return self.user.name