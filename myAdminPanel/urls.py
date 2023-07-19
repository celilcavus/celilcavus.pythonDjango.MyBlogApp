from django.urls import path
from . import views

urlpatterns = [
    path('',views.adminPanel,name="postblog"),
    path('/update/<int:id>',views.updated,name="getUpdate"),
    path('/update/record/<int:id>',views.Postupdate,name="update"),
    path('/remove/<int:id>',views.Remove,name="remove")
]
