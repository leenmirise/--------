from django.template import loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.shortcuts import render
from .forms import userForm, UserForm
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

            return HttpResponseRedirect("main")
        except User.DoesNotExist:
            # как вставить html код на страницу
            return HttpResponse("<h2>Проверьте правильность логина или пароля :(</h2>")

    else:
        userform = UserForm()
        return render(request, "prac/log.html", {"form": userform})

def reg(request):
    toform = userForm(request.POST)
   
    context = {
      'form': toform,
    }

    if request.method == "POST":
        if toform.is_valid():
            toform.save()
            context['form'] = toform
            return HttpResponseRedirect("index")

    return render(request, 'prac/reg.html.', context)

def main(request):
    return render(request, "prac/main.html")

def sp_dis(request):
    return render(request, "prac/sp_dis.html")

def sp_komp(request):
    return render(request, "prac/sp_komp.html")