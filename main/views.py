from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    myname = "Phú mập"
    context = {"name":myname}
    return render(request,"main/base.html/", context)