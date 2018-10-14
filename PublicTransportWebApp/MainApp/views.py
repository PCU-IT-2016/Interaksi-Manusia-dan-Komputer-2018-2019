from django.shortcuts import render
from MainApp.models import Category, Transportation
def index(request):
    return render(request, "MainApp/header.html")

def home(request):
    all_categories = Category.objects.all()
    categories_dictionary = {'all_categories' : all_categories}
    return render(request, "MainApp/home.html",categories_dictionary)

# SHOULD RETURNS A SCHEDULE INSTEAD OF A LIST OF TRANSPORTATIONS
def info(request, pk):
    # RETURNS 1
    category = Category.objects.all().get(pk=pk)
    # RETURNS 0 OR MORE
    transportations = Transportation.objects.all().filter(category_id=category)
    transportations_dictionary = {'all_transportations' : transportations}
    print("AAAAAA")
    return render(request, "MainApp/info.html", transportations_dictionary)

def contact(request):
    content = {'content' : ['if you would like to contact me, please mail me at', 'mail@mail.com']}
    return render(request, "MainApp/basic.html", content)