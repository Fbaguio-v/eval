from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views import View
# Create your views here.
# Create your views here.

class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'register/register.html', {'form' : form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('register')