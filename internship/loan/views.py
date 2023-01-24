from django.shortcuts import render,redirect
from .forms import empform,signupform
from django.http import HttpResponseRedirect
from .models import empmodel
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(r):
    return render(r,'home.html')

def form(r):
    form = empform()
    if r.method == 'POST':
        form = empform(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(r,'form.html',{'form':form})

@login_required
def detail(r):
    obj = empmodel.objects.all()
    return render(r,'detail.html',{'obj':obj})

def logout(r):
    return render(r,'logout.html')

def login(r):
    return render(r,'login.html')

def signup(r):
    form = signupform()
    if r.method == 'POST':
        form = signupform(r.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            form.save()
            return HttpResponseRedirect('/')
    return render(r,'signup.html',{'form':form})

def delete(r,id):
    obj = empmodel.objects.get(id=id)
    obj.delete()
    return redirect('/employ/detail')

def update(r,id):
    obj = empmodel.objects.get(id=id)
    if r.method=='POST':
        form = empform(r.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('employ/details')
    return render(r,'update.html',{'obj':obj})
