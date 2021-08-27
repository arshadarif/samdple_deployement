from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import UserForm,UserInfoForm,LogInForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# Create your views here.
def register(request):

    user = request.user
    user_form = UserForm()
    portfolio_form = UserInfoForm()

    registered = False

    if request.method == "POST":

        user_form = UserForm(data=request.POST)
        portfolio_form = UserInfoForm(data=request.POST)

        if user_form.is_valid() and portfolio_form.is_valid():

            user_save = user_form.save()
            user_save.set_password(user_save.password)
            user_save.save()

            portfolio = portfolio_form.save(commit=False)
            portfolio.user = user_save

            if 'profile_pic' in request.FILES:

                portfolio.profile_pic = request.FILES['profile_pic']
                print(request.FILES['profile_pic'])
            
            portfolio.save()

            registered = True

    return render(request, "basicapp/register.html",{'user_form':user_form,'portfolio_form':portfolio_form,'registered':registered,"user":user})

def log_in(request):

    form = LogInForm()
    user = request.user

    if request.method == "POST":

        form = LogInForm(request.POST)

        if form.is_valid():

            user_authenticate = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data["password"])

            if user_authenticate is not None:
                user = user_authenticate
                login(request, user)
                return HttpResponseRedirect(reverse("basicapp:welcome"))

    return render(request, "basicapp/login.html",{'form':form,'user': user})

@login_required
def welcome(request):

    user = request.user
    return render(request, "basicapp/welcome.html",{"user":user})

@login_required
def log_out(request):

    logout(request)
    return HttpResponseRedirect(reverse("basicapp:login"))