from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django import forms
from phonenumber_field.formfields import PhoneNumberField
from .models import Company


class CompanyRegistrationForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ('company_name', 'phone_number', 'email', 'company_information', 'image')
    
    def __init__(self, *args, **kwargs):
        super(CompanyRegistrationForm, self).__init__(*args, **kwargs)

        self.fields['phone_number'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['company_name'].widget.attrs['class'] = 'form-control'
        self.fields['company_information'].widget.attrs['class'] = 'form-control'
        self.fields['image'].widget.attrs['class'] = 'form-control'




