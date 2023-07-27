from django.shortcuts import redirect, render
# from django.contrib.auth.decorators import user_passes_test,login_required
from django.contrib.auth import authenticate,login,logout
# Create your views here.
from django.contrib.auth.models import User
error_message = {
    'error':"kullanici adi veya sifre yanlis!"
}

def admin_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, "admin/login.html",error_message)
    else:
        return render(request,"admin/login.html")
    
   

def admin_register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username,password=password)
        user.save()
        return redirect('/admin_login')
    else:
        return render(request,'admin/register.html')
def admin_logout(request):
    logout(request)
    return redirect('/myAdminPanel')
    