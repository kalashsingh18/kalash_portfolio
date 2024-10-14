from django.contrib import admin
from django.urls import path,include
# from update_project import 
from update_project.views import update_project
urlpatterns = [
    path("/update_project/<int:pk>/",update_project.as_view(),name="update_project"),
]