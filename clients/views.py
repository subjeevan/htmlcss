from django.shortcuts import render
from .form import DairyRegister
# Create your views here.

def form(request):
    regform=DairyRegister()
    return render(request, 'index.html',{'regform':regform})