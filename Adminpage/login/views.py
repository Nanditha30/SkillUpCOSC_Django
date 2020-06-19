from django.shortcuts import render
from django.http import HttpResponse
import requests

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
def upload(request):
    return render(request,'upload.html')

def sendvac(request):
    class sv:
        id=10
    global id
    idstr=str(id)
    i=5
    deptname1=request.POST['department']
    position1=request.POST['position']
    reqqual1=request.POST['Qualification']
    percentage1=request.POST['percentage']
    vac = { 'vacant_roll_id':idstr,'Dept_name':deptname1,'Position_vacant':position1,'Required_quali':reqqual1,'percentage':percentage1}
    r=requests.post('https://admintesting.herokuapp.com/addvacantroles',vac)
    id=i+2
    return HttpResponse(r.text)