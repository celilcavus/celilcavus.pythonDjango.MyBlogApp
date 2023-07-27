from django.urls import path
from accountant import views

urlpatterns = [
    path('/admin_login',views.admin_login,name="admin_login"),
    path('/admin_register',views.admin_register,name="admin_register"),
    path('admin_logout',views.admin_logout,name="admin_logout")
]
