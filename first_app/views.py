from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    my_dict={ "add_me" : "test to render add me"}
    return render(request,'index.html',context=my_dict)

def add(request):
    return HttpResponse("<h1>hello {} Welcome To Asc !!  </ha>".format(request.GET.get('message')))

