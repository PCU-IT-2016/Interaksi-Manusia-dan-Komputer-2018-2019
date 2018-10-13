from django.shortcuts import render

def index(request):
    return render(request, "MainApp/header.html")

def contact(request):
    content = {'content' : ['if you would like to contact me, please mail me at', 'mail@mail.com']}
    return render(request, "MainApp/basic.html", content)