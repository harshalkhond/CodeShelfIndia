from django.conf.urls import url
from django.shortcuts import render ,HttpResponse,redirect
from myapp.models import Contact, Feedback
from datetime import datetime
from django.contrib.auth import authenticate ,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import IntegrityError
# Create your views here.
def index(request):
    if request.user.is_anonymous:
        print(request.user.is_anonymous)
        return redirect("/login")
    return render(request,"index.html")
def loginuser(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username)
        print(password)
        user=authenticate(username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            return render(request,"login.html")
    return render(request,"login.html")
def logoutuser(request):
    logout(request)
    return redirect("/login")
def contact(request):
    if request.user.is_anonymous:
        return redirect("/login")
    if request.method=="POST":
        name=request.POST.get('name')
        feedback=request.POST.get('feedback')
        suggestion=request.POST.get('suggestion')
        feedback=Feedback(name=name,feedback=feedback,suggestion=suggestion)
        feedback.save()
        messages.success(request,"Submitted Successfully")
    return render(request,"contact.html")
def signup(request):
    try:
        if request.method=="POST":
            name=request.POST.get('name')
            username=request.POST.get('username')
            password=request.POST.get('password')
            email=request.POST.get('email')
            number=request.POST.get('number')
            contact=Contact(name=name,username=username,password=password,number=number,email=email)
            myuser=User.objects.create_user(username,email,password)
            myuser.first_name=name
            myuser.save()
            contact.save()
            return render(request,"login.html")
    except IntegrityError:
        messages.error(request,"signup not successful Try again")
    return render(request,"signup.html")

def about(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,"about.html")

def Dsa(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,"Dsa.html")

def bst(request):
    return render(request,"bst.html")

def call_address(request):
    return render(request,"call_address.html")

def call_ref(request):
    return render(request,"call_ref.html")

def classs(request):
    return render(request,"classs.html")

def common(request):
    return render(request,"common.html")

def compcalc(request):
    return render(request,"compcalc.html")

def complex_python(request):
    return render(request,"complex_python.html")

def database(request):
    return render(request,"database.html")

def defaultcons(request):
    return render(request,"defaultcons.html")

def dyna_ini(request):
    return render(request,"dyna_ini.html")

def even_sum(request):
    return render(request,"even_sum.html")

def factorial(request):
    return render(request,"factorial.html")

def func_overload(request):
    return render(request,"func_overload.html")

def hello(request):
    return render(request,"hello.html")

def inline(request):
    return render(request,"inline.html")
def linked(request):
    return render(request,"linked.html")
def multi(request):
    return render(request,"multi.html")
def navbar(request):
    return render(request,"navbar.html")
def new(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,"new.html")
def newfile(request):
    return render(request,"newfile.html")
def oddeven(request):
    return render(request,"oddeven.html")
def OOPindex(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,"OOPindex.html")
def op_comp(request):
    return render(request,"op_comp.html")
def ops1(request):
    return render(request,"ops1.html")
def paramet(request):
    return render(request,"paramet.html")
def polynomial(request):
    return render(request,"polynomial.html")
def postfix(request):
    return render(request,"postfix.html")
def privacy(request):
    return render(request,"privacy.html")
def pystring(request):
    return render(request,"pystring.html")
def pysub(request):
    return render(request,"pysub.html")
def pysum(request):
    return render(request,"pysum.html")
def python(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,"python.html")
def qlink(request):
    return render(request,"qlink.html")
def query(request):
    return render(request,"query.html")
def queue(request):
    return render(request,"queue.html")
def queuepointer(request):
    return render(request,"queuepointer.html")
def random(request):
    return render(request,"random.html")
def refer_var(request):
    return render(request,"refer_var.html")
def revprint(request):
    return render(request,"revprint.html")
def sortingcpp(request):
    return render(request,"sortingcpp.html")
def stack_class(request):
    return render(request,"stack_class.html")
def stack(request):
    return render(request,"stack.html")
def stacklink(request):
    return render(request,"stacklink.html")
def stackpointer(request):
    return render(request,"stackpointer.html")
def strongnum(request):
    return render(request,"strongnum.html")
def strpal(request):
    return render(request,"strpal.html")
def sum(request):
    return render(request,"sum.html")
def swap_val(request):
    return render(request,"swap_val.html")
def tandc(request):
    return render(request,"tandc.html")
def unary(request):
    return render(request,"unary.html")
