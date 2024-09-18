
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from django.contrib import messages
from django.views import View
import os

# Create your views here.

class FormView(View):
     
    def post(self, request):  
        form=ContactForm(request.POST)
        if form.is_valid():
            first_name=form.cleaned_data['first_name']
            last_name =form.cleaned_data['last_name']
            email =form.cleaned_data['email']
            phone_number=form.cleaned_data['phone_number']
            country=form.cleaned_data['country']
            company=form.cleaned_data['company']
            reason_for_contact=form.cleaned_data['reason_for_contact']

            from_email = settings.DEFAULT_FROM_EMAIL

            # Construct the email content
            subject = 'Contact Form Submission'
            message = (
                f'Name: {first_name} {last_name}\n'
                f'Email: {email}\n'
                f'Phone Number: {phone_number}\n'
                f'Country: {country}\n'
                f'Company: {company}\n\n'
                f'Reason for Contact:\n{reason_for_contact}'
            )

           
            try:
                send_mail(
                    subject,
                    message,
                    from_email,
                    ['xxxxxxxxx'],  # Replace here with  Mailtrap inbox email
                    fail_silently=False
                )
                messages.success(request, 'Your inquiry was successfully sent!')
            except Exception as e:
                messages.error(request, f'Error sending email: {e}')

        return render(request, 'myform/my_form.html', {'form': form})

