from django.urls import path

from BlogView import views


urlpatterns = [
    path('',views.index),
    path('details/<int:id>',views.blogDetails,name="blog_details")
]
