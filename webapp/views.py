from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth import authenticate , login,logout
from .forms import CreateUserForm , LoginForm , CreateRecord , UpdateForm
from django.contrib.auth.decorators import login_required
from .models import Record
from django.db.models import Q
import logging
from django.contrib import messages



def index(request):
    return render(request  , "web/index.html" , {})


def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form  = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request , "Registeration is successfully")
            return redirect('login')
    else:
        form = CreateUserForm()

    context = {
        "form":form
    }

    return render(request , "web/register.html" , context=context)

# Login Function
def sign_in(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request , data=request.POST )
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request , username=username, password=password)
            if user is not None : 
                login(request , user)
                messages.success(request , "Login is successfully")
                return redirect("dashboard")

    else:
        form = LoginForm()           

    context = {
        "form":form
    }

    return render(request , "web/mylogin.html"  , context=context)


@login_required(login_url='login')
def dashboard(request):

    records = Record.objects.all()

    context = {
        "records" : records
    }


    return render(request , "web/dashboard.html"  , context=context)

def logoutView(request):
    logout(request)

    return redirect('login') 

@login_required(login_url="login")
def create_record(request):
    form = CreateRecord()

    if request.method == "POST":
        form = CreateRecord(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request , "Record is Created")
            return redirect("dashboard")

    else:
        form = CreateRecord()

    context = {
        "form":form
    }


    return render(request ,  "web/create-record.html"  , context=context)

@login_required(login_url="login")
def view_record(request , id):
    
    record = get_object_or_404(Record , pk=id)

    context = {
        "record":record
    }

    return render(request , "web/view_record.html" , context=context)



def update_record(request, id):
    
    record = get_object_or_404(Record , id=id)
    form  = UpdateForm(instance=record)

    if request.method == "POST":
        form = UpdateForm(request.POST , instance=record)
        if form.is_valid():
            form.save()
            messages.success(request , "Record Is Updated")
            return redirect('dashboard')

    context = {
        "form":form
    }


    return render(request , "web/update_record.html" , context=context)

@login_required(login_url="login")
def delete_record(request, id):
    record = get_object_or_404(Record , id=id)
    record.delete()
    messages.success(request , "Record Is Deleted .")
    return redirect("dashboard")


logger = logging.getLogger(__name__)


@login_required(login_url="login")
def search(request):
    query = request.GET["query"]
    results = []
    try :
        if query:
            results = Record.objects.filter(Q(first_name__icontains=query) | Q(id__icontains=query))

    except Exception as e:
        logger.error(f"error during Search : {e} ")

    return render(request , "web/search.html" , context={"results" : results , "query":query})



def custom_page(request , exception):
    return render(request , "web/404.html", status=404)

