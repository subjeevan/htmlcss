from django.contrib import admin
from .models import DairyMembers
# Register your models here.

# admin.site.register(DairyMembers)

@admin.register(DairyMembers)
class DairyList(admin.ModelAdmin):
    list_display=['memb_fname','memb_lname']