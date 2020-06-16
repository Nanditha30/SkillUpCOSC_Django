from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def login(request):
    
    #return HttpResponse("hello wassup")
    return render(request,'login.html')
def register(request):
    return render(request,'register.html')

def options(request):
    username=request.POST['email']
    password=request.POST['pass']
    if username == "Admin@cosc.com" and password == "password" :
        return render(request,'options.html')
    else:
        return render(request,'login.html')
    