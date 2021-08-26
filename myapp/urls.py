"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os import name
from django.contrib import admin
from django.urls import path ,include
#newly imported
from myapp import views
urlpatterns = [
    path("",views.index,name="myapp"),
    path("contact",views.contact,name="contact"),
    path("about",views.about,name="about"),
    path("Dsa",views.Dsa,name="Dsa"),
    path("bst",views.bst,name="bst"),
    path("call_address",views.call_address,name="call_address"),
    path("call_ref",views.call_ref,name="call_ref"),
    path("classs",views.classs,name="classs"),
    path("common",views.common,name="common"),
    path("compcalc",views.compcalc,name="compcalc"),
    path("complex_python",views.complex_python,name="complex_python"),
    path("database",views.database,name="database"),
    path("defaultcons",views.defaultcons,name="defaultcons"),
    path("dyna_ini",views.dyna_ini,name="dyna_ini"),
    path("factorial",views.factorial,name="factorial"),
    path("even_sum",views.even_sum,name="even_sum"),
    path("func_overload",views.func_overload,name="func_overload"),
    path("hello",views.hello,name="hello"),
    path("inline",views.inline,name="inline"),
    path("linked",views.linked,name="linked"),
    path("multi",views.multi,name="multi"),
    path("navbar",views.navbar,name="navbar"),
    path("new",views.new,name="new"),
    path("newfile",views.newfile,name="newfile"),
    path("oddeven",views.oddeven,name="oddeven"),
    path("OOPindex",views.OOPindex,name="OOPindex"),
    path("op_comp",views.op_comp,name="op_comp"),
    path("ops1",views.ops1,name="ops1"),
    path("paramet",views.paramet,name="paramet"),
    path("polynomial",views.polynomial,name="polynomial"),
    path("postfix",views.postfix,name="postfix"),
    path("privacy",views.privacy,name="privacy"),
    path("pystring",views.pystring,name="pystring"),
    path("pysub",views.pysub,name="pysub"),
    path("pysum",views.pysum,name="pysum"),
    path("python",views.python,name="python"),
    path("qlink",views.qlink,name="qlink"),
    path("query",views.query,name="query"),
    path("queue",views.queue,name="queue"),
    path("queuepointer",views.queuepointer,name="queuepointer"),
    path("random",views.random,name="random"),
    path("refer_var",views.refer_var,name="refer_var"),
    path("revprint",views.revprint,name="revprint"),
    path("sortingcpp",views.sortingcpp,name="sortingcpp"),
    path("stack_class",views.stack_class,name="stack_class"),
    path("stack",views.stack,name="stack"),
    path("stacklink",views.stacklink,name="stacklink"),
    path("stackpointer",views.stackpointer,name="stackpointer"),
    path("strongnum",views.strongnum,name="strongnum"),
    path("strpal",views.strpal,name="strpal"),
    path("sum(",views.sum,name="sum"),
    path("swap_val",views.swap_val,name="swap_val"),
    path("tandc",views.tandc,name="tandc"),
    path("unary",views.unary,name="unary"),
    path("signup",views.signup,name="signup"),
    path("login",views.loginuser,name="login"),
    path("logout",views.logoutuser,name="logout")
    
]
