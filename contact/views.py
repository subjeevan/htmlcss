from django.shortcuts import render,redirect
from contact.form import Contact_Form
from .models import Contact
# Create your views here.
def savedata(request):
    if request.method=='POST':
        name=request.POST.get('name')
        address=request.POST.get('address')
        mobile=request.POST.get('mobile')
        message=request.POST.get('message')
        gender=request.POST.get('gender')
        country=request.POST.getlist('country')
        data=Contact(name=name,address=address,mobile=mobile,message=message,gender=gender,country=country)
        print(data)
        data.save()
        return redirect('show_data')
    print('error data didnt not save')
    return render(request,'contact.html')



def show_data(request,id=None):
    if id is None:
        if request.method=='POST':
            formdata=Contact_Form(request.POST)
            formdata.is_valid()
            print(formdata)
            formdata.save()
            return redirect('show_data')
        else:
            form=Contact_Form()
            data=Contact.objects.all()
            return render(request,'contact.html',{'form':form, 'datas':data})     
    elif id is not None:
         if request.method=='POST':
            edata=Contact.objects.get(id=id)
            formdata=Contact_Form(request.POST,instance=edata)
            formdata.is_valid()
            formdata.save()
            return redirect('show_data')
         else:
            edata=Contact.objects.get(id=id)
            form=Contact_Form(instance=edata)
            data=Contact.objects.all()
            return render(request,'contact.html',{'form':form, 'edata':edata,'datas':data})
    
            
        

def delete_data(request,id):
        data=Contact.objects.get(id=id)
        data.delete()
        return redirect('show_data')
    

