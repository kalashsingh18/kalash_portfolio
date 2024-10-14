from django.contrib import admin
from django.urls import path,include
from add_project.views import add_project,listallproject
urlpatterns = [
   path("",add_project,name="create_project"),
   path("/list",listallproject.as_view(),name="listallproject"),
]