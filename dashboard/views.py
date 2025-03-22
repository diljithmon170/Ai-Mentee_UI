from django.shortcuts import render

# def home(request):
#     return render(request, 'index.html')

# def log_sig(request):
#     return render(request, 'log_sig.html')

from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def level(request):
    return render(request, 'level.html', {'user': request.user})
