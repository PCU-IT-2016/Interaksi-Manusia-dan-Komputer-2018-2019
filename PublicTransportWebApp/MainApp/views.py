from django.shortcuts import render
from MainApp.models import Category, Transportation, Schedule, Account, City
from MainApp.forms import LoginForm

def index(request):
    return render(request, "MainApp/header.html")

def home(request):
    all_categories          = Category.objects.all()
    all_cities              = City.objects.all()
    categories_dictionary   = {
        'all_categories' : all_categories,
        'all_cities'     : all_cities
    }
    return render(request, "MainApp/home.html",categories_dictionary)

def map(request):
    return render(request, "MainApp/map.html")

def new_home(request):
    return render(request, "MainApp/new_home.html")

def schedule_list(request, pk):
    category_id         = pk
    query               = """
    SELECT * FROM MAINAPP_SCHEDULE S 
    JOIN MAINAPP_TRANSPORTATION T ON S.TRANSPORTATION_ID_ID = T.id 
    JOIN MAINAPP_CATEGORY C ON T.CATEGORY_ID_ID = C.id 
    WHERE C.id = {} 
    ORDER BY S.date_time
    """.format(pk)
    all_schedule        = Schedule.objects.raw(query)
    all_cities          = City.objects.all()
    schedule_dictionary = {
        'category_id'  : category_id,
        'all_schedule' : all_schedule,
        'all_cities'   : all_cities
    }
    print(schedule_dictionary)
    # category = Category.objects.all().get(pk=pk)
    # RETURNS 0 OR MORE
    # transportations = Transportation.objects.all().filter(category_id=category)
    # transportations_dictionary = {'all_transportations' : transportations}
    return render(request, "MainApp/schedule_list.html", schedule_dictionary)

def schedule_detail(request, pk):
    query                       = "SELECT * FROM MAINAPP_SCHEDULE S WHERE S.id = " + pk
    schedule                    = Schedule.objects.raw(query)
    schedule_detail_dictionary  = {"schedule" : schedule}
    return render(request, "MainApp/schedule_detail.html", schedule_detail_dictionary)

def login(request):
    if request.method == 'GET':
        return render(request, "MainApp/login.html", {'response' : ""})
    else:
        input_mail      = request.POST.get("inputEmail", "")
        input_pass      = request.POST.get("inputPassword", "")
        found_account   = Account.objects.filter(email=input_mail, password=input_pass)
        if not found_account:
            return render(request, "MainApp/login.html", {'response' : False})
        else:
            return home(request)
        
def register_form(request):
    if request.method == "GET":
        return render(request, "MainApp/register.html")
    else:
        if (request.POST.get("cancelButton")):
            return home(request)
        else: 
            response = True
            # to do list: make migrations -> first name + last name + phone number
            first_name = request.POST.get("firstname")
            last_name  = request.POST.get("lastname")
            password   = request.POST.get("password")
            email      = request.POST.get("email")

            username         = first_name + last_name
            account          = Account()
            account.username = username
            account.password = password
            account.email    = email
            account.save()

            all_categories   = Category.objects.all()
            all_cities       = City.objects.all()

            response_values = {
                'account'        : account ,
                'response'       : response,
                'all_categories' : all_categories,
                'all_cities'     : all_cities,
            }
            return render(request, "MainApp/home.html", response_values)

def contact(request):
    content = {'content' : ['if you would like to contact me, please mail me at', 'm26416083@john.petra.ac.id']}
    return render(request, "MainApp/basic.html", content)