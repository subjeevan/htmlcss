from django.shortcuts import render,redirect
from .form import MemberForm
from django.contrib import messages
from .models import Members
import pdb

# Create your views here.

def homepage(request):
    if request.method=='POST':
        formdata=MemberForm(request.POST)
        formdata.is_valid
        formdata.save()
        messages.success(request,"Data Saved Successfully")
        return redirect('homepage')
    else:
        datas=Members.objects.all()
        form=MemberForm()
    return render (request, 'homepage.html',{'form':form,'datas':datas})

def delform(request,id):
    deldata=Members.objects.get(id=id)
    deldata.delete()
    return redirect('homepage')

def editform(request,id):
    data=Members.objects.get(id=id)
    if request.method=='POST':
        form=MemberForm(request.POST,instance=data)
        form.is_valid
        form.save()
        return redirect('homepage')
    form=MemberForm(instance=data)
    return render(request,'update.html',{'form':form})
    
