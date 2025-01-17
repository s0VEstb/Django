from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm, SMSForm
from django.contrib.auth.models import User
from user.models import Profile, SMScode
import random
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail


def register_view(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, 'user/register.html', context={'form': form})
    elif request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, 'user/register.html', context={'form': form})

        user = User.objects.create_user(
            username=form.cleaned_data['username'],
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password'],
            is_active=True  # Пользователь сразу активен
        )
        Profile.objects.create(
            user=user,
            avatar=form.cleaned_data['avatar'],
            bio=form.cleaned_data['bio'],
            age=form.cleaned_data['age']
        )

        # Автоматический логин после регистрации
        login(request, user)

        return redirect('/products/')


def login_view(request):
    if request.method == "GET":
        form = LoginForm(request.POST)
        return render(request, 'user/login.html', context={'form': form})

    elif request.method == 'POST':
        form = LoginForm(request.POST, request.FILES)

        if not form.is_valid():
            return render(request, 'user/login.html', context={'form': form})

        user = authenticate(**form.cleaned_data)  # User object or None

        if not user:
            form.add_error(None, 'Invalid username or password')
            return render(request, 'user/login.html', context={'form': form})

        login(request, user)
        return redirect('/products/')


# def confirm_sms_view(request):
#     if request.method == 'GET':
#         form = SMSForm()
#         return render(request, 'user/confirm_sms.html', context={'form': form})
#     elif request.method == 'POST':
#         form = SMSForm(request.POST)
#         if not form.is_valid():
#             return render(request, 'user/confirm_sms.html', context={'form': form})
#         sms = form.cleaned_data['SMS']
#         sms_code = SMScode.objects.filter(code=sms).first()
#         if not sms_code:
#             form.add_error(None, 'Invalid code')
#             return render(request, 'user/confirm_sms.html', context={'form': form})
#         sms_code.user.is_active = True
#         sms_code.user.save()
#         sms_code.delete()
#         login(request, sms_code.user)
#         return redirect('/products/')


@login_required(login_url='/login/')
def profile_view(request):
    products = request.user.products.all()
    if request.method == "GET":
        return render(request, 'user/profile.html', context={'products': products})


def logout_view(request):
    logout(request)
    return redirect('main_page')
