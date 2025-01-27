from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def log_sig(request):
    return render(request, 'log_sig.html')

def dashboard(request):
    return render(request, 'dashboard.html')