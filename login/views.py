from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import Http404
from django.contrib.auth import login, logout


def sigin_view(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
        else:
            raise Http404("Not valid data")
    else:
        form = AuthenticationForm()
        return render(request, "login/signin.html", {'form': form}) 

def logout_view(request):
    logout(request)
    return redirect('/')

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            raise Http404("Not valid data")
    else:
        form = UserCreationForm()
        return render(request, "login/signup.html", {'form': form})