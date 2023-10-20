from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from .models import User
from django import forms
from phonenumber_field.formfields import PhoneNumberField


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите имя пользователя'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Введите пароль'
    }))

    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'


class UserProfileForm(UserChangeForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'read_only': True}))
    phone_number = PhoneNumberField(widget=forms.TextInput(attrs={'placeholder': 'Ваш номер телефона'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Ваша электронная почта'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ваше имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ваша фамилия'}))
    father_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ваше отчество'}))
    company_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Название компании'}))

    class Meta:
        model = User
        fields = ('username', 'phone_number', 'email', 'first_name', 'last_name', 'father_name', 'image', 'company_name')

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class AvatarUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('image',)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput)
    image = forms.ImageField(label='Ваш лого', required=False)

    class Meta:
        model = User
        fields = ('username', 'phone_number', 'email', 'first_name', 'last_name', 'father_name', 'company_name', 'image')
    
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['phone_number'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['father_name'].widget.attrs['class'] = 'form-control'
        self.fields['company_name'].widget.attrs['class'] = 'form-control'
        self.fields['image'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['confirm_password'].widget.attrs['class'] = 'form-control'


    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('Пароли не совпадают')
        return confirm_password

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user