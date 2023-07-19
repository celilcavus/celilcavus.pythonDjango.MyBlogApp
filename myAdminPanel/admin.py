from django.contrib import admin
from . import models
# Register your models here.
class myAdminModel(admin.ModelAdmin):
    list_display = ("id","title")



admin.site.register(models.myAdminPanel,myAdminModel)