from django.template import loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.shortcuts import render
from .forms import userForm, UserForm, RegUser
from .models import User

# Create your views here.

def index(request):
    return HttpResponse("<h1>Чё-то заработало</h1>")

def log(request):
    if request.method == "POST":
        username = request.POST.get("username")
        userpass = request.POST.get("userpass")     
        try:
            search = User.objects.get(userName=username, userPass=userpass)

            # admin
            if search.userRole == 3:
                return HttpResponseRedirect("reg")

            return HttpResponseRedirect("main")
        except User.DoesNotExist:
            # как вставить html код на страницу
            return HttpResponse("<h2>Проверьте правильность логина или пароля :(</h2>")

    else:
        userform = UserForm()
        return render(request, "prac/log.html", {"form": userform})


def reg(request):
    toform = RegUser(request.POST)
    userform = RegUser()

    if request.method == "POST":
        if toform.is_valid():
            toform.save()
        return render(request, 'prac/reg.html.', {"form": userform})
    else:
        return render(request, 'prac/reg.html.', {"form": userform})


def main(request):
    return render(request, "prac/main.html")

def sp_dis(request):
    return render(request, "prac/sp_dis.html")

def sp_komp(request):
    return render(request, "prac/sp_komp.html")

