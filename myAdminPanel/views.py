import datetime
from django.shortcuts import redirect, render
from . import models
from django.contrib.auth.decorators import user_passes_test,login_required
from django.contrib.auth import authenticate,login,logout
# Create your views here.

# def isAdmin(user):
#     return user

@login_required()
def adminPanel(request):
    if (request.method == "POST"):
        image = request.POST["image"]
        title = request.POST["title"]
        description = request.POST["description"]
        update_date = datetime.datetime.now()
        slugTitle = request.POST["slugTitle".replace(" ", "-")]
        isActive = request.POST.get("isActive", False)
        if isActive == "on":
            isActive = True
        else:
            isActive = False
        # print(image,title,description,update_date,slugTitle,isActive)
        models.myAdminPanel.objects.create(
            image=image, title=title, description=description, update_date=update_date, slugTitle=slugTitle, isActive=isActive)

    values = models.myAdminPanel.objects.all()
    model = {
        'blogValue': values
    }
    return render(request, 'admin/AdminPanel.html', model)


def updated(request, id):
    findValues = models.myAdminPanel.objects.get(id=id)
    model = {
        'value': findValues
    }
    return render(request, 'admin/Update.html', model)
    


def Postupdate(request, id):
    if (request.method == "POST"):
        # _id = request.POST["id"]
        image = request.POST["image"]
        title = request.POST["title"]
        description = request.POST["description"]
        update_date = datetime.datetime.now()
        slugTitle = request.POST["slugTitle".replace(" ", "-")]
        isActive = request.POST.get("isActive", False)
        if isActive == "on":
            isActive = True
        else:
            isActive = False

        updateValue = models.myAdminPanel.objects.get(id=id)
        updateValue.image=image
        updateValue.title=title
        updateValue.description=description
        updateValue.update_date=update_date
        updateValue.slugTitle=slugTitle
        updateValue.isActive=isActive
        updateValue.save()
        return redirect('/MyAdminPanel')
    


def Remove(request,id):
    removeValue = models.myAdminPanel.objects.get(id = id)
    
    removeValue.delete()
    return redirect('/myAdminPanel')
