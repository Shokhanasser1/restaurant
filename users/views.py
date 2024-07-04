from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout
from .forms import *
from .models import Profile




def create_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            login(request, user)
            messages.success(request, "Вы успешно зарегистрировались!")
            return redirect('/')
        else:
            messages.error(request, "Пожалуйста, исправьте ошибки в форме.")
    else:
        form = RegisterForm()
    return render(request, 'create_user.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username_or_email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username_or_email, password=password)

            if user is None:
                try:
                    user_obj = User.objects.get(email=username_or_email)
                    user = authenticate(request, username=user_obj.username, password=password)
                except User.DoesNotExist:
                    user = None
                except User.MultipleObjectsReturned:
                    messages.error(request, 'Несколько пользователей с таким email. Свяжитесь с администратором.')

            if user is not None:
                login(request, user)
                messages.success(request, 'Вы успешно вошли в систему.')
                return redirect('home')
            else:
                messages.error(request, 'Неверное имя пользователя, email или пароль.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'Вы успешно вышли из системы.')
    return redirect('home') 


@login_required
def profile_page(request, author_id: int = None):
    if not request.user.is_authenticated:
        return redirect('login')
    
    user = request.user
    profile = Profile.objects.filter(user__id=author_id).first() if author_id else user.profile

    return render(request, 'profile.html', {'profile': profile})


@login_required
def edit_profile(request):
    profile = Profile.objects.get(user=request.user)  
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Профиль обновлен успешно!')
            return redirect('profile')  
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
    else:
        form = ProfileForm(instance=profile)
        
    return render(request, 'edit_profile.html', {'form': form})