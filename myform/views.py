from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from django.contrib import messages
from django.views import View


# Create your views here.

def form_view(request):

    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            first_name=form.cleaned_data['first_name']
            last_name =form.cleaned_data['last_name']
            email =form.cleaned_data['email']
            phone_number=form.cleaned_data['phone_number']
            country=form.cleaned_data['country']
            company=form.cleaned_data['company']
            reason_for_contact=form.cleaned_data['reason_for_contact']

            #Send email
            send_mail(
                 'Contact Form Submission', #Subject
            reason_for_contact, #message body
            email, #From email 

            ['private_email@eaxmple.com'], #To email, this will be replaced with your private email
            fail_silently=False # Raise an exception if email sending fails

            )
            messages.success(request,'Your inquiry was successfully sent!' )

            
    else:
            form=ContactForm()

    return render(request, 'myform/my_form.html', {'form':form})

            

