"""
URL configuration for diary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from clients.views import form
from collection.views import col_form
from modelform.views import homepage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', form, name='form'),
    path('collection/',col_form,name='col_form'),
]

from modelform.views import delform,editform

modelform=[
    path('homepage/',homepage,name='homepage'),
    path('delform/<int:id>/', delform, name='delform'),
    path('editform/<int:id>/',editform,name='editform'),
]
urlpatterns.extend(modelform)

contact=[
    path('contact/',include('contact.urls')),
]

urlpatterns.extend(contact)