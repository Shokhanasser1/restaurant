
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
import re

class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=50, 
                            widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    first_name = forms.CharField(label='Last name', max_length=100,
                            widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
    last_name = forms.CharField(label='Last name', max_length=100,
                            widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
    email = forms.EmailField(label='Email', max_length=100,
                             widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(label='Password', max_length=50,
                                 widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(label='Confirm Password', max_length=50,
                                 widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Этот email уже используется.")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Это имя пользователя уже используется.")
        return username

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.username = self.data.get('username')
        self.first_name = self.data.get('first_name')
        self.last_name = self.data.get('last_name')
        self.email = self.data.get('email')
        self.password1 = self.data.get('password1')
        self.password2 = self.data.get('password2')

    def is_valid(self):
        form = super(RegisterForm, self).is_valid()

        if self.password1 != self.password2:
            self.add_error('password1', 'Пароль не совпадает')
            self.add_error('password2', 'Пароль не совпадает')
            return False

        self.username_pattern = r'^[a-zA-Z0-9_]{4,}$'
        if not re.match(self.username_pattern, self.username):
            self.add_error('username', 'Имя пользователя должно содержать только буквы, цифры и _')
            return False

        return form 
    
    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password1']
        )
        return user




class LoginForm(forms.Form):
    username = forms.CharField(label='Имя пользователя или Email')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')
    
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.username = self.data.get('username')
        self.password = self.data.get('password1')

    def is_valid(self):
        form = super(LoginForm, self).is_valid()
        return form
        

        
        
class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(label='First name', max_length=100, required=False,
                            widget=forms.TextInput(
                            attrs={'class': 'form-control', "placeholder": "First name"}))
    last_name = forms.CharField(label='Last name', max_length=100, required=False,
                            widget=forms.TextInput(
                                attrs={'class': 'form-control', "placeholder": "Last name"}))




    class Meta:
        model = Profile
        fields = ['user', 'bio']
    

    