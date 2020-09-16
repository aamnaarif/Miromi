from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForms
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForms(request.POST)
        if form.is_valid:
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('miromi-home')
    else:
        form = UserRegisterForms(request.POST)
    return render(request, 'users/register.html', {'form': form})
