from django import forms
from .models import Contact,Predict_Gujcet,Predict_JEE
from django.contrib.auth.models import User

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"


class GujCET_form(forms.ModelForm):
    class Meta:
        model = Predict_Gujcet
        fields = ['twelve_board','twelve_marks','GUJCET_marks','enter_category','choose_field']
        widgets = {
            'twelve_board': forms.TextInput(attrs={'class': 'form-control'}),
            'twelve_marks': forms.TextInput(attrs={'class': 'form-control'}),
            'GUJCET_marks': forms.NumberInput(attrs={'class': 'form-control'}),
            'enter_category': forms.TextInput(attrs={'class': 'form-control'}),
            'choose_field': forms.TextInput(attrs={'class': 'form-control'}),
        }

class JEE_form(forms.ModelForm):
    class Meta:
        model = Predict_JEE
        fields = ['twelve_board','twelve_marks','JEE_marks','enter_category','choose_field']
        widgets = {
            'twelve_board': forms.TextInput(attrs={'class': 'form-control'}),
            'twelve_marks': forms.TextInput(attrs={'class': 'form-control'}),
            'JEE_marks': forms.NumberInput(attrs={'class': 'form-control'}),
            'enter_category': forms.TextInput(attrs={'class': 'form-control'}),
            'choose_field': forms.TextInput(attrs={'class': 'form-control'}),
        }

