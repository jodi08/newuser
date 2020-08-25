from django.shortcuts import render, HttpResponseRedirect, reverse
from newuserprojec.settings import AUTH_USER_MODEL
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from newuserapp.forms import LogInForm, SignUpForm
from newuserapp.models import New_User

# Create your views here.
@login_required
def main_view(request):
    return render(request, "index.html", {'auth_user_model': AUTH_USER_MODEL})

def login_view(request):
    if request.method == "POST":
        form = LogInForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get("username"), password=data.get("password"))
            if user: 
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse("homepage")))
            
    form = LogInForm()
    return render(request, "login.html", {"form": form})

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = New_User.objects.create_user(username=data.get("username"), password=data.get("password"), displayname = data.get("displayname"))
            login(request, new_user)
            return HttpResponseRedirect(reverse("homepage"))

    form = SignUpForm()
    return render(request, 'signup.html', {"form": form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))