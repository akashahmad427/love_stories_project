from django.contrib import admin
from .models import Data
# Register your models here.
@admin.register(Data)
class InformAdmin(admin.ModelAdmin):
    list_display = ['id','name','moral','story']