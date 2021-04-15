from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def register(request):
    from = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})