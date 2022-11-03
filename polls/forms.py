from django import forms
from django.core.validators import EmailValidator
from django.core.validators import RegexValidator, FileExtensionValidator
from .models import User, Question, Choice

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
        if not cd['avatar']:
           cd['avatar'] = 'images/profile/grey_avatar.png'
        return cd['avatar']

class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(label='Username', widget=forms.TextInput,
                               validators=[RegexValidator(r'[a-zA-Z\-]', 'В логине доступны только латинские символы')],
                               required=True)

    full_name = forms.CharField(label='ФИО', widget=forms.TextInput,
                                validators=[RegexValidator(r'[а-яА-ЯёЁ\-\s]',
                                                           'В ФИО доступна только кириллица, пробелы и дефис')],
                                required=True)
    email = forms.EmailField(label='Email', widget=forms.EmailInput, required=True,
                             validators=[EmailValidator('Email не верен')])
    avatar = forms.ImageField(label="Pic an avatar",
                              validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'bmp'])],
                              required=False)



    def clean_avatar(self):
        cd = self.cleaned_data
        if not cd['avatar']:
           cd['avatar'] = '/images/profile/grey_avatar.png'
        return cd['avatar']
    class Meta:
        model = User
        fields = ['avatar', 'full_name', 'username', 'email']

class add_qForm(forms.ModelForm):
    img = forms.ImageField(label="Pic an avatar",
                              validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'bmp'])],
                              required=False)

    question_text = forms.CharField(label='Вопрос', widget=forms.TextInput, required=True)
    description = forms.CharField(label='Описание', widget=forms.TextInput, required=True)
    num_of_questions = forms.IntegerField(label='Количество вариантов', required=True)

    def clean_num_of_questions(self):
        cd = self.cleaned_data
        if cd['num_of_questions'] < 2 or cd['num_of_questions'] > 10:
            raise forms.ValidationError('Число вариантов не может быть меньше 2 а также больше 10')
        return cd['num_of_questions']

    def clean_img(self):
        cd = self.cleaned_data
        return cd['img']
    class Meta:
        model = Question
        fields = ['img', 'question_text', 'description', 'num_of_questions']

class add_optionsForm(forms.ModelForm):
    choice_text = forms.CharField(label='Вопрос', widget=forms.TextInput, required=True)

    def clean_cjoice_text(self):
        cd = self.cleaned_data
        if cd['choice_text'] == False:
            raise forms.ValidationError('Поле обязательно для заполнения')
        return cd['choice_text']

    class Meta:
        model = Choice
        fields = ['choice_text']

