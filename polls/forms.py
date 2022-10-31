from django import forms
from django.core.validators import EmailValidator
from django.core.validators import RegexValidator, FileExtensionValidator
from .models import User

class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Username', widget=forms.TextInput,
                               validators=[RegexValidator(r'[a-zA-Z\-]', 'В логине доступны только латинские символы')],
                               required=True)

    full_name = forms.CharField(label='ФИО', widget=forms.TextInput,
                                validators=[RegexValidator(r'[а-яА-ЯёЁ\-\s]',
                                                           'В ФИО доступна только кириллица, пробелы и дефис')],
                                required=True)

    password = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput, required=True)
    email = forms.EmailField(label='Email', widget=forms.EmailInput, required=True,
                             validators=[EmailValidator('Email не верен')])
    avatar = forms.ImageField(label="Pic an avatar", validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'bmp'])],
                              required=False)
    checkbox = forms.CharField(label='Privet information permission', widget=forms.CheckboxInput,
                               required=False)

    class Meta:
        model = User
        fields = ['avatar', 'full_name', 'username', 'email', 'password', 'password2']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']

    def clean_checkbox(self):
        cd = self.cleaned_data
        if cd['checkbox'] == False:
            raise forms.ValidationError('Подтвердите обработку персональных данных')
        return cd['checkbox']

    def clean_avatar(self):
        cd = self.cleaned_data
        if cd['avatar'] == None:
           cd['avatar'] = '/media/images/profile/grey_avatar.png'
        return cd['avatar']

class AuthenticationForm(forms.ModelForm):
    username = forms.CharField(label='Username', widget=forms.TextInput,
                               validators=[RegexValidator(r'[a-zA-Z\-]', 'В логине доступны только латинские символы')],
                               required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = ['username', 'password']