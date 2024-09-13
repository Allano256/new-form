from django import  forms

class ContactForm(forms.Form):
       first_name = forms.CharField( required=False)
       last_name =forms.CharField( max_length=50, required=False)
       Email=forms.EmailField( required=False)
       Phone=forms.NumberInput()
       country=forms.CharField( required=False)
       company=forms.CharField( max_length=100, required=True)
       reason_for_contact =
       
       forms.Textarea(attrs={
            'rows': 6,
            'cols': 50,
            'placeholder': 'Leave your inquiry here...'
        })

       def clean_email(self):
              email=self.cleaned_data['email']
              if not email.endswith('@example.com'):
                     raise forms.ValidationError('Kindly use an @example.com email adress')
              return email
       
       def clean_telephone_number(self):
              phone_number=self.cleaned_data['phone_number']
              if not phone_number.isdigit():
                     raise forms.ValidationError('The phone number should be only digits.')
              if len(phone_number) < 10 or len(phone_number) > 15:
                     raise forms.ValidationError('The phone numbetr should be between 10 and 15 digits long.')
              return phone_number

       
       
