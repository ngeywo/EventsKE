from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterUserForm, UserUpdateForm, ProfileUpdateForm



# Create your views here.
def login_user(request):
    if request.method== "POST":
        username = request.POST['username']
        password = request.POST['password']
        user= authenticate(request,username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('homee')

        else:
            messages.success(request, 'There Was An Error Loging In, Try Again!')
            return redirect('login')

    else:

        return render(request, 'registrarion/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, f'Logout successful!')
    return render(request, 'registrarion/logout.html', {} )

def register_user(request):
    if request.method == "POST":
        form= RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request,user)
            messages.success(request, f'Registration successful!')
            return redirect('homee')

    else:
        form = RegisterUserForm()

    return render(request, 'registration/signup.html',{'form':form, })

@login_required()
def profile(request):
    if request.method == "POST":
        U_form = UserUpdateForm(request.POST or None, instance = request.user)
        p_form = ProfileUpdateForm(request.POST or None, request.FILES, instance = request.user.profile)
        if U_form.is_valid() and p_form.is_valid():
            U_form.save()
            messages.success(request, f'Your account has been Updated!')
            return redirect('profile')

    else:
        U_form = UserUpdateForm(request.POST or None, instance=request.user)
        p_form = ProfileUpdateForm(request.POST or None, request.FILES, instance=request.user.profile)


    return render(request, 'registration/profile.html',{'U_form':U_form, 'p_form':p_form })

#
# def Password_reset(request):
#      return render(request, 'registration/password_reset.html', { })

#
# def Password_reset_done(request):
#     return render(request, 'registration/password_reset_done.html', {})