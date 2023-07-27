from django.shortcuts import render
import myAdminPanel.models
# from ..myAdminPanel.models import myAdminPanel
# Create your views here.
def index(request):
    postValue = myAdminPanel.models.myAdminPanel.objects.all().filter(isActive = True)

    values = {
        'value':postValue
    }

    return render(request,"pages/index.html",values)

def blogDetails(request,id):
    getValue = myAdminPanel.models.myAdminPanel.objects.get(pk=id)
    findValue = {
        'findVal':getValue
    }
    return render(request,'pages/details.html',findValue)