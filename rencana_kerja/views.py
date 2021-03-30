from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url="/login/")
def dashboard(request):
    context = {
        'title': 'Dashboard'
    }
    return render(request, 'index.html', context)
