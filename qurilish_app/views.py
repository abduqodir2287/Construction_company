from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from .forms import Contacts_Forms

def hello(request):
    temp = loader.get_template("hello.html")
    return HttpResponse(temp.render())

def home(request):
    try:
        temp = loader.get_template("home.html")
        return HttpResponse(temp.render())
    except:
        temp = loader.get_template("hello.html")
        return HttpResponse(temp.render())

def about_us(request):
    try:
        temp = loader.get_template("about_us.html")
        return HttpResponse(temp.render())
    except:
        temp = loader.get_template("hello.html")
        return HttpResponse(temp.render())

def services(request):
    try:
        temp = loader.get_template("services.html")
        return HttpResponse(temp.render())
    except:
        temp = loader.get_template("hello.html")
        return HttpResponse(temp.render())

def our_works(request):
    try:
        temp = loader.get_template("our_works.html")
        return HttpResponse(temp.render())
    except:
        temp = loader.get_template("hello.html")
        return HttpResponse(temp.render())

def contacts(request):
    if request.method == "POST":
        form = Contacts_Forms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = Contacts_Forms()

    page = {
        "forms": form
    }
    return render(request, "contacts.html", page)


