from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import SignupForm, LoginForm

def home(request):
    return render(request, 'index.html')

def log_sig(request):
    if request.method == 'POST':
        if 'name' in request.POST:  # Signup form
            form = SignupForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account created successfully! Please log in.')
                return redirect('log_sig')
            else:
                print(form.errors)  # Debugging: Print form errors to the terminal
                messages.error(request, 'Error creating account. Please check the form.')
        else:  # Login form
            form = LoginForm(data=request.POST)
            if form.is_valid():
                user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
                if user is not None:
                    login(request, user)
                    return redirect('dashboard')
                else:
                    messages.error(request, 'Invalid email or password.')
            else:
                messages.error(request, 'Error logging in. Please check the form.')

    signup_form = SignupForm()
    login_form = LoginForm()
    return render(request, 'log_sig.html', {'signup_form': signup_form, 'login_form': login_form})

def dashboard(request):
    return render(request, 'dashboard.html')