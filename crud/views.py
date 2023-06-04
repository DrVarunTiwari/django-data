from django.shortcuts import render,redirect
from .models import student
# Create your views here.

def home(request):
    std=student.objects.all()
    return render(request,'home.html',{'std':std})

def add(request):
    return render(request,'add.html')

def addrec(request):
    a=request.POST['sid']
    b=request.POST['sname']
    c=request.POST['sage']
    d=request.POST['sadd']
    std=student(sid=a,sname=b,sage=c,sadd=d)
    std.save()
    return redirect("/")

def delete(request,id):
    std=student.objects.get(id=id)
    std.delete()
    return redirect("/")

def update(request,id):
    std=student.objects.get(id=id)
    return render(request,'update.html',{'std':std})

def uprec(request,id):
    a=request.POST['sid']
    b=request.POST['sname']
    c=request.POST['sage']
    d=request.POST['sadd']
    std=student.objects.get(id=id)
    std.sid=a
    std.sname=b
    std.sage=c
    std.sadd=d
    std.save()
    return redirect("/")