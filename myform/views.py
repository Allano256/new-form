from django.shortcuts import render
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

            form.save()
            messages.succes(request, 'Your inquiry was successfully sent!')
        else:
            messages.error(request, 'Please check that all fields are filledout correctly!')
    else:
            form=ContactForm()

    return render(request, 'myform/my_form.html', {'form':form})

            

