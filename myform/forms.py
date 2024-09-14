from django import  forms
from django_countries.fields import CountryField


class ContactForm(forms.Form):
       first_name = forms.CharField( required=False)
       last_name =forms.CharField( max_length=50, required=False)
       Email=forms.EmailField( required=False)
       Phone=forms.RegexField(
        regex=r'^\+?1?\d{9,15}$', 
        error_messages={
            'invalid': 'Enter a valid phone number. This value may contain only numbers, and should be between 9 and 15 digits long.'
        },
        max_length=15
        )
       country =CountryField().formfield(
        widget=forms.Select(attrs={'class': 'country-picker'})
    )
       company=forms.CharField( max_length=100, required=True)
       reason_for_contact = forms.CharField(
        max_length=250,  
        widget=forms.TextInput(attrs={'placeholder': 'Reason for contact'})
       )
       
       

       def clean_email(self):
              email=self.cleaned_data['email']
              if not email.endswith('@example.com'):
                     raise forms.ValidationError('Kindly use an @example.com email adress')
              return email
      

       
       
