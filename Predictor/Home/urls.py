from django.urls import path
from .views import contact,predict_by_JEE,predict_by_GUJCET,about
app_name = 'Home'

urlpatterns = [
    path('contact/',contact,name='contact'),
    path('Jee/',predict_by_JEE,name='predict_by_JEE'),
    path('GujCET/',predict_by_GUJCET,name='predict_by_GUJCET'),
    path('',about,name='about')
]