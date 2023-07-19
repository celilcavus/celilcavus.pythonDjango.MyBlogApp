from django.urls import path

from BlogView import views


urlpatterns = [
    path('',views.index)
]
