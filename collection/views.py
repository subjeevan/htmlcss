from django.shortcuts import render
from .collectionform import Col_Form
def col_form(request):
    if request.method=='POST':
        form=Col_Form
        if form.is_valid:
            form.save()
    return render(request,'collection.html',{'col_form':col_form})
    
