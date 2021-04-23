from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import ContactForm, GujCET_form,JEE_form
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import pandas as pd


# Create your views here.



def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST or None)
        if form.is_valid():
            contact_name = form.cleaned_data['name']
            contact_email = form.cleaned_data['email']
            sub = form.cleaned_data['subject']
            content = form.cleaned_data['message']
            # print(contact_name)
            form.save()
            subject = 'Hello ' + contact_name + ' from predictor!'
            message = 'Stay Connected. We would love to hear you!'
            email_from = settings.EMAIL_HOST_USER
            email_to = [contact_email, ]
            send_mail(subject, message, email_from, email_to)
            messages.success(request, 'Form submitted successfully.')
            return redirect('Home:Home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = ContactForm()
    template = 'contact.html'
    return render(request, template, {'form': form})




@login_required
def predict_by_GUJCET(request):
    if request.method == 'POST':
        form = GujCET_form(request.POST or None)
        if form.is_valid():
            form.save()
            df1 = pd.read_excel("Final.xlsx")
            print(df1)
            twelve_board = request.POST['twelve_board']
            twelve_marks = float(request.POST['twelve_marks']) * 0.6
            GUJCET_marks = float(request.POST['GUJCET_marks']) * 0.4
            Final_GM = twelve_marks + GUJCET_marks
            category = request.POST['enter_category']
            choose_field = request.POST['choose_field']
            df2 = df1[(df1["XIIth Board"] == twelve_board) & (df1["Entrance given"] == 'GUJCET')]
            df2 = df2[(df2["Field"] == choose_field) & (df2["Final_J"] <= Final_GM)]
            df2 = df2[(df2["Category"] == category)]
            df2 = df2['College/University']

            print(df2)
            return render(request, 'gujcet.html', {'form': form, 'predictions': df2})
        else:
            messages.error(request,'Please correct the error below')
    else:
        form = GujCET_form()

    return render(request, 'gujcet.html', {'form': form})


@login_required
def predict_by_JEE(request):
    if request.method == 'POST':
        form = JEE_form(request.POST or None)
        if form.is_valid():
            form.save()
            df1 = pd.read_excel("Final.xlsx")
            print(df1)
            twelve_board = request.POST['twelve_board']
            twelve_marks = float(request.POST['twelve_marks']) * 0.6
            JEE_marks = float(request.POST['JEE_marks']) * 0.4
            Final_GM = twelve_marks + JEE_marks
            category = request.POST['enter_category']
            choose_field = request.POST['choose_field']
            df2 = df1[(df1["XIIth Board"] == twelve_board) & (df1["Entrance given"] == 'GUJCET')]
            df2 = df2[(df2["Field"] == choose_field) & (df2["Final_J"] <= Final_GM)]
            df2 = df2[(df2["Category"] == category)]
            df2 = df2['College/University']

            print(df2)
            return render(request, 'jee.html', {'form': form, 'predictions': df2})
        else:
            messages.error(request,'Please correct the error below')
    else:
        form = JEE_form()
    return render(request, 'jee.html', {'form': form})


def about(request):
    return render(request,'about.html')